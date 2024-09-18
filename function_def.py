import itertools
def b_9(x,y):
    if(x!=2 or y!=0): return x
    else: return 1
def b_10(x,y):
    if(x==0 and y==2): return 1
    elif (x==1 and y==2): return 0
    else: return x
def b_6(x, y):
    if (x == y): return x
    if (x == 0 and y == 1): return 1
    if (x == 1 and y == 0): return 1
    if (x == 0 and y == 2): return 0
    if (x == 2 and y == 0): return 2
    if (x == 1 and y == 2): return 1
    if (x == 2 and y == 1):
        return 2
    else:
        return 0
def b_5(x, y):
    if (x == y): return x
    if (x == 0 and y == 1): return 1
    if (x == 1 and y == 0): return 1
    if (x == 0 and y == 2): return 0
    if (x == 2 and y == 0): return 0
    if (x == 1 and y == 2): return 1
    if (x == 2 and y == 1):
        return 2
    else:
        return 0


def f_3(x_0, x_1, x_2, x_3):
    number_of_zeros = 0
    number_of_ones = 0
    number_of_twos = 0
    if x_0 == 1:
        return 1
    if (x_1 == 0): number_of_zeros += 1
    if (x_2 == 0): number_of_zeros += 1
    if (x_3 == 0): number_of_zeros += 1
    if (x_1 == 1): number_of_ones += 1
    if (x_2 == 1): number_of_ones += 1
    if (x_3 == 1): number_of_ones += 1
    if (x_1 == 2): number_of_twos += 1
    if (x_2 == 2): number_of_twos += 1
    if (x_3 == 2): number_of_twos += 1
    if x_0 == 2:
        if (number_of_ones >= 1):
            return 2
        elif (number_of_zeros >= 1):
            return 0
        else:
            return 2

    elif x_0 == 0:
        if (number_of_ones <= 1 and number_of_zeros == 0): return 0
        if (number_of_ones == 0): return 0
        if (number_of_ones >= 1 and number_of_twos == 0): return 1
        return 1


def f_4(x_0, x_1, x_2, x_3, x_4):
    number_of_zeros = 0
    number_of_ones = 0
    number_of_twos = 0
    if x_0 == 1:
        return 1
    if (x_1 == 0): number_of_zeros += 1
    if (x_2 == 0): number_of_zeros += 1
    if (x_3 == 0): number_of_zeros += 1
    if (x_4 == 0): number_of_zeros += 1
    if (x_1 == 1): number_of_ones += 1
    if (x_2 == 1): number_of_ones += 1
    if (x_3 == 1): number_of_ones += 1
    if (x_4 == 1): number_of_ones += 1
    if (x_1 == 2): number_of_twos += 1
    if (x_2 == 2): number_of_twos += 1
    if (x_3 == 2): number_of_twos += 1
    if (x_4 == 2): number_of_twos += 1

    if x_0 == 2:
        if (number_of_ones >= 1):
            return 2
        if (number_of_zeros == 0):
            return 2
        else:
            return 0

    if x_0 == 0:
        if (number_of_ones == 0): return 0
        if (number_of_ones == 1 and number_of_zeros == 0): return 0
        return 1

def f_5(x_0, x_1, x_2, x_3, x_4, x_5):
    number_of_zeros = 0
    number_of_ones = 0
    number_of_twos = 0
    if x_0 == 1:
        return 1
    if (x_1 == 0): number_of_zeros += 1
    if (x_2 == 0): number_of_zeros += 1
    if (x_3 == 0): number_of_zeros += 1
    if (x_4 == 0): number_of_zeros += 1
    if (x_5 == 0): number_of_zeros += 1
    if (x_1 == 1): number_of_ones += 1
    if (x_2 == 1): number_of_ones += 1
    if (x_3 == 1): number_of_ones += 1
    if (x_4 == 1): number_of_ones += 1
    if (x_5 == 1): number_of_ones += 1
    if (x_1 == 2): number_of_twos += 1
    if (x_2 == 2): number_of_twos += 1
    if (x_3 == 2): number_of_twos += 1
    if (x_4 == 2): number_of_twos += 1
    if (x_5 == 2): number_of_twos += 1

    if x_0 == 2:
        if(number_of_ones>=1):
            return 2
        elif(number_of_zeros>=1):
            return 0
        else: return 2

    if x_0 == 0:
        if (number_of_ones <= 1 and number_of_zeros == 0): return 0
        if (number_of_ones == 0): return 0
        return 1
def s_2(x_0,x_1,x_2):
    if(x_0==0): return x_0
    if(x_0==1): return x_0
    if(x_0==2):
        if(x_0!=x_1 and x_1!=x_2 and x_0!=x_2): return 1
        else: return 2
def s_3(x_0,x_1,x_2):
    if(x_0==0): return x_0
    if(x_0==1): return x_0
    if(x_0==2):
        if(x_0!=x_1 and x_1!=x_2 and x_0!=x_2): return x_1
        else: return 2
def s_4(x_0,x_1,x_2):
    if(x_0==2): return x_0
    if(x_0!=x_1 and x_1!=x_2 and x_0!=x_2): return (1-x_0)
    return x_0
def s_5(x_0,x_1,x_2):
    if(x_0!=x_1 and x_1!=x_2 and x_0!=x_2): return x_1
    return x_0
def check_s_2_out_tup(tup:tuple)->int:
    if (tup[5]==2 and tup[6]==1 and tup[7]==2): return 0
    if (tup[5] == 1 and tup[6] == 2 and tup[9] == 2): return 0
    if (tup[4] == 2 and tup[3] == 1 and tup[8] == 2): return 0
    if (tup[3] == 2 and tup[4] == 1 and tup[7] == 2): return 0
    if (tup[2] == 2 and tup[1] == 1 and tup[9] == 2): return 0
    if (tup[1] == 2 and tup[2] == 1 and tup[8] == 2): return 0
    if (tup[1] == 1 and tup[2] == 1 and  tup[8] == 2  and tup[9] == 2): return 0
    if (tup[3] == 1 and tup[4] == 1 and  tup[7] == 2  and tup[8] == 2): return 0
    if (tup[5] == 1 and tup[6] == 1 and  tup[7] == 2  and tup[9] == 2): return 0
    return 1
def seek_tuple(seek_tup,data_init,step)->str:
    print(seek_tup)
    iteration = 0
    data = set(data_init)
    while step==-1 or iteration<=step:
        #print(data)
        #print(1)
        iteration=iteration+1
        n = len(data)
        print(step,iteration,n,data)
        x = itertools.product(data, repeat=2)
        data2 = set(map(lambda y: tuple(b_5(*a) for a in zip(*y)), x))
        data = data.union(data2)
        if(seek_tup in data):
            if(step==-1): step=iteration+1
            z = itertools.product(data, repeat=2)
            for tuple_iter in z:
                #print(tuple1[0])
                tuple_comp = lambda tuple_var: tuple(b_5(*a) for a in zip(*tuple_var))
                # print(tuple2(tuple1))
                tuple1=[tup for tup in tuple_iter]
                tuple2=tuple_comp(tuple_iter)
                # if (tuple2==seek_tup) and (tuple2 in tuple1) == 1:
                #     print("degenerate")
                #     print(tuple1[0], tuple1[1], seek_tup)
                #     return seek_tuple(seek_tup,data_init,step-1)
                if (tuple2==seek_tup) and (tuple2 in tuple1) == 0:
                    print("nondegenerate")
                    print(tuple1[0], tuple1[1], seek_tup)
                    if(tuple1[0] in data_init):
                        tuplefirst=str((data_init.index(tuple1[0])))
                        print(tuple1[0],"->",data_init.index(tuple1[0]))
                    else:
                        tuplefirst=seek_tuple(tuple1[0],data_init,step-1)
                    if (tuple1[1] in data_init):
                        print(tuple1[1],"->",data_init.index(tuple1[1]))
                        tuplesecond = str((data_init.index(tuple1[1])))
                    else:
                        tuplesecond = seek_tuple(tuple1[1], data_init, step - 1)

                    if(tuplefirst!="" and tuplesecond!=""): return "("+tuplefirst+','+tuplesecond+')'

                    # print(data)
        # below code fragment is used to show tuples from which a particular tuple may be derived

        if (len(data) == n): break
        n = len(data)
        #return -1
    return ""




