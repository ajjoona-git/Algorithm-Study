T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    sum_list = []  # M개를 합한 값들을 담을 리스트
    # 입력받은 리스트를 순회하면서
    for i in range(N-M+1):
        sub_total = 0  # M개를 합한 값을 담을 변수
        for j in range(M):
            # M개를 합한 값을 계산하고, 그 값을 리스트에 담는다.
            sub_total += num_list[i+j]
        sum_list.append(sub_total)
    # M개의 합이 가장 큰 경우와 가장 작은 경우의 차이
    result = max(sum_list) - min(sum_list)
    print(f'#{test_case} {result}')