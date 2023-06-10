import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

    
int_1 = int(input('Input an positive integer: '))
int_2 = int(input('Input a second positive integer: '))


question = input('Would you like to find out GCF, LCM, or GCD? ').upper()

if question == 'GCD':
    x = math.gcd(int_1, int_2)
    print(x)


if question == 'LCM':
    x = lcm(int_1, int_2)
    print(x)

if question == 'GCF':
    def gcf(a,b):
        if a > b:
            a,b = b,a
        
        for x in range(a,0,-1):
            if a % x == 0 and b % x ==0:
                return x
    x = gcf(int_1, int_2)
    print(x)
    
    