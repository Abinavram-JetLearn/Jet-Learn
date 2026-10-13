import time
list =  ["1","11","111", "1111", "11111", "111111", "1111111", "11111111", "111111111", "1111111111"]
output = ""
l = 0
h = 0
midpoint = 0

def Linear_Search():
    answer = input("find this: ")
    start = time.time()
    for i in range (len(list)):
        if answer == list[i]:
            output = "item found"
            break
        else:
            output = "item not found"
    print(output)
    end = time.time() - start
    print(end)

Linear_Search()

def Binary_Search():
    answer = input("find this: ")
    start = time.time()
    l = 0
    h = len(list) - 1
    while l<=h:
        output = "item not found"
        midpoint = (l+h)//2
        if list[midpoint] == answer:
            output = "item found"
            break
        elif list[midpoint] > answer:
            h = midpoint-1
        elif list[midpoint] < answer:
            l = midpoint+1
    print(output)
    end = time.time() - start
    print(end)


Binary_Search()