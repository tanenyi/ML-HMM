# # # # #
#
#	Start of Setup
#
#

import csv
import math

#
#
#	End of Startup
#
# # # # #



# # # # #
#
#	Start of Question 1
#
#

seqlist = []
tag_count = {}
rawDB = {}

# Read data from file and sort into tags
with open("Project Data/train", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	subseqlist = ["*"]
	for row in rd:
		# ignore empty line
		if row == []:
			subseqlist.append("STOP")
			seqlist.append(subseqlist)
			subseqlist = ["*"]
		else:
			subseqlist.append(row[1])

for i in seqlist:
	for j in range(len(i)-1):
		if i[j] not in rawDB:
			rawDB[i[j]] = {}
		if i[j+1] not in rawDB[i[j]]:	
			rawDB[i[j]][i[j+1]] = 0	
		rawDB[i[j]][i[j+1]] = rawDB[i[j]][i[j+1]] + 1

for i in rawDB:
	count = 0
	for j in rawDB[i]:
		count += rawDB[i][j]
	tag_count[i] = count
		
for i in rawDB:
	for j in rawDB[i]:
		rawDB[i][j] = float(rawDB[i][j])/tag_count[i]
		# print transition parameters to console
		# print i, "->", j, "==", rawDB[i][j]

#
#
#	End of Question 1
#
# # # # #



# # # # #
#
#	Start of Question 2
#
#

# use logarithm of probabilities instead of just probabilities otherwise it may be too small to be represented aka underflow


# create anther copy for transition matrix
transition = rawDB

# prepare emission attributes
# Read data from file and sort into tags
rawDB = {}
counter = {}
wordList = []

with open("Project Data/train", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
		# convert to uppercase
		row[0] = row[0].upper()
		# convert "@USER.." to "@USER"
		if row[0].startswith("@USER"):
			row[0] = "@USER"
		# convert number to 0
		if row[0].isdigit():
			row[0] = "0"
		# convert "http://..." to "http"
		if row[0].startswith("HTTP://"):
			row[0] = "HTTP"
		# record words appeared
		if row[0] not in wordList:
			wordList.append(row[0])	
		# tag not found in dictionary (unlikely)
		if row[1] not in rawDB:
			# initialize counter for tag
			counter[row[1]] = 0
			# create tag in dictionary
			rawDB[row[1]] = {}
		# else tag found in dictionary (most likely)
		# increment the counter for tag
		counter[row[1]] = counter[row[1]] + 1
		# word not found in tag dictionary
		if row[0] not in rawDB[row[1]]:
			# create word and set count to 1
			rawDB[row[1]][row[0]] = 1
		# word found in tag dictionary
		else:
			# increase word count
			rawDB[row[1]][row[0]] = rawDB[row[1]][row[0]] + 1


# assign 0 emission rate to known words not appeared in some tags
for tag in rawDB:
	for w in wordList:
		if w not in rawDB[tag]:
			rawDB[tag][w] = 0


# Create another copy for emission matrix
emission = rawDB

# # Calculate emission probability
# for i in emission:
# 	for j in emission[i]:
# 		emission[i][j] /= float(counter[i]+1)

# Prepare input for decoding
text = []
subtext = []
output = []
newWord = []

with open("Project Data/test.in", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# take empty line as start of a new sentence
		if row == []:
			text.append(subtext)
			subtext = []
		else:
			# convert row[0] to uppercase
			row[0] = row[0].upper()
			# convert "@USER.." to "@USER"
			if row[0].startswith("@USER"):
				row[0] = "@USER"
			# convert number to 0
			if row[0].isdigit():
				row[0] = "0"
			# convert "http://..." to "http"
			if row[0].startswith("HTTP://"):
				row[0] = "HTTP"
			# prepare list of distinct new words for emission update
			if row[0] not in wordList and row[0] not in newWord:
				newWord.append(row[0])
			subtext.append(row[0])


# update emission parameters based on test input
for tag in emission:
	for old_w in emission[tag]:
		emission[tag][old_w] /= float(counter[tag]+len(newWord))
	for w in newWord:
		# if w not in emission[tag]:
		emission[tag][w] = 1 / float(counter[tag]+len(newWord))


# Start Viterbi
for subtext in text:
	# initialize alpha (or pi)
	# alpha_old -> alpha values for t-1
	# alpha_new -> alpha values for t
	alpha_old = {}
	alpha_old["*"] = 0
	seq = []
	# penalty for missing transition or emission
	penalty = -100

	# i -> word
	# k -> tag for t
	# j -> tag for t-1
	for i in subtext:
		alpha_new = {}
		subseq = []

		for k in emission.keys():
			argmax = ''
			# initialize to negative infinity
			maxprob = -99999999999

			if emission[k][i] == 0:
				e = penalty
			else:
				e = math.log(emission[k][i])

			for j in alpha_old:
				# if j->k in the transition database
				if k in transition[j]:
					alpha = alpha_old[j] + math.log(transition[j][k]) + e
				# penalize
				else:
					alpha = alpha_old[j] + penalty + e
				if alpha > maxprob:
					maxprob = alpha
					argmax = j
			alpha_new[k] = maxprob
			subseq.append((argmax, k, maxprob))		
		
		seq.append(subseq)
		alpha_old = alpha_new

	# handle stop
	subseq = []	
	maxprob = -99999999999
	argmax = ''
	for j in alpha_old.keys():
		if "STOP" in transition[j]:
			alpha = alpha_old[j] + math.log(transition[j]["STOP"])
		else:
			alpha = alpha_old[j] + penalty
		if alpha > maxprob:
			maxprob = alpha
			argmax = j
	subseq.append((argmax, "STOP", maxprob))	
	seq.append(subseq)

	# decode
	path = ["STOP"]
	while seq:
		for i in seq[-1]:
			# i => [last tag, current tag, prob at current tag]
			if i[1] == path[0]:
				path.insert(0, i[0])
				seq = seq[:-1]
				break			

	# store to output 
	# eliminate "*" and "STOP" for each path
	output.append((subtext, path[1:-1])) 


f = open("Project Data/test.out", "w")
# write to dev.p2.out
for i in output:
	temp = [a+"\t"+b+"\n" for a,b in zip(i[0], i[1])]
	for k in temp:
		f.write(k)
	f.write("\n")
f.close()

print "Task complete"

#
#
#	End of Question 2
#
# # # # #