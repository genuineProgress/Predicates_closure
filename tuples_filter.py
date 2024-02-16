import operators as o
input_file_path = output_file_path = 'predicates/test_1'
with open(input_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
data=[]
#paste sort conditions here
for tup in data2:
    check_1=check_2=check_3=0
    final_check=0
    if (tup[0]==0 or tup[5]==0): check_2=1
    if (tup[1] == 0 or tup[3] == 0): check_3 = 1
    if (tup[2] == 0 or tup[4] == 0): check_1 = 1
    if (tup[6]==0): check_2=check_3=1
    if (tup[7]==0): check_1=check_3=1
    if (tup[8]==0): check_2=check_1=1
    if (check_1==check_2==check_3==1): final_check=1
    if (tup[0]==0 and tup[1]==0): final_check=1
    if (tup[2]==0 and tup[3]==0): final_check=1
    if (tup[4]==0 and tup[5]==0): final_check=1
    if(final_check==0): data.append(tup)

for tup in data:
    o.printx(tup)
#