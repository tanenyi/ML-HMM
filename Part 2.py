# # # # #
#
#	Start of Setup
#
#

import csv

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
			rawDB[i[j]][i[j+1]] = 1
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

text = []

with open("Project Data/dev.in", "rb") as csvfile:
	rd = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	for row in rd:
		# ignore empty line
		if row == []:
			continue
		else:
			text.append(row[0])



#
#
#	End of Question 2
#
# # # # #