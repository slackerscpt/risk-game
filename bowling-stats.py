game_file = open('csvData\\Tuesday-2018-Stats.csv', 'r')

#for contents in game_file:
#    print (contents)


print ("--LINE 1--")
line1 = game_file.readline()
print (line1)
print ("--END--")

for contents in game_file:
    print (contents)
game_file.close()




import csv
with open('csvData\\Tuesday-2018-Stats.csv', newline='',encoding = 'utf-8-sig' ) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['first_name'], row['last_name'])
        print(row['Week'],row['Gm1'], row['Gm2'], row['Gm3'], row['SS'])