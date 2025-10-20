# 2096. 내려가기

"""
시간 제한 1초, 메모리 제한 4MB

점수 계산을 재귀호출했더니 메모리 초과 오류 발생
-> 스택으로 바꿨는데 여전히 메모리 초과 오류 발생
"""

def calculate_score_recur(curr_max, curr_min, r, c):
    """현재 위치(r, c)에서 얻을 수 있는 최대 점수, 최소 점수를 갱신한다."""
    # 종료 조건: 모든 줄을 검사했을 때
    if r == N:
        return

    # 최대 점수
    if curr_max + grid[r][c] > dp[r][c][0]:
        dp[r][c][0] = curr_max + grid[r][c]
    # 최소 점수
    if curr_min + grid[r][c] < dp[r][c][1]:
        dp[r][c][1] = curr_min + grid[r][c]

    # print(dp[r][c][0], dp[r][c][1])

    # 다음 줄로 내려간다. (c-1열 부터 c+1열 까지)
    for nc in range(c - 1, c + 2):
        if nc < 0 or nc > 2:
            continue
        calculate_score_recur(dp[r][c][0], dp[r][c][1], r + 1, nc)


def calculate_score_stack(curr_max, curr_min, sr, sc):
    """현재 위치(sr, sc)에서 출발해 얻을 수 있는 최대 점수, 최소 점수를 갱신한다."""
    stack = [(curr_max, curr_min, sr, sc)]

    while stack:
        curr_max, curr_min, r, c = stack.pop()

        # 종료 조건: 모든 줄을 검사했을 때
        if r == N:
            continue

        # 최대 점수
        if curr_max + grid[r][c] > dp[r][c][0]:
            dp[r][c][0] = curr_max + grid[r][c]
        # 최소 점수
        if curr_min + grid[r][c] < dp[r][c][1]:
            dp[r][c][1] = curr_min + grid[r][c]

        # 다음 줄로 내려간다. (c-1열 부터 c+1열 까지)
        for nc in range(c - 1, c + 2):
            if nc < 0 or nc > 2:
                continue
            stack.append((dp[r][c][0], dp[r][c][1], r + 1, nc))



N = int(input())  # 행의 수
grid = [list(map(int, input().split())) for _ in range(N)]

# 각 좌표마다 계산할 수 있는 (최대 점수, 최소 점수)를 기록한다.
dp = [[[0, 9 * N] for _ in range(3)] for _ in range(N)]

# 첫 번째 행을 순회하면서 점수를 계산한다.
for c in range(3):
    calculate_score_recur(0, 0, 0, c)
    # calculate_score_stack(0, 0, 0, c)

# dp 마지막 행에서 최대 점수, 최소 점수를 구한다.
max_score = max(dp[-1], key=lambda x: x[0])[0]
min_score = min(dp[-1], key=lambda x: x[1])[1]

print(max_score, min_score)
