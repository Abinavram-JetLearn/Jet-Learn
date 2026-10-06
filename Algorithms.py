import time

num = int(input("Any Num: "))
start = time.time()
ans = 0
for i in range(num + 1):
    ans = ans + i
print(ans)
end = time.time() - start
print(end)

num = int(input("Any Num: "))
start = time.time()
ans = (num*(num+1))/2
print(ans)
end = time.time() - start
print(end)
