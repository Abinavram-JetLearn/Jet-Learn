list = [3,9,4,2]
swap = 0
sorted = False
while sorted == False:
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            swap += 1
    if swap != 0:
        swap = 0
    else:
        sorted = True
print(list)