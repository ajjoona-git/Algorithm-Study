# 20739: 고대 유적 2


def get_longest(arr, n, m):
    """주어진 nxm 크기의 배열(arr)에서 가로 방향으로 가장 긴 구조물의 길이를 반환하는 함수"""
    max_count = 0

    for r in range(n):
        c = 0  # 초기 위치
    
        while c < m:
            count = 0
            # 범위 내에서 구조물('1')을 발견하면 길이를 구한다.
            while c + count < m and arr[r][c + count] == '1':
                count += 1
            # 최대 길이 갱신
            if max_count < count:
                max_count = count
            # 다음 위치로 이동
            c += (count + 1)

    return max_count


T = int(input())
for tc in range(1, T+1):
    # NxM 배열
    N, M = map(int, input().split())
    grid = [input().split() for _ in range(N)]
    # 세로 방향 탐색을 위한 전치 행렬
    rotated_grid = list(zip(*grid))

    max_len_h = get_longest(grid, N, M)
    max_len_v = get_longest(rotated_grid, M, N)
    max_len = max(max_len_h, max_len_v)
    # 만약 구조물이 하나도 없는 경우 0을 출력한다.
    if max_len <= 1:
        max_len = 0

    print(f'#{tc} {max_len}')