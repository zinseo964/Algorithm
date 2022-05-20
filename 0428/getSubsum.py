import sys
def getMaxsum(data):
    sum = 0
    maxSum = 0
    for i in range(0,len(data)):
        sum += data[0]
        del(data[0])
        maxSum = max(sum,maxSum)
    
    return maxSum

def getSubsum(data) :
    
    l = len(data)
    i = l // 2
    mid_l = []
    mid_r = []
    if l== 1:
        return data[0]
    else : 
        mid_l = data[:i]
        mid_r = data[i:]
        left = getSubsum(data[:i])
        right = getSubsum(data[i:])
        mid_l.reverse()
        mid = getMaxsum(mid_l) + getMaxsum(mid_r)
        return max(left,right,mid)
    

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
