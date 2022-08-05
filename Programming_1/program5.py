def lcm(x,y):
    if x > y:
        big = x
    else:
        big = y

    while(True):
        if((big % x == 0) and (big %y == 0)):
            lcm = big;
            break
        big = big+1
    return lcm

def hcf(x,y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if((x % i == 0) and (y % i  == 0)):
            hcf = i

    return hcf


def convert(x):
    print(oct(x))
    print(bin(x))
    print(hex(x))

'''
n1 = int(input('Enter number 1 : '))
n2 = int(input('Enter number 2 : '))
print(f'The LCM Is {lcm(n1,n2)}')

n3 = int(input('Enter number 1 : '))
n4 = int(input('Enter number 2 : '))
print(f'The HCF Is {hcf(n3, n4)}')
'''

print(convert(5))
print(ord('A'))