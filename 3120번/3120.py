#3120

a, b = map(int,input().split())
tmp = a - b 
cnt = 0
tmp_list = [0,0,0,0,0,0]
while True:
    if tmp == 0 : break
    tmp_list[0] = abs(tmp + 10)
    tmp_list[1] = abs(tmp + 5)
    tmp_list[2] = abs(tmp + 1)
    tmp_list[3] = abs(tmp - 1)
    tmp_list[4] = abs(tmp - 5)
    tmp_list[5] = abs(tmp - 10)
    tmp = min(tmp_list) 
    cnt += 1
    

print(cnt)
