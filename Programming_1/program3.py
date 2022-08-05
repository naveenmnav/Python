def num_state(n):
    if n == 0:
        return f'The number {n} is Zero'
    elif n > 0:
        return f'The number {n} is Positive'
    elif n < 0:
        return f'The number {n} is Negative'
    else:
        return f'Undefined'


def odd_or_even(n):
    if n % 2 == 0:
        return f'The number {n} is Even'
    elif n % 2 != 0:
        return f'The number {n} is Odd'
    else:
        return f'Undefined'


def leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        return f'{year} is a leap year'
    elif year % 4 == 0 and year % 100 != 0:
        return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year'


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return f'{n} is not a prime number'
                return f'{i} times of {n // i} is {n}'
                break
            else:
                return f'{n} is a prime number'
    elif n==0:
        return f'O is neither prime nor composite'
    else:
        return f'{n} is a prime number'


def print_prime(n):
    arr = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            arr.append(i)

    fin = len(arr)

    return f'The total count is {fin} \n {set(arr)}  '


print(num_state(10))
print(num_state(-10))
print(odd_or_even(10))
print(odd_or_even(13))
print(leap_year(2015))
print(leap_year(2020))
print(is_prime(4))
print(is_prime(13))
print(print_prime(10000))

