arr=(10,5,2,3,5,6,11,6,0)
sorted_arr=sorted(arr)
n=len(sorted_arr)
sum_arr=sum(sorted_arr)
temp=[]
for i in range(0,n):
    temp.append(sum_arr-sorted_arr[i])
print(temp[n-1],temp[0])