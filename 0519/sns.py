import sys
from collections import deque
sys.setrecursionlimit(100000)

def SNS(n_nodes, myInput, a, b):
    '''
    엘리스친구의 친구관계가 myInput으로 주어지고, 사용자 a, b가 주어질 때 둘 사이의 촌수를 반환합니다.
    '''
    if a == b : return 0
    
    graph = [[] for i in range(n_nodes)]
    m_edges = len(myInput)
    
    for line in myInput:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
        
    queue = deque([a])
    visit = [0] * n_nodes

    visit[a] = 1

    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if visit[node] == 0:
                visit[node] = visit[cur] + 1
                queue.append(node)
    return visit[b] -1 if visit[b] > 0 else -1

def main():
    '''
    아래 코드를 수정하지 마시오.
    '''
    
    n_nodes, m_edges = input().split()
    n_nodes = int(n_nodes)
    m_edges = int(m_edges)
    
    a, b = input().split()
    a = int(a)
    b = int(b)

    myInput = []

    for i in range(m_edges) :
        line = [int(x) for x in input().split()]
        myInput.append(line)
    
    print(SNS(n_nodes,myInput,a,b))

if __name__ == "__main__":
    main()
