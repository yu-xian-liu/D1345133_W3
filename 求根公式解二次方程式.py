a=int(input("請輸入二次方程式係數a:"))
b=int(input("請輸入二次方程式係數b:"))
c=int(input("請輸入二次方程式係數c:"))
d=(-b+((b**2-4*a*c)**0.5))/2*a
e=(-b-((b**2-4*a*c)**0.5))/2*a
print(f'x1={d},x2={e}')