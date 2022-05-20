import sys

def maxSlope(points) :
    points.sort()
    l = len(points)
    result = []
    for i in range(0,l-1):
        dx = points[i+1][0] - points[i][0]
        dy = points[i+1][1] - points[i][1]
        if(dx != 0):
            result.append(abs(dy/dx))
        else : 
            result.append(0)
    return max(result)

def main():

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % maxSlope(points))

if __name__ == "__main__":
    main()
