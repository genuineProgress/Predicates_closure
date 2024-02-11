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




