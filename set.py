a={"apple","orange","grapes","mango"}
b={"apple","cherry","orange","guava"}
c={"orange","strawberry","litchi","grapes"}
d=(a.intersection(b))
e=(d.intersection(c))
v=(d.union(e))
print(v)
f=(a.union(b))
g=(f.union(c))
print(g)
y=(a.difference(b))
n=(b.difference(a))
m=(c.difference(b))
h=y.copy()
h.update(n)
i=h.copy()
i.update(m)
print(i)

