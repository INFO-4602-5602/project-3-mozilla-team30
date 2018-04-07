import csv

file_name = "20171013111831-SurveyExport.csv"
data = {}
rowNum = 0

countryCount =  {}

with open(file_name, 'rU') as file: 
	readCSV = csv.reader(file, delimiter=',')
	rowNumber = 0
	for row in readCSV:
		finalRow = []
		
		finalRow.append(row[5].replace(" ", "_"))
		if finalRow[0] == "":
			continue
		finalRow.append(row[7].replace(" ", "_").split(":")[0])
			
		if (finalRow[1] == ""):
			finalRow[1] = "Not_Really"

		str = finalRow[0] + "__" + finalRow[1]
		
		if str in data:
			num = int(data[str][2])
			finalRow.append(num+1)
		else :
			finalRow.append(1)

		num = 0
		if rowNumber > 0:
			if finalRow[0] in countryCount:
				num = int(countryCount[finalRow[0]])
				
			num += 1
			countryCount[finalRow[0]] = num

		data[str] = finalRow
		# print finalRow
		rowNumber += 1
		
	sorted(data, key=data.__getitem__)
	print data
	print countryCount

fileW = open("cleanedData.csv", "wb")
writer = csv.writer(fileW, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
for row in data:
	list = data[row]
	if list[0] in countryCount:
		list.append(countryCount[list[0]])
		list.append((list[2] * 100.0)/list[3])
	writer.writerow(list)

fileW.close()
file.close()