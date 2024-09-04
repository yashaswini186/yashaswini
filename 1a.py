m1=int(input("enter the number"))
m2=int(input("enter the number"))
m3= int(input("enter the number"))
if(m1<m2 and m1<m3):
    Avg=(m2+m3)/2
elif(m2<m1 and m2<m3):
    Avg=(m1+m3)/2
else:
    Avg=(m1+m2)/2
print("Average of two marks",Avg)