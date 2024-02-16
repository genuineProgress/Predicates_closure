# from inspect import signature
import itertools
import sys
import function_def as f
import operators as o
tm=1 #that variable tells whether matrix from input_file_path should be transposed before processing, 1 - yes, 0 - no
rp=0 #that variable tells whether program (except transposition) should be executed, 1 - yes, 0 - no
input_file_path = output_file_path = 'predicates/test_1'
if(tm==1):
    matrix = o.read_matrix_from_file(input_file_path)
    transposed_matrix = o.transpose_matrix(matrix)
    o.write_matrix_to_file(transposed_matrix, output_file_path)
if(rp==0): sys.exit()
with open(input_file_path, 'r') as input:
    data = input.readlines() #reading data
data2=[]
count=0
for str in data:
    if(str): data2.append(tuple([int(i) for i in str.split()]))
    count=count+1
print(count)
print(data2)
data = data2
data = set(data)
prel_data2=o.generate_columns(12)
data2=set()
for elem in prel_data2:
    data2.add(tuple((elem)))
data2=data2.difference(data)
data2=list(data2)
data2.sort()
for tuple in data2:
    o.printx(tuple)
sys.exit()
# below code fragment was needed once in the past check
# for tuple in data:
#     if(tuple[0]!=1 or tuple[1]!=1 or tuple[2]!=1 or tuple[3]!=1):
#         if(tuple[4]!=1 or tuple[5]!=1 or tuple[6]!=1 or tuple[7]!=1):
#             if(tuple[8]!=1 or tuple[9]!=1 or tuple[10]!=1 or tuple[11]!=1):
#                 print(tuple)
#                 break
print(data)

#printing columns of our predicate as tuples
#for tup in data:
#    print(tup)
iteration=0
while True:
    n = len(data)
    x = itertools.product(data, repeat=2)
    #z = itertools.product(data, repeat=3)
    data2 = set(map(lambda y: tuple(f.b_5(*a) for a in zip(*y)), x))
    data = data.union(data2)
    # below code fragment is used to show tuples from which a particular tuple may be derived
    # for tuple1 in z:
    #     tuple2=lambda tuple1: tuple(f.s_4(*a) for a in zip(*tuple1))
    #     if tuple2(tuple1)==(0, 0, 0, 1, 0, 1, 1, 0):
    #          print(tuple1)
    #         #for tup in data:
    #    #print(tup)
    #print()
    iteration = iteration + 1
    print(iteration, len(data))
    if(len(data)==n): break
    n=len(data)
# #print(len(data))
# below code fragment was needed once in the past check
# for x in range (0,3):
#     print((2,2,1,1,1, 1,,1,) in data)
# print((2,2,1,1,2,1,2,1) in data)
# print((2,2,1,1,2,1,1,2) in data)
# print((2,2,1,1,1,2,2,1) in data)
# print((2,2,1,1,1,2,1,2) in data)
# print((2,2,1,1,2,2,2,1) in data)
# print((2,2,1,1,2,2,1,2) in data)
# print((2,2,1,1,2,1,2,2) in data)
# print((2,2,1,1,1,2,2,2) in data)

# below code fragment was needed once in the past check
#output = open("dataout.txt", "w")
# y=itertools.product({1,2},repeat=10)
# count_neg=0
# for tup in y:
#     if(tup[0]==2 and (tup in data)==False):
#         if (f.check_s_2_out_tup(tup)):
#             print(tup)
#             count_neg=count_neg+1
# print(count_neg)
count=0
data=list(data)
data.sort() #that is to print tuples in lexicographical order

# output_data=[]

for tup in data:
    # below code fragment was needed once in the past check
    #if tup[0]==2:
        #output_data.append(tup)

        count=count+1
        o.printx(tup)
print(count)

# below code fragment was needed once in the past check
#print(len(signature(b_6).parameters))
#with open('data.txt', 'w') as f:
#for tup in data2:
#    print(tup)
#print(operators.check_fs(data2))
