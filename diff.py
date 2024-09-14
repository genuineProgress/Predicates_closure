import operators as o
input1_file_path='predicates/data_b_5_0_4_operation'
input2_file_path='rows_output.txt'
with open(input1_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
data = data2
input1=set(data)
with open(input2_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
data = data2
input2=set(data)
output=input2.difference(input1)
output=list(output)
output.sort()
for tup in output:
    o.printx(tup)
