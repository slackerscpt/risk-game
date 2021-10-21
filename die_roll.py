from die import Die

f = open("rolledDies-20-sided.txt", "a")

current_die = Die(20)
for numbers in range(1,1000001):
    f.write(str(current_die.roll()))
    f.write("\n")

f.close()