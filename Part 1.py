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
		# tag not found in dictionary
		elif row[1] not in rawDB:
			# initialize counter for tag
			counter[row[1]] = 0
			# create tag in dictionary
			rawDB[row[1]] = {}
		# tag found in dictionary
		elif row[1] in rawDB:
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

# Create another copy
emission = rawDB

# Calculate emission probability
for i in emission:
	for j in emission[i]:
		emission[i][j] /= float(counter[i])
		# print "Tag:", i, " | Value:", j, " | Count:", emission[i][j]

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
		# tag not found in dictionary (unlikely)
		elif row[1] not in rawDB:
			# initialize counter for tag
			counter[row[1]] = 0
			# create tag in dictionary
			rawDB[row[1]] = {}
		# tag found in dictionary (most likely)
		elif row[1] in rawDB:
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

# Create another copy
emission = rawDB

# Calculate emission probability
for i in emission:
	for j in emission[i]:
		emission[i][j] /= float(counter[i])
		# print "Tag:", i, " | Value:", j, " | Count:", emission[i][j]

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

text = []
tag  = []
match_count = 0
weighted_count = 0

with open("Project Data/dev.in", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
		else:
			text.append(row[0])

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
	# if no appropriate tags found
	if maxprob == 0:
		# append "unknown" tag
		tag.append("=")
		# increment counter for normalisation
		weighted_count += 1
	# if appropriate tags found
	else:
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
print "Specific Accuracy:", float(match_count)/(len(text)-weighted_count)*100, "%"

with open("Project Data/dev.pl.out", "w") as csvfile:
	# set csv format
    output = ['text', 'tag']
    writer = csv.DictWriter(csvfile, fieldnames = output, delimiter = "\t")
    writer.writeheader()
    # write each row
    for i in range(0, len(text)-1):
    	writer.writerow({'text': text[i], 'tag': tag[i]})

#
#
#	End of Question 3
#
# # # # #