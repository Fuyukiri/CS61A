from ucb import trace
@trace
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
@trace
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n : f_then_g(print, shrink, n // 10)