row=5
for i in range (0,row):
    for j in range(i,row-1):
        print (" ",end="")
    for k in range(-1,i):
        print("*",end="")
    print("\n")