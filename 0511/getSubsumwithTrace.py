def getSubsumWithTrace(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합, 구간의 시작, 구간의 끝을 list로 반환하는 함수를 작성하세요.
    '''
    T = [0] * len(data)
    T[0] = max(0,data[0])
    first = []
    for n in range(1,len(data)):
        T[n] = max(0,(max(0,T[n-1]) + data[n]))
        if T[n] == 0:
            first.append(n)
    sum_num = max(T)
    
    last = T.index(sum_num) +1
    first_n = filter(lambda num : num < last , first)
    first_n = max(first_n) + 2
    
    return [sum_num, first_n, last]

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsumWithTrace(data))

if __name__ == "__main__":
    main()