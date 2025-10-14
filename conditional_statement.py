# age = 20
# if age<= 21:
#   print("you are young")
# else:
#  print("you are not young")

     # nested if else\\


age = 18
is_member = True
if age <= 18:
    if is_member:
        print("you are eligible for a discount")
    else:
        print("you are not eligible for a discount")
elif age >= 65:
    if is_member:
        print("you are eligible for a senior citizen discount")
    else:
        print("you are not eligible for a senior citizen discount")