# 2636. 치즈

"""
시간 제한: 1초, 메모리 제한: 128MB

줄기세포배양 문제랑 비슷한 듯
치즈는 점점 작아지기 때문에 2차원 리스트에 풀이하면 비효율적임

1. 치즈가 있는 좌표를 모두 set에 저장 -> cheese
2. 최외각 치즈 좌표를 모두 set에 저장 -> melting
3. bfs
    델타 탐색하면서 녹은 치즈(melting)의 주변 치즈를 별도로 저장 -> (시간, 좌표)
"""
from collections import deque

N, M = map(int, input().split())

# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1
grid = [list(map(int, input().split())) for _ in range(N)]

# 치즈가 있는 좌표를 저장한다.
cheese = set()
for r in range(N):
    for c in range(M):
        if grid[r][c] == 1:
            cheese.add((r, c))

# 최외각 치즈 좌표를 저장한다.
# 어떻게 하지..??

