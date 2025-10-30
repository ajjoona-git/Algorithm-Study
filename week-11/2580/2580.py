# 2580. 스도쿠

"""
시간 제한 1초, 메모리 제한 256MB
(런타임에러: AttributeError)

1. 구간별로 탐색
    각 행과 열에 없는 숫자 확인
    3*3 크기 안에 없는 숫자 확인
    빈칸에 가능한 숫자들 메모 (예: {(0, 2): {1, 2, 6}, ...})
    -> 모든 칸을 순회한 뒤에 후보가 1개인 칸부터 채워나감
    -> 채워진 칸의 행,열,구간에 대해서 해당 숫자 삭제

2. 숫자별로 탐색
    행, 열에 해당 숫자가 있는지 확인 -> 후보군에서 제외
    예: {1: {'row': {0,1,2,3,4,...}, 'col': {0,1,2,3,4,...}, 'box': {0,1,2,3,4,...}}, ...}
"""


board = [list(map(int, input().split())) for _ in range(9)]

# 각 빈칸에 가능한 숫자들을 메모한다.
memo = {}

def check_row(r):
    """해당 행에서 비어있는 숫자를 set 형태로 변환한다."""
    used = set(range(1, 10))
    return used.difference(set(board[r]))

def check_col(c):
    """해당 열에서 비어있는 숫자를 set 형태로 변환한다."""
    used = set(range(1, 10))
    for i in range(9):
        if board[i][c] != 0:
            used.remove(board[i][c])
    return used

def check_box(r, c):
    """해당 3x3 정사각형에서 비어있는 숫자를 set 형태로 변환한다."""
    r_start = (r // 3) * 3
    c_start = (c // 3) * 3

    used = set(range(1, 10))
    for i in range(r_start, r_start + 3):
        for j in range(c_start, c_start + 3):
            if board[i][j] != 0:
                used.remove(board[i][j])
    return used

def decide_number(r, c):
    """빈칸(r, c)을 채우거나, 후보군(memo)에 저장한다."""
    # 가능한 숫자 목록을 찾고
    candidates = check_row(r) & check_col(c) & check_box(r, c)
    # 그게 1개라면
    if len(candidates) == 1:
        # 바로 적용한다.
        board[r][c] = candidates.pop()
    # 아니라면
    else:
        # memo에 저장한다.
        memo[(r, c)] = candidates


# 1회차 순회
for r in range(9):
    for c in range(9):
        # 빈칸에 대해서
        if board[r][c] == 0:
            decide_number(r, c)

# 후보 숫자 개수를 기준으로 오름차순 정렬
memo = sorted(memo, key=lambda x: len(x.value()))

# 빈 칸이 남아있는 동안 계속 순회
while memo:
    (r, c), numbers = memo.pop()
    decide_number(r, c)

# 결과 출력
for row in board:
    print(*row)