mysum=0
for i in range(5,10):
    mysum=mysum+i
print(mysum)

a=int(input("enter a number"))
for i in range(1,a,1):
    a=a*i
print(a)


a=int(input("Enter a number"))
for i in range(2,a,a):
    if(a%i==0):
        print("Its not a prime number ")
    else:
        print("Its a prime number")