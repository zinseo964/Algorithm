def stair(data) :
    '''
    각 계단에 쓰여있는 점수가 list로 주어질 때, 이 게임에서 얻을 수 있는 총 점수의 최댓값을 반환하는 함수를 작성하세요.
    '''
    n = len(data)
    T = [0] * n
    T[0] = data[0]
    T[1] = data[1]
    for i in range(2, n+1):
        T[i] = max(T[i-1],T[i-2]) + data[i]
    return T[n]

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(stair(data))

if __name__ == "__main__":
    main()
