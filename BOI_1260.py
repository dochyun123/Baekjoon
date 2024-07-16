# BFS, DFS
from collections import deque

N, M, V = map(int, input().split())
graph = {}
for i in range(1,N+1):
    graph[i]=[]

for _ in range(M):
    m,n = map(int,input().split())
    graph[m].append(n)

def BFS(start,graph):
    q=deque()
    q.append(start)
    visited = {start : True}
    while q:
        cur_n = q.popleft()
        print(cur_n,end = ' ')
        for next_n in graph[cur_n]:
            if next_n not in visited:
                q.append(next_n)
                visited[next_n]= True
    return visited

def DFS(start,graph):
    visited={}
    visited[start] = True
    print(start,end=' ')
    for next_n in graph[start]:
        if next_n not in visited:
            DFS(next_n,graph)



def dfs(cur_v,graph):
    visited = {}
    visited[cur_v] = True
    print(cur_v,end = ' ')
    for next_v in graph[cur_v]:
        if next_v :
            if next_v not in visited:
                dfs(next_v,graph)
    return visited

print(dfs(V,graph))

# DFS(V,graph)
# BFS(V,graph)


# def bfs(graph,start_v):
#     q = deque()
#     q.append(start_v) # 예약
#     visited = {start_v: True}   # 방문표시
#     while q:
#         cur_v = q.popleft()
#         print(cur_v,end = ' ')
#         for next_v in graph[cur_v]:
#             if next_v not in visited:
#                 q.append(next_v)
#                 visited[next_v] = True
#     return visited



# visited = {}
# bfs(graph,V)
# dfs(V)
