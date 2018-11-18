# a=[2,4]
# b=[16,32,96]
a=[3,4]
b=[24,48]
f=[4,8,12,16]
m=len(a)
n=len(b)
c=list(range(a[m-1],b[0]+1))
print(c)
def divisible_numbers(a, b):
    return [i for i in a if all(i%j==0 for j in b)]

def check(num,den):
	c=0
	for j in range(len(den)):
		e=all(i%den[j]==0 for i in num)
		if (e==True):
			c=c+1
		else:
			pass
	return(c)
d=divisible_numbers(c,a)
print(d)
e=check(b,d)
print(e)