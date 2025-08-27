# 1949. 등산로 조성

def explore_path(r, c, curr_h, path_len, chance=True):
    """가장 긴 등산로를 찾아 길이를 반환하는 함수
    - Args
        (r, c): 현재 위치
        curr_h: 현재 위치의 높이
        path_len: 현재까지 등산로의 길이
        chance: 공사 가능 여부, True(가능) / False(불가능)
    """
    global max_path_len
    # 현위치의 방문 표시
    visit[r][c] = 1

    # 4방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 벽 체크, 방문 체크
        if not (0 <= nr < N and 0 <= nc < N) or visit[nr][nc] == 1:
            continue

        # 1. 현위치보다 낮은 지형이라면 ㄱㄱ
        if grid[nr][nc] < curr_h:
            explore_path(nr, nc, grid[nr][nc], path_len + 1, chance)
            # visit[nr][nc] = 0

        # 2. 현위치보다 높거나 같은데, chance가 살아있고 K가 충분하다면 공사 진행시켜
        elif chance and K > (grid[nr][nc] - curr_h):
            # 현재 높이보다 1만큼 작은 높이만큼 깎는다.
            explore_path(nr, nc, curr_h - 1, path_len + 1, False)
            chance = True
    
    # 백트래킹을 위해 현위치에 대한 방문 정보 초기화
    visit[r][c] = 0

    # 등산로의 최대 길이 갱신
    if path_len > max_path_len:
        max_path_len = path_len

    return


def find_highest():
    """가장 높은 봉우리의 위치를 반환하는 함수"""
    max_height = {'height': 0, 'loc': []}
    
    for r in range(N):
        for c in range(N):
            # 최대 높이보다 높을 경우, height와 loc 모두 갱신
            if grid[r][c] > max_height['height']:
                max_height['height'] = grid[r][c]
                max_height['loc'] = [(r, c)]
            # 최대 높이와 같을 경우, loc에 현위치 추가
            elif grid[r][c] == max_height['height']:
                max_height['loc'].append((r, c))
    
    return max_height['height'], max_height['loc']


# 상하좌우 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 탐색을 위한 초기화
    visit = [[0] * N for _ in range(N)]
    max_path_len = 0

    # 가장 높은 봉우리(시작점) 정보
    max_h, start_points = find_highest()
    for r, c in start_points:
        explore_path(r, c, max_h, 1, True)

    print(f'#{tc} {max_path_len}')