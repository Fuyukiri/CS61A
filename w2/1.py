from re import X


def make_adder(n):
    """ return a function that takes of K, N and return K + N
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

    # make_adder(adder(__n__, k))

# c://define square(X) (x * x)
swap = lambda x, y: (y, x)

def square(x):
    return x * x
def search(f):
    xx = 0
    while True:
        if f(xx):
            return xx
        xx += 1

def inverse(g):
    """
    return g(y) such that g(f(x)) ->x

    y = f(x)
    """
    return lambda y : search(lambda x : g(x) == y)



