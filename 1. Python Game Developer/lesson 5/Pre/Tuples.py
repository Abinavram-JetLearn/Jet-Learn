t = (10, 20, 30,[1,2,3,4,5])
ta = "red", "orange", "green"
taa = "red",

print(t[0])
print(ta[1])
t[3][0] = "1+1 = 3"
print(t)
print(len(taa))
print(t+ta+taa)

if "red" in ta:
    print("red in ta")
else:
    print("false")

for item in t:
    print(item)
for item in ta:
    print(item)
for item in taa:
    print(item)


