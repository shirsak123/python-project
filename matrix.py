#A=[[1,2,3],[4,5,6]]
#for row in A:
#    for element in row:
#        print(element)


b=[]
a=[]

for i in range(3):
    a.append(b)
    for j in range(2):
        b.append(1)
print(a)



a=[]
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(1)
print(a)




result = [["name","maths","eng"],
["john",88.0,86.0,76.0,66.0,76.0],
["sam",77.0,67.0,87.0,67.0,56.0]]
print(result[1])
sum=0
avg=0
for i in range(1,len(result[1])):
    sum=result[1][i]+sum
    avg=sum/len(result[1])
print(sum)
print(avg)




