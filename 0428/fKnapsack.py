import sys

def fKnapsack(materials, m) :
    materials = sorted(materials, key = lambda x: x[1]/x[0],reverse=True)
    value = 0
    for i in range(len(materials)):
        if m > materials[i][0]:
            m -= materials[i][0]
            value += materials[i][1]
        elif m == materials[i][0]:
            m -= materials[i][0]
            value += materials[i][1]
            return value
        else:
            if materials[i][0] > 0:
                value += (materials[i][1]/materials[i][0])*m
            return value
    return value

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    materials = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, m))

if __name__ == "__main__":
    main()
