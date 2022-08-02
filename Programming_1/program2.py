import calendar
import cmath


def km_miles(km):
    return km * (0.62137)


def ctof(c):
    return (c * (1.8) )+ 32


def disp_cal(year, month):
    return calendar.month(year, month)


def quad(a, b, c):
    d = (b ** 2) - (4 * a * c)
    return (-b - cmath.sqrt(d)) / (2 * a)


def swaps(x, y):
    x, y = y, x
    return x, y


print(f'KM to Miles {km_miles(100)}')
print(f'Celsius to F {ctof(40)}')
print(f'Calendar : {disp_cal(2022, 9)}')
print(f'Quadratic Equation : {quad(10,20,14)}')
print(f'Swapping : {swaps(34, 56)}')
