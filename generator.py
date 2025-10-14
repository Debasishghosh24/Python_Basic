# print(next(gen))
# print(next(gen))
# print(next(gen))

# s = "Debasish"
# it = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


def gen_demo():
    yield "Debasish"
    yield "Ghosh"
gen = gen_demo()
for i in gen:
       print(i)