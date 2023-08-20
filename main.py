#from inspect import signature
import itertools
import functools
import operator
def b_6(x, y):
        if (x == y): return x
        if (x == 0 and y == 1): return 1
        if (x == 1 and y == 0): return 1
        if (x == 0 and y == 2): return 0
        if (x == 2 and y == 0): return 2
        if (x == 1 and y == 2): return 1
        if (x == 2 and y == 1): return 2
        else: return 0
def b_5(x, y):
    if (x == y): return x
    if (x == 0 and y == 1): return 1
    if (x == 1 and y == 0): return 1
    if (x == 0 and y == 2): return 0
    if (x == 2 and y == 0): return 0
    if (x == 1 and y == 2): return 1
    if (x == 2 and y == 1): return 2
    else: return 0
with open('data.txt', 'r') as input:
    data = input.readlines()
    #data = list(data)
    #data=data.split
    #del data[-1]
#print(data)
data2=[]
for str in data:
    #str.split()
    data2.append(tuple([int(i) for i in str.split()]))
#print(data2)
data = data2
data = set(data)
#print(data)
#for tup in data:
#    print(tup)
while True:
    n = len(data)
    x = itertools.product(data, repeat=2)
    data2 = set(map(lambda y: tuple(b_5(*a) for a in zip(*y)), x))
    data = data.union(data2)
    #for tup in data:
    #    print(tup)
    #print()
    if len(data) == n:
        break
#print((1,0,0) in data)
#print((1,0,0,0,0) in data)
#print((1,0,0,0,2) in data)
#print((1,1,1,0,0) in data)
#print(len(data))

# output = open("dataout.txt", "w")
for tup in data:
    if tup[4]==2 and tup[3]==0 and tup[2]==1: print(tup[0],tup[1],sep=' ',end='\n')
    #str = functools.reduce(operator.add, (tup))
    #output.write(str)
# output.close()
# input.close()
#print(len(signature(b_6).parameters))
#with open('data.txt', 'w') vvas f: