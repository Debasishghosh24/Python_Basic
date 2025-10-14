# d1 = {1: 'Debasish', 2:'Ghosh'}
# print(d1)

# d2 = dict(a="Debasish", b="Ghosh")
# print(d2)

# d = {"name": "debasish", 1: "suman"}
# # print(d["name"])
# print(d.get("name"))

                     # Adding or updating elements in dictionary

# d = {1: 'Debasish', 2:'Ghosh'}
# d["age"] = 22
# d[1] = 'suman'
# print(d)

                                   #Removing dictionary items

# d = {1: 'Debasish', 2: 'GHosh', 3: 'Suman', 'age':22}

# # Using del to remove an item
# del d["age"]
# print(d)

# # Using pop() to remove an item and return the value
# val = d.pop(1)
# print(val)

# # Using popitem to removes and returns
# # the last key-value pair.
# key, val = d.popitem()
# print(f"Key: {key}, Value: {val}")

# # Clear all items from the dictionary
# d.clear()
# print(d)


                                       # iterating through a dictionary
# d = {1: 'Debasish', 2: 'Ghosh', 'age':22}

# # Iterate over keys
# for key in d:
#     print(key)

# # Iterate over values
# for value in d.values():
#     print(value)

# # Iterate over key-value pairs
# for key, value in d.items():
#     print(f"{key}: {value}")                      

                           # Nested Dictionary


students = {}

students['student1'] = {'name': 'Debasish', 'age': 21, 'grade': 'A'}
students['student2'] = {'name': 'Sayantan', 'age': 22, 'grade': 'B'}
students['student3'] = {'name': 'Bodhi', 'age': 21, 'grade': 'A+'}

print("Student Details:")
print(students)

students['student1']['department'] = 'CSE'
print(students)

