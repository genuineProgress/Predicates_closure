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
def f_3(x_0,x_1,x_2,x_3):
    n = 0
    m = 0
    if x_0==1: return 1
    elif x_0==2:
        if(x_1==0 or x_2==0 or x_3==0): return 0
        else: return 2
    elif x_0 == 0:
        if (x_1 == 1): n += 1
        if (x_2 == 1): n += 1
        if (x_3 == 1): n += 1
        if (x_1 == 2): m += 1
        if (x_2 == 2): m += 1
        if (x_3 == 2): m += 1
        if (n == 0):
            return 0
        elif (n == 1 and m == 2):
            return 0
        else:
            return 1
def f_4(x_0,x_1,x_2,x_3,x_4):
    n = 0
    m = 0
    if x_0==1: return 1
    elif x_0==2:
        if(x_1==0 or x_2==0 or x_3==0 or x_4==0): return 0
        else: return 2
    elif x_0 == 0:
        if (x_1 == 1): n += 1
        if (x_2 == 1): n += 1
        if (x_3 == 1): n += 1
        if (x_4 == 1): n += 1
        if (x_1 == 2): m += 1
        if (x_2 == 2): m += 1
        if (x_3 == 2): m += 1
        if (x_4 == 2): m += 1
        if (n == 0):
            return 0
        elif (n == 1 and m == 3):
            return 0
        else:
            return 1
def f_5(x_0,x_1,x_2,x_3,x_4,x_5):
    n=0
    m=0
    if x_0==1: return 1
    elif x_0==2:
        if(x_1==0 or x_2==0 or x_3==0 or x_4==0 or x_5==0): return 0
        else: return 2
    elif x_0==0:
        if(x_1==1): n+=1
        if(x_2==1): n+=1
        if (x_3 == 1): n += 1
        if (x_4 == 1): n += 1
        if (x_5 == 1): n += 1
        if (x_1 ==2): m += 1
        if (x_2 ==2): m += 1
        if (x_3 ==2): m += 1
        if (x_4 ==2): m += 1
        if (x_5 ==2): m += 1
        if(n==0): return 0
        elif(n==1 and m==4): return 0
        else: return 1

def check_fs(data): #return 0 if check is not successful and 1 otherwise
    #here we check f_3
    check_f_3=1
    for list in data:
        set_list=set(list)
        n = len(list)
        x = itertools.product(set_list, repeat=4)
        set_list2 = set(map(lambda y: tuple(f_3(*a) for a in zip(*y)), x))
        set_list = set_list.union(set_list2)
        # for tup in data:
        #    print(tup)
        # print()
        if len(set_list) != n:
            check_f_3=0
            print(list)
    #if(check_f_3==0): return 0
    #here we check f_4
    check_f_4=1
    for list in data:
        set_list=set(list)
        n = len(list)
        x = itertools.product(set_list, repeat=4)
        set_list2 = set(map(lambda y: tuple(f_3(*a) for a in zip(*y)), x))
        set_list = set_list.union(set_list2)
        # for tup in data:
        #    print(tup)
        # print()
        if len(set_list) != n:
            check_f_4=0
            print(list)
    #if(check_f_4==0): return 0
    #here we check f_5
    check_f_5=1
    for list in data:
        set_list=set(list)
        n = len(list)
        x = itertools.product(set_list, repeat=4)
        set_list2 = set(map(lambda y: tuple(f_3(*a) for a in zip(*y)), x))
        set_list = set_list.union(set_list2)
        # for tup in data:
        #    print(tup)
        # print()
        if len(set_list) != n:
            check_f_5=0
            print(list)
    #if(check_f_5==0): return 0
    if(check_f_3==0 or check_f_4==0 or check_f_5==0): return 0
    else: return 1



with open('data.txt', 'r') as input:
    data = input.readlines()
    #data = list(data)
    #data=data.split
    #del data[-1]
#print(data)
data2=[[]]
i=-1
for str in data:
    #str.split()
    #print(len(str))
    if(len(str)==1):
        i+=1
        data2.append([])
        #print(2)
    else:data2[i].append(tuple([int(i) for i in str.split()]))
#print(data2)

data = data2
zero_one={0,1}
zero_one_two={0,1,2}
interim_values_of_f=itertools.product(zero_one,repeat=12)
interim_2_values_of_f=itertools.product(zero_one_two,repeat=12)
values_of_f=set(i+j for i,j in itertools.product(interim_values_of_f,interim_2_values_of_f))
print(len(values_of_f))
def adder(x):
   def inner(y):
      return x + y
   return inner

add_one = adder(1)
print(add_one(5))
print(check_fs(data))


