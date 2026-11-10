list = [3,9,4,2]

def Mergesort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        print(left)
        print(right)
        Mergesort(left)
        Mergesort(right)

Mergesort(list)