isize = 0

def dfs(x, y, pMap, visited):
    global isize
    visited[x][y] =1
    
    di = [(1,0),(0,1),(-1,0),(0,-1)]
    
    n = len(pMap)
    for d in di:
        nx = x+d[0]
        ny = y+d[1]
        
        if nx< 0 or ny < 0 or nx > n-1 or ny > n-1 : continue
        if pMap[nx][ny]==0: continue
        
        if not visited[nx][ny]:
            isize += 1
            dfs(nx, ny, pMap, visited)
            
            
def cadastralSurvey(pMap):
    '''
    디지털월드의 국토의 모양이 주어졌을 때, 섬의 갯수 (int) 와 각 섬의 크기들 (list)을 반환하세요.
    '''
    global isize
    
    num_island = 0
    n = len(pMap)
    
    visited = []
    
    for i in range(n):
        visited.append([0 for j in range(n)])
        
    islands_size = []
    for i in range(n):
        for j in range(n):
            if pMap[i][j] == 1 and visited[i][j] == 0:
                num_island += 1
                isize = 1
                dfs(i, j, pMap, visited)
                islands_size.append(isize)
    islands_size.sort()

    return num_island, islands_size

def read_input():
    size = int(input())
    returnMap = []
    for i in range(size):
        line = input()
        __line = []
        for j in range(len(line)) :
            __line.append(int(line[j]))
        
        returnMap.append(__line)
    return returnMap

def main():
    pMap = read_input()
    print(cadastralSurvey(pMap))

if __name__ == "__main__":
    main()

