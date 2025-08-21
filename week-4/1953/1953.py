# 1953. 탈주범 검거
"""
테스트 케이스 1/5 -> 터널이 연결되는 경우를 생각 안해서 틀림!
ex. +| 이런 식으로 터널이 있을 경우
    +에서는 옆으로 가는걸 카운트 하지만, 실제로는 못 감.
=> connected 딕셔너리 추가해서 보완.
"""

import sys
sys.stdin = open("sample_input.txt")


# delta: 상, 하, 좌, 우 이동을 위한 델타
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# tunnels: 터널 구조물 타입별로 이동가능한 델타 인덱스를 저장함
tunnels = {
    '1': [0, 1, 2, 3],  # 상하좌우
    '2': [0, 1],  # 상하
    '3': [2, 3],  # 좌우
    '4': [0, 3],  # 상우
    '5': [1, 3],  # 하우
    '6': [1, 2],  # 하좌
    '7': [0, 2],  # 상좌
}

# connected: 상하좌우로 이동했을 때 연결가능한 터널 구조물 타입
connected = {
    0: ['1', '2', '5', '6'],  # 상
    1: ['1', '2', '4', '7'],  # 하
    2: ['1', '3', '4', '5'],  # 좌
    3: ['1', '3', '6', '7'],  # 우
}


T = int(input())
for tc in range(1, T+1):
    # N x M: 지하 터널 지도의 크기
    # (R, C): 맨홀 뚜껑의 위치(= 탈출 1시간 후의 위치)
    # L: 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())

    # after_escape: 탈출 후 경과된 시간
    after_escape = 1
    # possible: 탈주범이 은신할 수 있는 장소 (중복 제거를 위해 set로 지정함)
    possible = set()

    # underground: 지하 터널 지도 (NxM)
    underground = [input().split() for _ in range(N)]


    while after_escape <= L:
        # 현시간에 이동가능한 장소를 리스트 형태로 저장한다.
        visited = []

        # 1시간 후의 위치는 맨홀 뚜껑의 위치
        if after_escape == 1:
            visited.append((R, C))
        else:
            # one_hour_ago를 순회하면서 이동 가능한 장소를 탐색한다.
            for x, y in one_hour_ago:
                # (x, y)의 터널 구조물 타입의 이동 가능한 장소
                for i in tunnels.get(underground[x][y]):
                    nx = x + delta[i][0]
                    ny = y + delta[i][1]
                    # (nx, ny)가 지하 터널 지도 범위 안에 있으면서 방문하지 않았고 연결된 터널이면, visited에 추가
                    if(
                        0 <= nx < N and 0 <= ny < M
                        and (nx, ny) not in possible
                        and underground[nx][ny] in connected[i]
                    ):
                        visited.append((nx, ny))
                        
        # 은신 가능한 장소에 추가
        possible.update(visited)
        # 1시간 경과
        after_escape += 1
        one_hour_ago = visited[:]

    print(f'#{tc} {len(possible)}')