a=[10,20,20,10,10,30,50,10,20]
a=sorted(a)
print(a)
# c=[]
# for i in range(len(a)):
#     b=a.count(a[i])
#     c.append(b)
# print(c)
def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return(unique_list)
z=unique(a)
print(z)
# y=[x for x in z]

d=[]
for i in range(len(z)):
	b=a.count(z[i])
	d.append(b)
e=[int(x/2) for x in d]
print(sum(e))