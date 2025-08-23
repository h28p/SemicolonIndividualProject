# 백준 1753번 풀이 (최단 거리, G5)

# 기본 설정
from sys import stdin
from heapq import *

input = stdin.readline

# 입력
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 메인 코드
INF = 10**9
dist = [INF] * (V+1)
dist[K] = 0

q = []
heappush(q, (0, K))

while q:
    d, p = heappop(q)

    if dist[p] != d:
        continue

    for v, w in graph[p]:
        if dist[v] > d + w:
            dist[v] = d+w
            heappush(q, (d+w, v))

# 출력
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])