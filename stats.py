die_stats = open('rolledDies-20-sided.txt', 'r')


counter = {}
overall = 0
for numbers in die_stats:
    int_number = int(numbers)
    overall += 1
    if (int_number in counter):
        counter[int_number] += 1
    else:
        counter[int_number] = 1


print (counter)
print (overall)

for keys in counter:
    print ('The die came out with {} total times: {}'.format(keys,counter[keys]))
    print ('Percent showing up {}'.format((counter[keys]/overall)* 100))


