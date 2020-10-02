#selction sort
n=int(input("Enter the number of elements u want in the list to sort"))
list=[]
for i in range(0,n):
    element=int(input("ENter the element for the list"))
    list.append(element)
print("before sorting")
print(list)
for i in range(0,len(list)-1):
    minindex=i
    for j in range(i+1,len(list)):
        if list[j]<list[minindex]:
            minindex=j
    if minindex!=i:
        list[minindex],list[i]=list[i],list[minindex]
print("after sorting")
print(list)
