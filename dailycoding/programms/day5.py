"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

"""
#car(pair) = a ; cdr(pair) = b

def cons(a, b):
    def pair(f):
        f(a, b)
        return f(a, b)
    return pair

def get_object_value_car(a, b):
    get_value_car = cons(a, b).__closure__[0].cell_contents
    return get_value_car
def get_object_value_crd(a, b):
    get_value_crd = cons(a, b).__closure__[1].cell_contents
    return get_value_crd

