from math import factorial

#Pascal Traingle as a Square
n = int(input('Enter a number: '))
for i in range(n):
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    for k in range(j, n-1):
        print("0", end=" ")
    print()


#Daimond starts pattern

n = int(input("Enter a number: "))
for i in range(1, (n+1)//2 + 1):
    for j in range((n+1)//2 - i):
        print(" ", end = "")
    for k in range((i*2)-1):
        print("*", end = "")
    print()

for i in range((n+1)//2 + 1, n + 1):
    for j in range(i - (n+1)//2):
        print(" ", end = "")
    for k in range((n+1 - i)*2 - 1):
        print("*", end = "")
    print()



#Hollow Equilateral Triangle

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i - 1):
        print('  ', end='')
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print('* ' , end='')
        else:
            if i == n - 1:
                print('* ', end='')
            else:
                print('  ', end='')
    print()


#Hollow Inverted Triangle


n = int(input("Enter a number = "))

for i in range(0,n):
    for j in range(0,n):
        if i == 0 or j == n-1 or j == i :
            print('* ', end = '')
        else:
            print('  ', end = '')
    print()
