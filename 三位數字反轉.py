a=int(input("請輸入三位數字:"))
b=int(a/100)
c=int((a%100)/10)
d=(a%100)%10
print(f'結果:{d}{c}{b}')