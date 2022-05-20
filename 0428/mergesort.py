import sys

def makeResult(left,right):
    l = len(left)
    r = len(right)
    result = []
    for i in range(0,l+r):
        if(len(left)==0):
            result.append(right[0])
            del(right[0])
        elif(len(right)==0):
            result.append(left[0])
            del(left[0])
        elif(left[0]>right[0]):
            result.append(right[0])
            del(right[0])
        else:
            result.append(left[0])
            del(left[0])
    return result

def mergeSort(data) :
    l = len(data)
    i = l // 2
    if(l > 1):
        l_temp = mergeSort(data[:i])
        r_temp = mergeSort(data[i:])
        result = makeResult(l_temp,r_temp)
        print(i,result)
        return result
    else:
        return data
def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
