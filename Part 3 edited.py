# # # # #
#
#	Start of Setup
#
#

import csv
import math

emoticons = [";)",":p",":-)","xd",";-)",";d","(;",":3",";p","=p",":-p","=))",";]","xdd","#gno","xddd",">:)",";-p",">:d","8-)",";-d",":)","(:","=)",":))",":]","=]","^_^",":)))","^.^","[:",";))","((:","^__^","(=","^-^",":))))",":(",":/","-_-","-.-",":-(","d:",":|",":s","-__-","=(","=/",">.<","-___-",":-/","</3",":\\","-____-",";(","/:",":((",">_<","=[",":[","#fml","<3","xoxo","<33","xo","<333","#love","<3333"]

companies = ['Ford Motor', 'JetBlue Airways', 'Bank of America', 'Northwestern Mutual', 'General Dynamics', 'eBay', 'Target', 'Abbott Laboratories', 'Avaya', 'EMC', 'Dr Pepper Snapple Group', 'Oracle', 'American International Group', 'Cigna', 'McGraw-Hill Companies', 'DaVita', 'Hewlett-Packard', 'Verizon Communications', 'Procter & Gamble Co.', 'United Parcel Service, Inc.', 'Halliburton', 'Express Scripts Holding', 'WellPoint', 'Advanced Micro Devices', 'Staples', 'Microsoft', 'Pfizer', 'Waste Management', 'Pitney Bowes', 'Emerson Electric', 'U.S. Bancorp', 'MetLife', 'Computer Sciences Corporation', 'PepsiCo', 'AT&T Mobility', 'Celgene Corporation', 'ARAMARK Corporation', 'International Business Machines', 'Level 3 Communications', 'Johnson Controls Inc', 'Gilead Sciences', 'Starbucks', 'Starwood Hotels & Resorts', 'Cisco Systems', 'Marriott International', 'Apple', 'AMR', 'Paccar', 'Amgen', 'Fifth Third Bancorp', 'General Electric', 'Home Depot', 'Citi', 'Bristol-Myers Squibb', 'McKesson', 'Cognizant Technology Solutions', 'Boeing', 'Sprint Nextel', 'Insight Enterprises', 'NetApp', 'Symantec', 'J P Morgan Chase & Co', 'Thermo Fisher Scientific', 'Texas Instruments Incorporated', 'SLM', 'UnitedHealth Group', 'PPG Industries', 'Henry Schein, Inc.', 'Avery Dennison', 'Fannie Mae', 'Marsh & McLennan Companies', 'Harley-Davidson', 'Booz Allen Hamilton', 'Automatic Data Processing', 'Bank of New York Mellon Corp', 'Massachusetts Mutual Life Insurance', 'American Express', 'MasterCard', 'Caterpillar', 'Southwest Airlines Co', 'Micron Technology', 'The Hartford Insurance Company', 'Walgreens Distribution Center', 'Xerox', 'BiogenIdec', "Lowe's", 'TIAA-CREF', '3M Company', 'Johnson & Johnson', 'Monsanto Company', 'Walt Disney', 'DIRECTV', 'Dow Chemical', 'Lockheed Martin', 'News Corp.', 'Harris', 'New York Life Insurance', 'Baxter International', 'Capital One', 'General Motors', 'Parker-Hannifin Corporation', 'Guardian Life Insurance Co', 'Honeywell International', 'Northrop Grumman Corporation', 'Dell', 'PNC Financial Services Group', 'Yahoo!', 'Allstate', 'Merck & Co.', 'Frontier Communications', 'Whirlpool', 'Cardinal Health', 'Eli Lilly', 'Tech Data', 'Intel', 'St. Jude Medical, Inc.', 'Agilent Technologies', 'Hertz Global Holdings', 'Exxon Mobil', 'Qualcomm', 'The J. M. Smucker Company', 'NRG Energy', 'Nationwide', 'Boston Scientific Corporation', 'Cummins', 'FirstEnergy', 'Xcel Energy', 'Wells Fargo', 'Medtronic Inc', 'Armour-Eckrich Meats', 'National Oilwell Varco', 'WESCO International', 'AmerisourceBergen', 'Costco Wholesale', 'Rockwell Automation, Inc', 'Ecolab Inc.', 'Entergy', 'Enbridge Energy Partners, L.P.', 'Valero Corp', 'Kimberly-Clark', 'Alcoa', 'Sempra Energy', 'Brita Water Co', 'W.W. Grainger Inc', 'Allergan', 'Energy Future Holdings', 'Applied Materials, Inc.', 'FMC Technologies Inc', 'CA', 'General Mills', 'SAIC', 'Avnet, Inc.', 'PMI Mortgage Insurance Co.', 'Owens Corning', 'Cameron International', 'International Paper', 'Sysco', 'The H.J. Heinz Company', 'Textron', 'Campbell Soup', 'Newell Rubbermaid', 'Sealed Air', 'Mosaic Company', 'Consolidation Coal Co', 'OfficeMax', 'Coca-Cola Enterprises', 'Becton Dickinson', 'Dole Food', 'Raytheon', 'Motorola Solutions', 'CenterPoint Energy', 'Celanese', 'Air Products & Chemicals', 'Public Service Enterprise Group', 'Chevron', 'Eastman Chemical', 'Peter Kiewit Sons', 'Ingram Micro', 'Kellogg', 'Graybar Electric', 'SanDisk', 'HD Supply', 'Estee Lauder Companies, Inc.', 'Goodyear Tire & Rubber', 'First Data', 'Fidelity National Financial', 'Illinois Tool Works', 'priceline.com Incorporated', 'Walmart', 'Phillips 66', 'Berkshire Hathaway', 'CVS Caremark', 'Kroger Co.', 'Archer Daniels Midland', 'Prudential Financial', 'Freddie Mac', 'Marathon Petroleum', 'INTL FCStone', 'State Farm Insurance', 'ConocoPhillips', 'Comcast', 'Amazon.com', 'United Technologies', 'Google', 'Coca-Cola', 'Best Buy', 'Safeway', 'FedEx', 'Enterprise Products Partners', 'Goldman Sachs Group', 'CHS', 'Sears Holdings Corporation', 'DuPont', 'Humana Inc.', 'World Fuel Services', 'Hess Corporation', 'Plains All American Pipeline', 'United Continental Holdings', 'Liberty Mutual Insurance Group', 'HCA Holdings', 'Delta Air Lines', 'Aetna', 'Deere', 'Supervalu', 'Mondelez International', 'Tyson Foods', 'Tesoro', 'Morgan Stanley', 'Murphy Oil USA Refinery', 'Time Warner Inc.', 'Publix Super Markets', 'Macys Merchandising Group', 'Fluor', 'McDonalds Corporation', 'Rite Aid', 'The TJX Companies, Inc.', 'Travelers', 'Aflac', 'Occidental Petroleum', 'Nike', 'Exelon', 'Time Warner Cable', 'Baker Hughes', 'Union Pacific', 'USAA', 'ManpowerGroup', 'Arrow Electronics', 'PBF Energy', 'HollyFrontier', 'Duke Energy', 'Nucor Corporation', 'United States Steel', "Kohl's", 'CenturyLink', 'Kraft Foods Group', 'Danaher', 'AES', 'Phelps Dodge Sierrita Corp', 'Global Companies LLC', 'Altria Group', 'Energy Transfer Equity', 'Jabil Circuit, Inc.', 'Colgate-Palmolive', 'Progressive', 'Apache', 'Southern', 'TRW Automotive', 'Marathon Oil', 'Dollar General', 'AutoNation', 'Icahn Enterprises', 'Gap', 'PG&E Corporation', 'Community Health Systems Inc.', 'American Electric Power', 'Cbs', 'Lear', 'Loews', 'DISH Network', 'NextEra Energy', 'Omnicom Group', 'Land O Lakes, Inc.', 'Coventry Health Care', 'L-3 Communications', 'Viacom', 'US Airways Group', 'Yum Brands', 'Chubb', 'Penske Automotive Group', 'Toys R" Us"', 'Anadarko Petroleum', 'Dominion Hope', 'Edison International', 'Smithfield Foods, Inc.', 'Genuine Parts Co', 'J.C. Penney', 'Navistar International Corporation', 'Dean Foods Company', 'ONEOK Energy Services Company, L.P.', 'Ally Financial', 'Western Digital', 'Chesapeake Energy', 'PPL', 'Consolidated Edison', 'Nordstrom Prosthesis Program', 'Csx Corporation', 'Whole Foods Market Incorporated', 'EOG Resources', 'Lincoln Financial Group', 'Health Net', 'C.H. Robinson Worldwide Inc', 'SunTrust Banks', 'Huntsman Petrochemical Corp', 'Praxair Inc', 'Las Vegas Sands Corp.', 'Stanley Black & Decker, Inc.', 'Conrail', 'URS', 'Jacobs Engineering Group Inc', 'VF Imagewear', 'Branch Banking & Trust (BB&T)', 'Avon Products', 'Office Depot', 'Liberty Global', 'Unum Group', 'L Brands', 'CarMax', 'Visa', 'Synnex', 'Ameriprise Financial Inc.', 'R.R. Donnelley & Sons', 'Kinder Morgan', 'CDW', 'State Street Corp.', 'Tenet Healthcare Corporation', 'Liberty Interactive', 'Genworth Financial, Inc.', 'AGCO', 'Newmont Mining Corporation', 'Reinsurance Group of America', 'KKR', 'Ross Stores Distribution Center', 'Sherwin-Williams', 'Western Refining', 'Devon Energy Corporation', 'Bed Bath & Beyond', 'BlackRock', 'Family Dollar Stores', 'Hillshire Brands', 'Leucadia National Corp.', 'Principal Financial', 'Rock-Tenn Company', 'MGM Resorts International', 'Discover Financial Services', 'Owens & Minor', 'GameStop Corp.', 'DTE Energy Co.', 'Caesars Entertainment', 'Ball', 'Centene Corporation', 'Stryker', 'Autozone, Inc.', 'Sonic Automotive', 'Dover Corporation', 'Assurant', 'Crown Holdings', 'Reliance Steel', 'Peabody Energy', 'Reynolds American', 'Autoliv', 'Hormel Foods', 'AECOM Technology', 'Ashland', 'Oshkosh', 'Republic Services', 'Thrivent Financial for Lutherans', 'Corning', 'Broadcom', 'Darden Restaurants', 'TravelCenters of America LLC', 'Spectrum Group International', 'KBR', 'Commercial Metals', 'Masco', 'Universal Health Services', 'Charter Communications', 'QuestDiagnostics', 'Williams', 'Group 1 Automotive', 'WellCare Health Plans', 'Dollar Tree Distribution Center', 'Pantry', 'Tenneco', 'Avis Budget Group', 'Terex', 'Steel Dynamics Inc', 'Precision Castparts Corp', 'Dana Holding', 'BorgWarner Inc.', 'Visteon', 'BARNES & NOBLE INC', 'Franklin Resources', 'Weyerhaeuser', 'Owens-Illinois', 'Alpha Natural Resources', 'Interpublic Group of Companies, Inc.', 'Core-Mark Holding', 'Pacific Life', 'Ralph Lauren', 'Ameren Corporation', 'Mylan', 'Health Management Associates', 'PetSmart, Inc.', "Dillard's", 'Huntington Ingalls Industries', 'Cablevision Systems', 'Jarden', 'Hershey', 'Ingredion', 'CBRE Group', 'UGI', 'NuStar Energy', 'Vanguard Health Systems', "Casey's General Stores", 'American Family Insurance Group', 'Mutual of Omaha Insurance', 'Mattel', 'Quanta Services', 'EMCOR Group', 'Regions Financial', 'Northeast Utilities', 'Ryder System', 'Anixter International', 'CMS Energy', 'CC Media Holdings', 'Advance Auto Parts', 'Kindred Healthcare', 'Seaboard Corporation', 'OReilly Ozark Automotive, Inc.', 'Foot Locker Warehouse', 'Windstream', 'CH2M Hill', 'Omnicare', 'CF Industries Holdings', 'Sanmina', 'NII Holdings', 'PVH', 'Molina Healthcare', 'Cliffs Natural Resources', 'General Cable', 'Shaw Group', 'Expeditors International of Washington', 'Ak Steel Holding Corporation', 'SPX', 'Actavis', 'FIS Global', 'Targa Resources', "Dick's Sporting Goods", 'W.R. Berkley', 'Live Nation Entertainment', 'NCR', 'Mohawk Industries', 'Auto-Owners Insurance Group', 'Laboratory Corp. of America', 'Western Union', 'Joy Global', 'MeadWestvaco', 'Con-way', 'MRC Global', 'Exelis', 'Erie Insurance Group', 'Domtar', 'Calpine', 'Susser Holdings', 'Kelly Services', 'Big Lots', 'Gannett', 'Telephone & Data Systems', 'Host Hotels & Resorts', 'Western & Southern Financial Group', 'Andersons', 'United Natural Foods Inc.', 'Spectra Energy Corp.', 'Wynn Resorts', 'Bemis Company, Inc', 'NiSource', 'MetroPCS Communications', 'Facebook', 'Pepco Holdings', 'United Stationers', 'American Financial Group, Inc.', 'J. B. Hunt Transport Services', 'Charles Schwab', 'Allegheny Technologies', 'Jones Financial', 'Latrobe Steel Distributors', 'Old Republic International Corporation', 'Simon Property Group, Inc', 'YRC Worldwide', 'Nash-Finch']
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
		if row[0] in emoticons:
			row[0] = "emoticons"
		# if row[0] in companies:
		# 	row[0] = "companies"
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

with open("Project Data/dev.in", "rb") as csvfile:
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
			if row[0] in emoticons:
				row[0] = "emoticons"
			# if row[0] in companies:
			# 	row[0] = "companies"
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


f = open("Project Data/dev.p3.out", "w")
# write to dev.p2.out
for i in output:
	temp = [a+"\t"+b+"\n" for a,b in zip(i[0], i[1])]
	for k in temp:
		f.write(k)
	f.write("\n")
f.close()

tag = []
with open("Project Data/dev.p3.out", "rb") as csvfile:
	tag_f = csv.reader(csvfile, delimiter = "\t", quotechar = None, skipinitialspace = True)
	j = 0
	for i in tag_f:
		if not i:
			continue
		else:
			tag.append(i)
			

match_count = 0
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
			if tag[i][1] == row[1]:
				# increment match counter
				match_count += 1
			# increment index counter
			i += 1

# print accuracy against all words
print "General Accuracy:", float(match_count)/len(tag)*100, "%"
# General Accuracy: 80.8944543828 %



#
#
#	End of Question 2
#
# # # # #