num=[1,1,2,2,3,3,3,3,4,5,5,5]
freq_map={}
for i in range(0,len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1

print("freq_map:=",freq_map)


#hash.get method
# num=[1,1,2,2,3,3,3,3,4,5,5,5]
# hash_map={}
# n=len(num)
# for i in range(0,n):
#     hash_map[num[i]]=hash_map.get(num[i],0)+1

# print("hash_map:=",hash_map  )