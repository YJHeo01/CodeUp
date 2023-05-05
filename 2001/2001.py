pasta = int(input())
for i in range(2):
    tmp = int(input())
    if pasta > tmp:
        pasta = tmp # 제일 저렴한 파스타값 구하기
    
juice = [0,0]

for i in range(2):
    juice[i] = int(input()) 

juice.sort() #제일 저렴한 주스값을 juice[0]에 저장

set_price = float((pasta + juice[0]) * 1.1)

print("%.1f" %set_price)
