# # # # #
#
#	Start of Setup
#
#

import csv

# List / Dictionary Database
rawDB = {}

# Number counter for each tag
counter = {}

# List of distinct words
wordList = []

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

# Read data from file and sort into tags
with open("Project Data/train", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
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

# Read data from file and sort into tags
with open("Project Data/train", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
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

# Create another copy
emission = rawDB

text = []
tag  = []
match_count = 0
weighted_count = 0
newWord = []


with open("Project Data/dev.in", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
		else:
			text.append(row[0])
			# prepare list of distinct new words for emission update
			if row[0] not in wordList and row[0] not in newWord:
				newWord.append(row[0])

# update emission parameters based on test input
for t in emission:
	for old_w in emission[t]:
		emission[t][old_w] /= float(counter[t]+len(newWord))
	for w in newWord:
		# if w not in emission[t]:
		emission[t][w] = 1 / float(counter[t]+len(newWord))


#
#
#	End of Question 2
#
# # # # #



# # # # #
#
#	Start of Question 3
#
#


# # #
# greedy pocket algorithm
#

# iterate though list of new text
for i in text:
	# reset max probability of current text
	maxprob = 0
	# reset argument of max probability of current text
	argmax = ""
	# iterate through tags
	for j in emission.keys():
		# iterate through database text
		for k in emission[j].keys():
			# if database text is the same as current text
			if k == i:
				# if probability of database text is more than last stored value
				if emission[j][k] > maxprob:
					# set stored probability to new value
					maxprob = emission[j][k]
					# set stored argument to new value
					argmax = j
	# append particular tag
	tag.append(argmax)

#
#
# # #


with open("Project Data/dev.out", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	# set index counter
	i = 0
	for row in rd:
		# ignore empty line
		if row == []:
			continue
		else:
			# if predicted tag is the same as gold standard
			if tag[i] == row[1]:
				# increment match counter
				match_count += 1
			# increment index counter
			i += 1

# print accuracy against all words
print "General Accuracy:", float(match_count)/len(text)*100, "%"

# print accuracy against all known words
# print "Specific Accuracy:", float(match_count)/(len(text)-weighted_count)*100, "%"

f = open("Project Data/dev.pl.out", "w")
# write each row
for i in range(0, len(text)-1):
    	f.write(text[i]+"\t"+tag[i]+"\n")

#
#
#	End of Question 3
#
# # # # #