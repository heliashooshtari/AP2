#tamrin2
A=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
L=list(A)
print(A)  
min=max=L[0]
for i in L[1:]:
    if i<min:
        min=i
    elif i>max:
        max=i
print(min)
print(max)        