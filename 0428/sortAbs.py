import math
import sys

def sortAbs(array):
    if len(array) ==1:
        return array

    mid = len(array)//2
    left = sortAbs(array[:mid])
    right = sortAbs(array[mid:])

    result = []

    leftPtr = 0
    rightPtr = 0

    while leftPtr < len(left) or rightPtr < len(right):
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf

        if abs(leftValue) < abs(rightValue):
            result.append(leftValue)
            leftPtr +=1
        else:
            result.append(rightValue)
            rightPtr +=1

    return result 

def main():
    line = [int(x) for x in input().split()]

    print(*sortAbs(line))

if __name__ == "__main__":
    main()
