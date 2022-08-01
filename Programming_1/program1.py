import random


def hello():
    return 'Hello World'


def addition(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise Exception('Cannot Divide by 0')
    else:
        return a / b


def areaOfTriangle(l, b):
    return l * b


def swap_var(a, b):
    a, b = b, a

    return a, b


def random_num(a, b):
    return random.randint(a, b)

print(f'Hello World Program :  {hello()}')
print(f'Add :  {addition(10, 20)} ')
print(f'Division : {division(10, 10)} ')
print(f'Area : {areaOfTriangle(10, 12)}')
print(f'Swapping : {swap_var(1010, 101)}')
print(f'Random generator : {random_num(8, 19)}')
