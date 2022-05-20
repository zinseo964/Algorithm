def sortAbs(array):
    
    if len(array)<= 1:
        return array
        
    pivot = array[0]
    left = getSmall(array[1:],pivot)
    right= getLarge(array[1:],pivot)

    return sortAbs(left)+[pivot]+sortAbs(right)
    
def getSmall(array,pivot):
    data = []
    for a in array:
        if abs(a)<= abs(pivot):
            if abs(a)==abs(pivot):
                if a <= pivot:
                    data.append(a)
            else:
                data.append(a)   
    return data
    
def getLarge(array,pivot):
    data = []
    for a in array:
        if abs(a)>= abs(pivot):
            if abs(a)==abs(pivot):
                if a > pivot:
                    data.append(a)
            else:
                data.append(a)
    return data

def main():
    line = [int(x) for x in input().split()]

    print(*sortAbs(line))

if __name__ == "__main__":
    main()
