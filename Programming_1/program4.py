def fact(n):
    final = 1
    for i in range (1,n+1):
        final = final*i

    return final


def multi(target, r):

    for i in range(1,r+1):
        print(f'{target} X {i} = {target*i} \n')


print(f'The factorial is {fact(5)}')
num = int(input("Enter the number for which you need to find the multiplication table: "))
r = int(input("Enter the order till which you want to find the table: "))
print(multi(num, r))

