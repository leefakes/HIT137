import random

def Number_String(length=10):
    return ([str(random.randint(0,9)) for _ in range(length)])
a = Number_String(10)
b = Number_String(20)

print (a,"\n",b)

