import sys

def reservation(meetingList) :
    meetingTime = sorted(meetingList, key = lambda x: x[0],reverse=False)
    room = []
    for i in range(len(meetingTime)):
        if i == len(meetingList):
            return len(room)

        t = meetingTime[i][1]

        for k in range(i+1,len(meetingTime)):
            if t <= meetingTime[k][0]:
                t = meetingTime[k][1]
                meetingList.remove(meetingTime[k])

        room.append((meetingTime[i][0],t))
        meetingTime = meetingList

    return len(room)
    

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    meetingList = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        meetingList.append( (data[0], data[1]) )

    print(reservation(meetingList))

if __name__ == "__main__":
    main()
