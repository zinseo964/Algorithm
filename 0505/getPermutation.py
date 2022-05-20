from xml.dom.minidom import CharacterData


def getPermutation(n, r) :
    alphabet = []
    for i in range(n):
        alphabet.append(chr(97 + i))
    
    result = permutation(alphabet,r)
    r_chr = []
    for i in range(len(result)):
        chra = ' '.join(s for s in result[i])
        r_chr.append(chra)
    return r_chr

def permutation(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permutation(ans, n-1):
                result.append([arr[i]] + p)
    
    return result
    

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]

    print(getPermutation(firstLine[0], firstLine[1]))

if __name__ == "__main__":
    main()
