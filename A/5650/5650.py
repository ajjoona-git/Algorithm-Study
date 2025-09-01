# 5650. 핀볼 게임

import sys
sys.stdin = open("sample_input.txt")
from pprint import pprint


# 블록 번호별로 델타 인덱스 순서대로 블록에 접근했을 때 변하는 방향
# 인덱스는 현재 진행 중인 방향, 값은 튕겨져 나가는 방향
blocks = {
    1: [1, 3, 0, 2],  # 하, 우, 상, 좌
    2: [3, 0, 1, 2],  # 우, 상, 하, 좌
    3: [2, 0, 3, 1],  # 좌, 상, 우, 하
    4: [1, 2, 3, 0],  # 하, 좌, 우, 상
    5: [1, 0, 3, 2],  # 하, 상, 우, 좌
}


# 방향 탐색 순서 (상하좌우 순)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_wormholes(arr, n):
    """주어진 게임판에서 웜홀(6~10)의 위치를 저장해 딕셔너리 형태로 반환하는 함수"""
    # 웜홀의 위치를 찾아 저장한다.
    wormholes = {}
    for r in range(n):
        for c in range(n):
            if 6 <= arr[r][c] <= 10:
                wormholes.setdefault(arr[r][c], [])
                wormholes[arr[r][c]].append((r, c))
    
    # 저장된 웜홀의 위치들은 2개씩이므로 각각의 위치쌍을 별도로 저장한다.
    wormhole_pair = {}
    for loc in wormholes.values():
        wormhole_pair[loc[0]] = loc[1]
        wormhole_pair[loc[1]] = loc[0]

    return wormhole_pair


def get_score(arr, r, c):
    """주어진 게임판에서 (r,c)를 시작점으로 할 때의 최대 점수를 반환하는 함수"""
    max_score = 0

    # 상하좌우 네 방향 탐색
    for i in range(4):
        score = 0
        nr, nc = r + delta[i][0], c + delta[i][1]

        while True:
            # 벽이면 방향 전환, score +1
            # if not (0 <= nr < N and 0 <= nc < N):
            #     nr -= delta[i][0]
            #     nc -= delta[i][1]
            #     i = blocks.get('wall')[i]
            #     score +1
            #     continue

            # 종료 조건
            # 출발 위치로 돌아오거나 블랙홀(-1)에 빠지기 전까지 반복
            if (nr, nc) == (r, c) or arr[nr][nc] == -1:
                # 최대 점수 갱신
                max_score = max(max_score, score)   
                break

            # 0이면 통과
            # elif arr[nr][nc] == 0:
            #     pass
            
            # 1~4이면 blocks 방향 전환, score +1
            elif 1 <= arr[nr][nc] <= 4:
                i = blocks.get(arr[nr][nc])[i]
                score += 1

            # 5(혹은 벽)이면 지금까지의 점수 *2하고 출발위치로 돌아감
            # 현재까지의 루트를 되돌아갈 것이기 때문이다.
            elif arr[nr][nc] == 5:
                score = score * 2 + 1
                nr, nc == r, c
                continue

            # 6~10이면 wormhole_pair 위치 변경
            elif 6 <= arr[nr][nc] <= 10:
                nr, nc = wormhole_pair.get((nr, nc))
                continue

            nr, nc = nr + delta[i][0], nc + delta[i][1]
        

    return max_score


T = int(input())
for tc in range(1, 1+1):
    N = int(input())
    # 벽과 5번 블록의 역할이 같으므로, grid의 외곽을 5로 패딩해준다.
    grid = [[5] + list(map(int, input().split())) + [5] for _ in range(N)]
    grid.insert(0, [5] * (N + 2))
    grid.append([5] * (N + 2))

    # 웜홀 찾기
    wormhole_pair = find_wormholes(grid, N+2)

    max_score = 0

    # 게임판에서 0인 모든 공간에서 점수 계산
    for r in range(1, N+1):
        for c in range(1, N+1):
            if grid[r][c] == 0:
                local_max_score = get_score(grid, r, c)
                print(local_max_score)
                max_score = max(max_score, local_max_score)
    
    print(f'#{tc} {max_score}')