import csv
import json


f = open('C:/csv_project/bijnor_csv.csv', 'r')
reader = csv.DictReader(f)
out = json.dumps([row for row in reader])
print(out)
