# version 1 

# num=[4,6,1,0,2]
# target=10
# for i in range(len(num)):
#     x=num[i]
#     y=target-x
#     for j in range(len(num)):
#         k=num[j]
#         # print(k)
#         if k==y:
#             print(f"The index for {target} is {i}{j}")
#             break



num=[2,7,11,15]
target=9
dict_seen={}
for i,value in enumerate(num):
    y=target-value
    if y in dict_seen:
        print([i,dict_seen[y]])
    else:
        dict_seen[value]=i
