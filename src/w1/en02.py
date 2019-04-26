import random

def makelist(n):
    li = []
    for i in range(n):
        li.append(random.randint(1,100))
    return li

def bbSort(rawli):
    for i in range(len(rawli)):
        for j in range(len(rawli)-1, i, -1):
            if rawli[j] < rawli[j-1]:
                rawli[j], rawli[j-1] = rawli[j-1], rawli[j]

    return rawli

ranlis = makelist(10)
sortedlist = bbSort(ranlis)

print(sortedlist)