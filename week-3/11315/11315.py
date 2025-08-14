# 11315: 오목 판정
# Fail(93/100): 대각선을 모든 가능한 시작점에서 확인해야 한다!
# 아래 코드는 중앙을 가로지르는 대각선만 고려하고 있음.

def check_bingo():
    # 대각선
    count_diag1 = 0
    count_diag2 = 0
    for i in range(N):
        # 우하향 대각선(\)
        if grid[i][i] == 'o':
            count_diag1 += 1
        elif count_diag1 >= 5:
            return "YES"
        else:
            count_diag1 = 0
        
        # 우상향 대각선(/)
        if grid[i][N-1-i] == 'o':
            count_diag2 += 1
        elif count_diag2 >= 5:
            return "YES"
        else:
            count_diag2 = 0    

    if count_diag1 >= 5 or count_diag2 >= 5:
        return "YES"


    # 가로
    for r in range(N):
        count = 0
        for c in range(N):
            # 돌이 있는 칸이면 연속된 돌의 개수를 센다.
            if grid[r][c] == 'o':
                count += 1
            # 돌이 없는 칸이면 연속된 돌이 5개 이상인지 확인한다.
            elif count >= 5:
                return "YES"
            # 돌의 개수를 초기화한다.
            else:
                count = 0
        # 마지막이 'o'로 끝나는 경우
        if count >= 5:
            return "YES"
        

    # 세로
    for c in range(N):
        count = 0
        for r in range(N):
            # 돌이 있는 칸이면 연속된 돌의 개수를 센다.
            if grid[r][c] == 'o':
                count += 1
            # 돌이 없는 칸이면 연속된 돌이 5개 이상인지 확인한다.
            elif count >= 5:
                return "YES"
            # 돌의 개수를 초기화한다.
            else:
                count = 0
        # 마지막이 'o'로 끝나는 경우
        if count >= 5:
            return "YES"
        

    # 가로, 세로, 대각선 모두 오목이 완성되지 않았다면, 'NO' 반환
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [input() for _ in range(N)]

    print(f'#{tc} {check_bingo()}')