# 17143. 낚시왕
"""
시간 제한: 1초

(0, 0)에서 출발, (0, C) 도착하면 종료
1. 오른쪽 한 칸 이동 (c열)
2. c열에서 가장 상단에 있는 상어 잡기
    - 잡은 상어는 제거
3. 상어 이동
    - 속력(s): 칸/초
    - 방향(d): 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
    - 벽 만나면 방향 전환(상하 / 좌우) + 속력 유지
        - 2 * (R(상하) 또는 C(좌우) - 1) 마다 반복
    - 한 칸에 상어 두 마리 이상인 경우, 크기(z)가 가장 큰 상어만 유효 (나머지 상어는 제거)
낚시왕이 잡은 상어 크기의 합 구하기
"""

# 격자판의 크기 R x C, 상어의 수 M
R, C, M = map(int, input())

grid = [[-1] * (C + 1) for _ in range(R + 1)]  # 격자판
sharks = {}  # 상어의 정보
for id in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    grid[r][c] = id  # 해당 좌표에 상어의 아이디 기록
    sharks[id] = [s, d, z]  # [속력, 방향, 크기]

# 방향 벡터 (정지/상/하/우/좌)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

answer = 0

# 낚시꾼의 위치 col
for col in range(1, C + 1):
    # 상어 잡기
    for row in range(1, R + 1):
        if grid[row][col] > 0:
            id = grid[row][col]
            # 잡은 상어의 크기 더하기
            answer += sharks[id][-1]
            # 잡은 상어 제거
            sharks.pop(id)
            # 격자판 초기화
            grid[row][col] = -1

    # 상어 이동
