import sys

def coinChange(n) :
    result = 0
    coins = [100,50,10,5,1]
    for coin in coins :
        result += n // coin
        n = n %coin
    return result
        
def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(coinChange(n))

if __name__ == "__main__":
    main()
