# 5650. 핀볼 게임


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


def find_wormholes(arr, N):
    """주어진 게임판에서 웜홀(6~10)의 위치를 저장해 딕셔너리 형태로 반환하는 함수"""
    # 웜홀의 위치를 찾아 저장한다.
    wormholes = {}
    for r in range(N):
        for c in range(N):
            if 6 <= arr[r][c] <= 10:
                wormholes.setdefault(arr[r][c], [])
                wormholes[arr[r][c]].append((r, c))
    
    # 저장된 웜홀의 위치들은 2개씩이므로 각각의 위치쌍을 별도로 저장한다.
    wormhole_pair = {}
    for loc in wormholes.values():
        wormhole_pair[loc[0]] = loc[1]
        wormhole_pair[loc[1]] = loc[0]

    return wormhole_pair


def get_score(arr, N, r, c):
    """주어진 게임판에서 (r,c)를 시작점으로 할 때의 최대 점수를 반환하는 함수"""
    max_score = 0
    # 상하좌우 네 방향 탐색
    for i in range(4):
        score = 0
        # 출발 위치로 돌아오거나 블랙홀(-1)에 빠지기 전까지 반복
            nr, nc = r + delta[i][0], c + delta[i][1]
            # 0이면 통과
            # 1~5이면 blocks 방향 전환
            # 6~10이면 wormhole_pair 위치 변경

    return max_score