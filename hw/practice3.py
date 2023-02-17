sum=0
for i in range(1,101):
    if 40<=i<=67:
        if i%2==1:
            print(i)
            sum+=i
print(sum)