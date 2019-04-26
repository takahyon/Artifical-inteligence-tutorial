import random

def makelist(n):
    li = []
    for i in range(n):
        li.append(random.randint(1,100))
    return li

print(makelist(10))
