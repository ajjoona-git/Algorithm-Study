# 1486. 장훈이의 높은 선반
# 조합으로 풀기

import itertools

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # 만들 수 있는 키의 조합 중에서
    # 그 합이 B 이상이면서, B와의 차이가 가장 작은 것
    # -> 조합
    min_diff = sum(heights)
    
    # 조합은 개수를 지정해야 한다.
    for i in range(1, N+1):
        for combo in itertools.combinations(heights, i):
            if sum(combo) >= B and sum(combo) - B < min_diff:
                min_diff = sum(combo) - B 

    print(f'#{tc} {min_diff}')