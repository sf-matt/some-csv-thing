import csv, json
import config

dataArray = []
csvFile = open(config.csvFile, encoding = 'utf-8')
jsonFile = open(config.jsonArrayFile, 'w', encoding = 'utf-8')


reader = csv.DictReader(csvFile)
for row in reader:
    dataArray.append(row)

jsonFile.write(json.dumps(dataArray, indent = 4))