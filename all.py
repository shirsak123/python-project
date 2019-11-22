result = [["name","maths","eng"],
["john",88.0,86.0,76.0,66.0,76.0],
["sam",77.0,67.0,87.0,67.0,56.0]]
print(result[2])
sum=0
avg=0
for i in range(1,len(result[2])):
    sum=result[2][i]+sum
    avg=sum/len(result[2])
print(sum)
print(avg)