a=int(input("請輸入一個五位數:"))
b=int(a/10000)
c=int((a%10000)/1000)
d=int((a%1000)/100)
e=int((a%100)/10)
f=(a%100)%10
print('結果:')
print(b)
print(c)
print(d)
print(e)
print(f)