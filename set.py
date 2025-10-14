# s = set(["a", "b", "c"])
# print(s)


             # adding elements in pytho set



# Creating a Set
# people = {"Jay", "Idrish", "Archi"}
# print("People:")
# print(people)


# people.add("Daxit")


# # set using iterator
# for i in range(1, 6):
#     people.add(i)

# print("\nSet after adding element:", end = " ")
# print(people)
#set difference
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

new_set = set1 - set2
print(new_set)
