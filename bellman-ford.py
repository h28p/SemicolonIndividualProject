# 백준 11657번 풀이 (타임머신, G4)

# 기본 설정
from sys import stdin
input = stdin.readline

# 입력

N, M = map(int, input().split())
graph = []
INF = 10**8
dist = [INF] * (N+1)
dist[1] = 0
isLoopExist = False
# 리스트에 간선을 차례대로 저장
for i in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

# 메인 코드

for i in range(1, N+1):
    # N-1번 반복 : 모든 간선에 대해 갱신하기 -> 전부 갱신됨
    if i < N:
        for u, v, w in graph:
            if dist[u] != INF:
                dist[v] = min(dist[v], dist[u]+w)
    # N번째 : 이때도 갱신되면 음수 사이클이 존재함 -> 최단거리 계산 불가능
    else:
        for u, v, w in graph:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = -INF
                isLoopExist = True
                break

# 출력
if isLoopExist:
    print(-1)
else:
    for i in dist[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)


