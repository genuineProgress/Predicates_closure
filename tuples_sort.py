import operators as o
input_file_path = 'predicates/data_b_5_0_4_exception'
with open(input_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
#paste sort conditions here
data2.sort()
for tup in data2:
    o.printx(tup)