a=[3,2,1,2,3]
b=0
c=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            b=j-i
            c.append(b)
        else:
            pass
print(min(c))