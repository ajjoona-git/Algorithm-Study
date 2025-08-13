# 1959: 두 개의 숫자열

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    max_sum = 0  # 최대값

    # 1. N < M
    if N < M:
        b_idx = M - N
        for j in range(b_idx+1):  # b_list의 인덱스
            total = 0
            for i in range(N):  # a_list의 인덱스
                total += a_list[i] * b_list[j+i]
            # 최대값 갱신
            if max_sum < total:
                max_sum = total
    
    # 2. N > M
    elif N > M:
        a_idx = N - M
        for i in range(a_idx+1):  # a_list의 인덱스
            total = 0
            for j in range(M):  # b_list의 인덱스
                total += a_list[i+j] * b_list[j]
            # 최대값 갱신
            if max_sum < total:
                max_sum = total
    
    # 3. N == M
    else:
        total = 0
        for i in range(N):
            total += a_list[i] * b_list[i]
        if max_sum < total:
            max_sum = total

    print(f'#{tc} {max_sum}')