import csv

# List / Dictionary Database
rawDB = {}

# Number counter for each tag
counter = {}

# Start of Question 1
#
#

# Read data from file and sort into tags
with open("Project Data/train", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t")
	for row in rd:
		if row == []:
			continue
		elif row[1] not in rawDB:
			rawDB[row[1]] = {}
		elif row[1] in rawDB:
			if row[0] not in rawDB[row[1]]:
				rawDB[row[1]][row[0]] = 1
			else:
				rawDB[row[1]][row[0]] = rawDB[row[1]][row[0]] + 1

# Count per tag
for i in rawDB:
	for j in rawDB[i]:
		print "Tag:", i, " | Value:", j, " | Count:", rawDB[i][j]
		if i not in counter:
			counter[i] = 0
		counter[i] += rawDB[i][j]

# Create another copy
emission = rawDB

# Calculate emission probability
for i in emission:
	for j in emission[i]:
		emission[i][j] /= float(counter[i])
		print "Tag:", i, " | Value:", j, " | Count:", emission[i][j]

#
#
# End of Question 1

# Start of Question 2
#
#

# Read data from file and sort into tags
with open("Project Data/dev.in", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t")
	for row in rd:
		if row == []:
			continue
		elif row[1] not in rawDB:
			rawDB[row[1]] = {}
		elif row[1] in rawDB:
			if row[0] not in rawDB[row[1]]:
				rawDB[row[1]][row[0]] = 1
			else:
				rawDB[row[1]][row[0]] = rawDB[row[1]][row[0]] + 1

# Count per tag
for i in rawDB:
	for j in rawDB[i]:
		print "Tag:", i, " | Value:", j, " | Count:", rawDB[i][j]
		if i not in counter:
			counter[i] = 0
		counter[i] += rawDB[i][j]

# Create another copy
emission = rawDB

# Calculate emission probability
for i in emission:
	for j in emission[i]:
		emission[i][j] /= float(counter[i])
		print "Tag:", i, " | Value:", j, " | Count:", emission[i][j]

#
#
# End of Question 2