a = int(input("Enter a number"))
b=True
for i in range(2,a):
    if a%i == 0:
        b=False
        break


if(b==True):
    print('it is prime')
else:
    print('it is not a prime')

