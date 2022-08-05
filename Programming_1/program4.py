def fact(n):
    final = 1
    for i in range(1, n + 1):
        final = final * i

    return final


def multi(target, r):
    for i in range(1, r + 1):
        print(f'{target} X {i} = {target * i} \n')


def fibonacci(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)


def sum_num(n1, n2):
    if n1 != 0 and n2 != 0:
        return f'The sum of {n1} and {n2} is {n1 + n2}'
    else:
        if n1 == 0:
            return f'{n1} is zero'
        else:
            return f'{n2} is zero'



def amstrong_number(n):
    temp = n
    length = len(str(n))
    a = 0
    addn = 0
    while temp!=0:
        a = a%10
        addn = addn+(a**length)
        temp = temp //10

    if(addn == n):
        return f'The number {n} is an amstrong number'
    else:
        return f'The number {n} is not an amstrong number'



print(f'The factorial is {fact(5)}')
num = int(input("Enter the number for which you need to find the multiplication table: "))
r = int(input("Enter the order till which you want to find the table: "))
print(multi(num, r))

fib = int(input("Enter the number for which you need to fibonacci series: "))
fibonacci(fib)

n1 = int(input('Enter 1 numbers : '))
n2 = int(input('Enter another number'))
print(sum_num(n1, n2))

ams = int(input('Enter a number : '))
print(amstrong_number(ams))