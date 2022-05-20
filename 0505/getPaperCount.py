def getPaperCount(myMap) :
    
    whiteCnt = 0
    blueCnt = 0
    white = 0
    blue = 0
    n = len(myMap)
    
    for i in range(n):
        for j in range(n) :
            if myMap[i][j] == 0:
                white += 1
            elif myMap[i][j] ==1:
                blue += 1

    if blue == n*n :
        blueCnt += 1
    elif white == n*n:
        whiteCnt += 1
        
    else :
        
        newMap1 =[]
        newMap2 =[]
        newMap3 =[]
        newMap4 =[]
        for i in range(n):
            for j in range(n):
                if i < n/2:
                    if j < n/2:
                        newMap1.append([int(myMap[i][j])])
                    else:
                        newMap2.append([int(myMap[i][j])])
                else:
                    if j < n/2:
                        newMap1.append([int(myMap[i][j])])
                    else:
                        newMap2.append([int(myMap[i][j])])
        
        val1 = getPaperCount(newMap1)
        val2 = getPaperCount(newMap2)
        val3 = getPaperCount(newMap3)
        val4 = getPaperCount(newMap4)
        
        whiteCnt = whiteCnt + val1[0] + val2[0] + val3[0] + val4[0]
        print("*",whiteCnt)
        blueCnt = blue + val1[1] + val2[1] + val3[1] + val4[1]
        print("**",blueCnt)

    return (whiteCnt, blueCnt)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    myMap = []
    for i in range(n) :
        myMap.append([int(x) for x in input().split()])

    retValue = getPaperCount(myMap)

    print(retValue[0])
    print(retValue[1])

if __name__ == "__main__":
    main()
