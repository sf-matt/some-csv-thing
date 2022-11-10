import csv, json
import config

dataDic = {}
csvFile = open(config.csvFile, encoding = 'utf-8')
jsonFile = open (config.jsonDictFile, 'w', encoding = 'utf-8')


reader = csv.DictReader(csvFile)
for rows in reader:
    key = rows[config.dictKey]
    dataDic[key] = rows

jsonFile.write(json.dumps(dataDic, indent = 4))