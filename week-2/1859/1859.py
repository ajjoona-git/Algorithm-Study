# 1859. 백만 장자 프로젝트

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 기간
    prices = list(map(int, input().split()))  # N일 간의 매매가

    # 마지막 날의 값을 최대값으로 초기화한다.
    max_price = prices[-1]
    profit = 0  # 최대 이익

    # 마지막 날의 매매가부터 순회하면서
    for i in range(N-2, -1, -1):
        # 현재값이 최대값보다 크다면
        if prices[i] > max_price:
            # 최대값을 갱신한다.
            max_price = prices[i]
        # 현재 값이 최대값보다 작거나 같다면
        else:
            # 최대값과 현재값의 차액만큼 이익에 추가한다.
            profit += max_price - prices[i]

    # 결과를 출력한다.
    print(f'#{test_case} {profit}')