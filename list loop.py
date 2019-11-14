L=[1,2,3,4,5,6,7]
for i in range(-3,0,1):
    L.pop(i)
print(L)

L=[1,2,3,4,5,6,7,8,9,10]
for i in L:
    if i%2==1:
     L.remove(i)
print(L)


L1=[1,"red",2,3]
L2=["apple","orenge","grape"]
L3=["python","java","c"]
print(L1+L2)
L2.extend(L1)
print(L2)
L3.append("C++")
print(L3)
L1.remove("red")
print(L1)

L2=["apple","orenge","grape"]
for fruit in L2:
    print(fruit)














