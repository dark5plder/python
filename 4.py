time = "12:40:22AM"
data = time.split(":")

if (data[2].find("AM") ==2):
    if(data[0]=="12"):
        data[0]="00"
    else:
        pass
elif(data[2].find("PM") ==2):
    if(data[0]=="12"):
        pass
    else:
        data[0]=int(data[0])+12
d=data[2]
data[2]=d[0:2]
myList = ':'.join(map(str, data))
print(myList)