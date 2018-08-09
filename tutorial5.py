from random import randint

# Open a file for writing. If it exists the content will be overwritten
file = open("integers.txt","w")

for integer in range(500):
    file.write(str(randint(1,1000))+"\n")

file.close()

# Open file for reading and sum integers
file = open("integers.txt","r")

total = 0
for line in file:
    total += int(line.strip())

print(total)

