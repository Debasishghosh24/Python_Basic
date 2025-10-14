# a = [1, 2, 3, 4, 5]
# res = []
# for val in a:
#     res.append(val * 2)
# print(res)

         # Dictionary comprehension 

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5] 

myDict = { k:v for (k,v) in zip(keys, values)}
print(myDict)