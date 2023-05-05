N = int(input())
A, B = map(int,input().split())
D_cal = int(input())
T_cal = [0]*N
for i in range(N):
    T_cal[i] = int(input())
T_cal.sort()
biggest_cal = D_cal/A
for i in range(1,N):
    tmp = D_cal
    for j in range(i):
        tmp = tmp + T_cal[-1-j]
    tmp = tmp / (A + B*i)
    if tmp > biggest_cal: biggest_cal = tmp
    else : break
    
print(int(biggest_cal))
