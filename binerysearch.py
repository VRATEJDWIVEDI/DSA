arr=[10,20,30,40,50,60,70,80]
lb,key=0,40
ub=len(arr)-1
middle=lb+(ub+lb)//2
while lb<=ub:
    if arr[middle]==key:
        print("data is found",key)
        break
    elif arr[middle]<key:
        lb=middle+1
    else:
        ub=middle-1
else:
    print("data is not found")
