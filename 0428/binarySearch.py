import sys

def binarySearch(data, m) :
    data.sort()
    l = len(data)
    if(l==1):
        if data[0] == m:
            return "Yes"
        else:
            return "No"
    else :
        i = int(l/2)
        if(m == data[i]):
            return "Yes";
        elif(m < data[i]):
            return binarySearch(data[:i],m)
        else:
            return binarySearch(data[i:],m)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(binarySearch(data, m))

if __name__ == "__main__":
    main()
