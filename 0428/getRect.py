import sys
def getSubsum(data):
    n = len(data)

    if n==1:
        return data[0]

    mid = n//2
    left = getSubsum(data[:mid])
    right = getSubsum(data[mid:])

    Sum = 0

    leftSum = 0
    rightSum = 0

    for i in range(mid-1,-1,-1):
        Sum += data[i]
        leftSum = max(Sum,leftSum)
    
    Sum = 0

    for i in range(mid,n):
        Sum += data[i]
        rightSum = max(Sum, rightSum)
    
    return max([left,right,leftSum+rightSum])
    
def getRect(heights) :
    '''
    n개의 판자의 높이가 주어질 때, 이를 적당히 잘라 얻을 수 있는 직사각형의 최대 넓이를 반환하는 함수를 작성하세요.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getRect(data))

if __name__ == "__main__":
    main()
