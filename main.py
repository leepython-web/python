# This is a simple tree
n = int(input())
sumabsolute = int(((1 + n)/2)*n)
sum = 0
for i in range(1,n):
    x = int(input())
    sum += x
print(sumabsolute - sum)