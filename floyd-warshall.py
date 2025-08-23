# 백준 11404번 풀이 (플로이드, G4)

# 기본 설정
from sys import stdin
input = stdin.readline

# 입력
N = int(input())
M = int(input())

INF = 2147483647
dist = [[INF] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()