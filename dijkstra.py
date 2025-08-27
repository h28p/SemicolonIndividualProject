# 백준 1753번 풀이 (최단 거리, G5)

# 기본 설정
from sys import stdin
from heapq import *

input = stdin.readline

# 입력

V, E = map(int, input().split())
K = int(input())
# 인접 리스트 : graph[v]에 v와 연결된 정점 모두 저장
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    

# 메인 코드

INF = 10**9
dist = [INF] * (V+1)
dist[K] = 0
# heap 생성
q = []
heappush(q, (0, K))

# heap의 길이가 0이면 종료
while q:
    # heap에서 최솟값 pop
    d, p = heappop(q)
    # 갱신되어 p까지의 거리가 heap에 있던 값과 다르면 패스
    if dist[p] != d:
        continue
    # p와 연결된 모든 정점에 대해 반복
    for v, w in graph[p]:
        # 갱신되는 경우 (직접 가는 것보다 거쳐 가는 것이 빠른 경우)
        # dist 배열을 갱신하고 heap에 갱신된 값 추가
        if dist[v] > d + w:
            dist[v] = d+w
            heappush(q, (d+w, v))

# 출력
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:

        print(dist[i])
