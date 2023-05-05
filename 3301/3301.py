#3301

n = int(input())

money = [50000,10000,5000,1000,500,100,50,10]

cnt = 0
index = 0
while n!=0:
    if n - money[index] >= 0:
        n -= money[index]
        cnt += 1
    else : index += 1

print(cnt)
