import operators as o
def check1(data2)->list:
    data = []
    check_1=check_2=check_3=0
    final_check=0
    if (tup[0]==0 or tup[5]==0 or tup[10]==0): check_2=1
    if (tup[1] == 0 or tup[3] == 0 or tup[11]==0): check_3 = 1
    if (tup[2] == 0 or tup[4] == 0 or tup[9]==0): check_1 = 1
    if (tup[6]==0): check_2=check_3=1
    if (tup[7]==0): check_1=check_3=1
    if (tup[8]==0): check_2=check_1=1
    if (check_1==check_2==check_3==1): final_check=1
    if (tup[0]==0 and tup[1]==0): final_check=1
    if (tup[2]==0 and tup[3]==0): final_check=1
    if (tup[4]==0 and tup[5]==0): final_check=1

    if (tup[0] == 0 and (tup[3] != tup[6] or tup[6] != tup[11] or tup[11] != tup[3])): final_check = 1
    if (tup[1] == 0 and (tup[5] != tup[6] or tup[6] != tup[10] or tup[10] != tup[5])): final_check = 1
    if (tup[2] == 0 and (tup[1] != tup[7] or tup[7] != tup[11] or tup[11] != tup[1])): final_check = 1
    if (tup[3] == 0 and (tup[4] != tup[7] or tup[7] != tup[9] or tup[9] != tup[4])): final_check = 1
    if (tup[4] == 0 and (tup[0] != tup[8] or tup[8] != tup[10] or tup[10] != tup[0])): final_check = 1
    if (tup[5] == 0 and (tup[2] != tup[8] or tup[8] != tup[9] or tup[9] != tup[2])): final_check = 1

    if(final_check==0): data.append(tup)
    return data
def check2(data2)->list: #for data_b_5_0_4_exception
    data = []
    for tup in data2:
        check_1=check_2=check_3=check_4=0
        final_check=0
        if (tup[0] == 0 or tup[1] == 0 or tup[2] == 0 or tup[3] == 0 or tup[4] == 0 or tup[5] == 0 or tup[6] == 0): check_1 = 1
        if (tup[0] == 0 or tup[1] == 0 or tup[2] == 0 or tup[7] == 0 or tup[8] == 0 or tup[9] == 0 or tup[10] == 0): check_2 = 1
        if (tup[0] == 0 or tup[3] == 0 or tup[4] == 0 or tup[7] == 0 or tup[8] == 0 or tup[11] == 0 or tup[12] == 0): check_3 = 1
        if (tup[1] == 0 or tup[3] == 0 or tup[5] == 0 or tup[7] == 0 or tup[9] == 0 or tup[11] == 0 or tup[13] == 0): check_4 = 1
        final_check=max(check_1,check_2,check_3,check_4)
        if(final_check==0): data.append(tup)
        return data
input_file_path = output_file_path = 'predicates/data_b_5_0_4_exception'
with open(input_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
#paste sort conditions here
data=check2(data2)
for tup in data:
    o.printx(tup)
#


