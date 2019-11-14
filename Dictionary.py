#create a dictionary with key 'rollno' and add list of rollnos, similarly and add "name" key and add 5 names in that key

dict={"rollno":[1,2,3,4],"name":["ande","Shirsak","a","b"]}
roll=dict["rollno"]
nam=dict["name"]

data=int(input("enter your rollno"))
temp=0
for i in range(len(roll)):
    if roll[i]==data:
        temp=i
        print(nam[temp])


dict={"rollno":[1,2,3,4],"name":["ande","Shirsak","a","b"]}
del(dict["rollno"])
print(dict)

maths = {"john":88,"sam":77}
for key,value in maths.items():
    print(value)

maths = {"john":88,"sam":77}
for key,value in maths.items():
    print(key)


a={"rollno":[1,2,3,4],"name":["ande","Shirsak","a","b"]}
a.update({"address":["kTM,BKT,v,g"]})
print(a)


a={"rollno":[1,2,3,4]}
b={"name":["ande","Shirsak","a","b"]} #concatinate d and b
c={}
for d in (a,b):c.update(d)
print(c)



a={"rollno":[1,2,3,4]}
if "rollno" in a:
    print("key is present")
else:
    print("key is not present")


d={}
for x in range(1,5):
    d[x]=x**2
print(d)


a={"a":100, "b":200}
b={"x":300, "y":200}
c=a.copy()    #to merge a dictionary in third empty variable
c.update(b)
print(c)





dict={"rollno":[1,2,3,4,5,6,7,8],"name":["anuragh","rita","ritesh","sita","hari","gauri","ram","gita"],"marks":[50,60,82,94,55,66,77,88],"gender":["male","female","male","female","male","female","male","female"]}
for i in range(len(dict["rollno"])):
    if dict["gender"][i]=="male":
        print(dict["name"][i])
        print(dict["marks"][i])





