# lst1=[1,2,3,4,5]
# lst2=[1,'python',4.5,5]
# lst3=list(["tom","sherry","jay"])
# lst4=list('python')
# lst5=[[1],["tom","terry","jay"],[3,4,409500559]]

# print(lst1)
# print(lst1,lst2,lst3)
# print("lst5:"+str(lst5))

# for e1 in lst5:    
#     print(e1,end="")

# d1={'chicken':2,'dog':4,'cat':3}
# print(d1['cat'])
# print(d1['chicken'])
# print(d1['dog'])
# print(d1)
# d1['cat']=4
# print(d1)
# d1['spider']=8
# print(d1)

# s1=set()
# s2=set((2,3,1))
# s3={1,2,3,4,5}
# s4={1,1,2,3,3}
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# s5={1,1,2,1,3,4,5}
# s6={5,4,3,2,1}
# print(s5)
# print(s6)

def sum_to_n(start,stop):
    s=0
    for i in range(start,stop+1):
        s+=i
    print("總和="+str(s))

sum_to_n(1,10)
sum_to_n(1,10)
sum_to_n(1,10)
def convert_to_f(c):
    f=(9.0*c)/5.0+32.0
    return f
g=convert_to_f(float(input("123")))
print(g)