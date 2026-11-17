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
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                k += 1
                i += 1
            else:
                list[k] = right[j]
                k += 1
                j += 1
        while j < len(right):
            list[k] = right[j]
            k += 1
            j += 1
        while i < len(left):
            list[k] = left[i]
            k += 1
            i += 1

Mergesort(list)
print(list)