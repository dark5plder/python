a=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
b="zaba"
c=list(b)
e=[]
for i in range(len(c)):
	d=ord(c[i])-96
	e.append(d)
f=[]
print(e)
for j in range(len(e)):
    x=a[e[j]-1]
    f.append(x)
print(f)
g=len(e)*max(f)
print(g)