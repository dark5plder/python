n = int(input())

grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
for i in range(n):
    if (grades[i]<40 and 40-grades[i]<3):
        grades[i]=grades[i]+(40-grades[i])
    elif(grades[i]%5==0):
        pass
    elif((5-grades[i]%5)<3):
        grades[i]=grades[i]+5-(grades[i]%5)
    else:
        pass
    
print(grades)