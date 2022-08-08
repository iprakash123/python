a=('ip',1,5,6)
print(type(a))
print(a[0:2])
print(a[2:])


b=('ip','raja','deep','ans')
if'deep'in b:
    print("super")
else:
    print("not valid")


c=('ip','ajith','vijay','surya')
d=list(c)
d[2]='karthi'
c=tuple(d)
print(c)


e=('ip','ajith','vijay','surya')
f=list(e)
e.append("sk")
e=tuple(f)
print(e)

g=('ip','ajith','vijay','surya')
h=("sj",)
g +=h
print(g)








