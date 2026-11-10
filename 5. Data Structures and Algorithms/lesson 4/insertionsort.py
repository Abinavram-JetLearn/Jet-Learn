list = [3,9,4,2,1,6,7,4]
for i in range(1,len(list)):
    current = list[i]
    j = i-1
    while current < list[j] and j >= 0:
        list[j+1] = list[j]
        list[j] = current
        j = j-1
        print(list)
    