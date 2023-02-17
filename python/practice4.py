L=float(input("請輸入繩子長度"))
T=0
while L>=20:
    L/=2
    T+=1
print("對折%d次後小於20公分"%(T))