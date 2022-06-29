# This is a simple tree

n = int(input())
for i in range(1,n+1):
    for n in range(1,i+1):
        print (n,sep='', end='')
    print()