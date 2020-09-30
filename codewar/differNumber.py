def find_outlier(integers):
    L1=[]
    L2=[]
    for i in integers:
        if i%2!=0:
            L1.append(i)
        else:
            L2.append(i)
    if len(L1)>len(L2):
        for j in L2:
            return j
    else:
        for j in L1:
            return j


def square_digits(num):
    L1=[]
    L2=[]
    a=str(num)
    for i in a:
        L1.append(i)
    for j in L1:
        k=int(j)
        L2.append(str(k*k))
    return int(''.join(L2))


if __name__ == '__main__':
    print find_outlier([2, 4, 6, 8, 10, 3])
    print find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
    find_outlier([160, 3, 1719, 19, 11, 13, -21])
    print square_digits(9119)