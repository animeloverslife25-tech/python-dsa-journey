#brute force method

# num=20
# result=[]
# for i in range(1, num + 1):
#     if num%i==0:
#         result.append(i)
        
# print("result=",result)


#better solution
# num=20
# result=[]
# for i in range(1,(num//2)+1):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print("result=",result)

#optimal approuch
from math import sqrt
num=20
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
    if num%i!=i:
        result.append(num//i)

result.sort()
print("result",result)