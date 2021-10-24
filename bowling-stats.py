import csv
import statistics

games = []
with open('csvData\\Tuesday-2019-Stats.csv', newline='',encoding = 'utf-8-sig' ) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['first_name'], row['last_name'])
        print(row['Week'],row['Gm1'], row['Gm2'], row['Gm3'], row['SS'])
        if (int(row['SS']) > 0):
            games.append(int(row['Gm1']))
            games.append(int(row['Gm2']))
            games.append(int(row['Gm3']))
        

csvfile.close()
games.sort()
print (games)
print (sum(games))
print (len(games))
print (sum(games)/len(games))
print (statistics.median(games))
print (statistics.mean(games))
