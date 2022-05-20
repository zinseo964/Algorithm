from turtle import left
from unittest.util import sorted_list_difference


def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if(len(array)<= 1):
        return array
    pivot = array[0]
    left_arr = []
    right_arr = []
    result = []
    for i in range(1,len(array)):
        if(array[i] < pivot):
            left_arr.append(array[i])
        else :
            right_arr.append(array[i])
    left_arr = quickSort(left_arr)
    right_arr = quickSort(right_arr)
    left_arr.append(pivot)
    result = left_arr + right_arr


def main():
    line = [int(x) for x in input("정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))

if __name__ == "__main__":
    main()
