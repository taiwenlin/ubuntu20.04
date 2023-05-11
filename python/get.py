def getmax(a,b,c):
    lst=[a,b,c]
    return max(lst)

def get_sum(a,b,c,d):
    lst=[a,b,c,d]
    return sum(lst)

def get_average(a,b,c,d):
    lst=[a,b,c,d]
    return sum(lst)/len(lst)

if __name__ == "__main__":
    print(getmax(1,4,3))
    print(get_sum(1,2,3,4))
    print(get_average(1,2,3,4))