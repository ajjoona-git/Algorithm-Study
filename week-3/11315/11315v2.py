# 11315: 오목 판정
# 델타 이용 -> PASS

def find_five_stones():
    # 가로, 세로, 대각선으로 탐색하기 위한 델타 (우, 우하, 하, 좌하 순)
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]

    # 현재 위치 (r, c)
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 'o':
                # i: 방향 변경을 위한 인덱스
                for i in range(4):
                    count = 1
                    # k: 탐색 횟수 (다섯 개 연속하는 경우가 최대임)
                    for k in range(1, 5):
                        nr = r + dr[i] * k
                        nc = c + dc[i] * k
                        # 벽 체크 & 돌이 있다면 count +1
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 'o':
                            count += 1
                        # 현재 방향으로의 탐색을 중지한다.
                        else:
                            break
                    # 탐색을 끝까지 마쳤다면 (count == 5) "YES" 반환
                    else:
                        return "YES"
                    
    # "YES"를 반환하지 못한 채로 탐색을 마쳤다면 "NO" 반환
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [input() for _ in range(N)]

    print(f'#{tc} {find_five_stones()}')