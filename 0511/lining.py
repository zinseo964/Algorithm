import sys

def lining(n) :
    
    T = [1,2];
    for i in range(2, n+1):
        T.append(T[i-1] + T[i-2])
    return T[n]


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = int(input())

    print(lining(data))

if __name__ == "__main__":
    main()
