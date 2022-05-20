def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    i = 0
    j = 0
    for x in p :
        if x == '(':
            i = i+1
        elif x == ')':
            j = j+1
    if i == j:
        return "YES"
    else :
        return "NO"

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


