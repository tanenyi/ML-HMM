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

print seqlist

#
#
#	End of Question 1
#
# # # # #