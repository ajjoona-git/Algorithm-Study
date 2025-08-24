# 1486. 장훈이의 높은 선반

def make_powerset():
    """부분 집합을 만들고, 각 요소의 누적합을 계산하는 함수"""
    global min_diff

    # 비트마스크를 활용해 부분 집합 만들기
    for i in range(2 ** N):
        current_sum = 0
        for j in range(N):
            if i & (1<<j):  # j번째 값을 포함한다.
                current_sum += heights[j]
        # 요소의 합이 B 이상이면 min_diff를 갱신한다.
        if current_sum >= B and current_sum - B < min_diff:
            min_diff = current_sum - B
    return


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # 만들 수 있는 키의 조합 중에서
    # 그 합이 B 이상이면서, B와의 차이가 가장 작은 것
    # -> 부분 집합
    min_diff = sum(heights)
    make_powerset()
    print(f'#{tc} {min_diff}')