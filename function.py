

# def is_even(num):
#     if type(num) == int:
#         if num % 2 == 0:
#             return 'even'
#         else:
#             return 'odd'
#     else:
#         return 'not an integer'

# for i in range(1, 11):
#     x = is_even(i)
#     print(i, "is", x)

                           # *args
# def add_numbers(*args):
#     print(args)
#     print(type(args))
#     return(sum(args))

# print(add_numbers(2,4,6,8,10))
# print(add_numbers(2,5,7,8,9,10,12))

# def student_info(*args, **kwargs):
#     print("subjects:", args)
#     print("details:", kwargs)

# student_info('maths', 'english', 'biology', name="Debasish", age=24, city="paschim medinipur")

s1 = "debasish ghosh"
s2 = lambda func: func.upper()
print(s2(s1))