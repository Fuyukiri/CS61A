
def p(s):
    if len(s) == 1:
        yield s
    else:
        for x in p(s[1:]):
            for i in range(len(s)):
                # print("x:", x, "i:", i, "s[0]:", s[0])
                yield x[:i] + [s[0]] + x[i:]

a = p([1,2,3])
sorted(p((10, 20, 30)))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))