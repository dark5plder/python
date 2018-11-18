s=7
t=10
a=4
b=12
m=3
n=3
apples=[2,3,-4]
apples[:]=[i+a for i in apples]

oranges=[3,-2,-4]
oranges[:]=[i+b for i in oranges]

count_apple=0
count_orange=0

for i in range(0,m):
    if (apples[i]>=s and apples[i]<=t):
        count_apple=count_apple+1
    else:
        pass
for j in range(0,n):
    if(oranges[j]<=t and oranges[j]>=s):
        count_orange=count_orange+1
    else:
        pass
print(count_apple,count_orange)
