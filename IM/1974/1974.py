# 1974. 스도쿠 검증 


def check_1to9(line):
    """주어진 리스트에 1부터 9까지 숫자가 하나씩 있는지 확인하는 함수"""
    # 1~9까지 숫자의 존재 여부를 확인하기 위한 배열
    # 인덱스와 숫자를 일치시키기 위해 길이를 10으로 했다.
    # False: 아직 존재하지 않음, True: 존재함
    check = [False] * 10

    for num in line:
        if check[num]:
            return False
        else:
            check[num] = True
    
    return True


def check_sudoku():
    """스도쿠에 겹치는 숫자가 있는지 없는지 확인하는 함수
        겹치는 숫자가 없을 경우 1, 그렇지 않을 경우 0을 반환한다."""
    
    # 가로줄 검사
    for row in sudoku:
        if not check_1to9(row):
            return 0
            
    # 세로줄 검사
    for c in range(N):
        col = []
        for r in range(N):
            col.append(sudoku[r][c])
        if not check_1to9(col):
            return 0

    # 3x3 격자 검사
    for r in range(0, N, 3):
        for c in range(0, N, 3):
            grid = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    grid.append(sudoku[i][j])
            if not check_1to9(grid):
                return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    N = 9
    sudoku = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {check_sudoku()}')

