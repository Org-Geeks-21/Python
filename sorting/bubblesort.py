def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list   

print(bubblesort([2,3,5,1,4,8,7]))    