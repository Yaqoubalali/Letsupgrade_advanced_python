list1=[10,20,30,40,50]
list2=[5,15,25,35,45,60]
list3=[]
x=0
L=len(max(list1,list2))
while x < L:
    try:
        if list1[x] < list2[x]:
            add1=list1[x]
            add2=list2[x]
        elif list2[x] < list1[x]:
            add1=list2[x]
            add2=list1[x]
    except Exception as o:
        continue
    list3.append(add1)
    list3.append(add2)
    x=x+1
print(list3)
    
