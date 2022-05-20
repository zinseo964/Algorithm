def maxTriangle(triangle) :
    n = len(triangle)
    T = [[0]* (i) for i in range(1, n + 1)]
    T[0][0] = triangle[0][0]
    for x in range(1, n):
        for i in range(0, x+1):
            if i== 0:
                T[x][i] = T[x-1][i]
            elif i <= x-1:
                T[x][i] = max(T[x-1][i], T[x-1][i-1]) + triangle[x][i]
            else :
                T[x][i] = T[x-1][i-1] + triangle[x][i]
    return max(T[n-1])

def main():
    n = int(input())
    tri = []

    for i in range(n) :
        tri.append([int(v) for v in input().split()])

    print(maxTriangle(tri))

if __name__ == "__main__":
    main()
