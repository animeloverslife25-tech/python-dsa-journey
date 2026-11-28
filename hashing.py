n = [1, 2, 2, 5, 6, 7, 5, 8, 9, 10]
m = [2, 44, 5, 11, 11, 111, 4, 5, 8, 9, 0, 10]

# for i in range(0, len(m)):
#     count = 0
#     for j in range(0, len(n)):
#         if m[i] == n[j]:
#             count += 1
#     print(m[i], "is:=", count)


# hash_list=[0]*11
# for i in n:
#     hash_list[i]+=1
# for num in m:
#     if num < 1 or num > 10:
#         print(f"{num}: 0")
#     else:
#         print(f"{num}: {hash_list[num]}")



#character hashing
s="azssuyyzzsdcx"
q=["a","s","c","d","x","y","z"]
hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1

for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97 
    print(f"{ch}: {hash_list[index]}")