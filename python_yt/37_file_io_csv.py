import csv

batemps = open('bayareatemps.csv', 'r',)
bareader = csv.DictReader(batemps)
print(type(bareader))
for row in bareader:
    print(row)

import json

jsontemps = open('jsontemps.json', 'w')
batemps.seek(0) 
reader = csv.DictReader(batemps)
output = json.dumps([row for row in reader])
jsontemps.write(output)
jsontemps.close()
batemps.close()
exit()