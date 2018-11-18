ar = list(map(int, input().rstrip().split()))
n=len(ar)
sorted_ar=sorted(ar)
count=0
for i in range(0,n):
    if(sorted_ar[n-1]==sorted_ar[i]):
        count=count+1
print(count)