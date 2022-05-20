import sys

def getNearest(data, m) :
    data.sort()
    l = len(data)
    if(l == 2):
        a = data[0] - m
        b = data[1] - m
        if(abs(a) > abs(b)):
            return data[1]
        else:
            return data[0]
    elif(l==1):
        return data[0]
    else :
        i = int(l/2)
        if(m == data[i]):
            return m;
        elif(m < data[i]):
            return getNearest(data[:i+1],m) # 이게 포인트임 i까지가 아니라 i+1 까지라는거
        else:
            return getNearest(data[i:],m)
    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == "__main__":
    main()
