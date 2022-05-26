
# def keep_ints(cond, n):
#     """Print out all integers 1..i..n where cond(i) is true
#     >>> def is_even(x):
#     ...     # Even numbers have remainder 0 when divided by 2.
#     ...     return x % 2 == 0
#     >>> keep_ints(is_even, 5)
#     2
#     4
#     """
#     i = 1
#     while i < n:
#         if cond(i):
#             print(i)
#         i += 1

# def make_keeper(n):
#     """Returns a function which takes one parameter cond and prints out
#     all integers 1..i..n where calling cond(i) returns True.
#     >>> def is_even(x):
#     ...     # Even numbers have remainder 0 when divided by 2.
#     ...     return x % 2 == 0
#     >>> make_keeper(5)(is_even)
#     2
#     4
#     """
#     def wrapper(cond):
#         i = 1
#         while i < n:
#             if cond(i):
#                 print(i)
#             i += 1 
#     return wrapper

# def curry2(h):
#     def f(x):
#         def g(y):
#             return h(x, y)
#         return g
#     return f
# make_adder = curry2(lambda x, y: x + y)
# # make_adder -> f
# add_three = make_adder(3)
# # add_three = f(3) -> g
# add_four = make_adder(4)
# # add_four = f(4) -> g
# five = add_three(2)
# # five = g(3) -> lambda(3, 2)
# print(five)


n = 7

def f(x):
    n = 8
    print("xxxx")
    return x + 1

def g(x):
    n = 9
    print("gg")
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)

g = (lambda y : y())(f)


s = "y"
h = s # "y"
def y(y):
    h = "h"
    print("y1 ", y)
    if y == h:
        return y + "i"
    y = lambda x : x(h)
    print("y2 ",y)
    print(h)
    return lambda hh : y(hh)
bbb = y(y)(y) # y("y")("y")
print(bbb)