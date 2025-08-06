# 1970. 쉬운 거스름돈

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 거슬러 주어야 할 금액

    # 돈의 종류
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 돈의 종류별로 필요한 개수
    changes = [0] * len(moneys)
    
    # 현재 금액을 돈의 종류로 나눈 몫이 개수,
    # 현재 금액을 돈의 종류로 나눈 나머지로 현재 금액을 갱신
    for i, money in enumerate(moneys):
        changes[i] = N // money
        N = N % money

    print(f"#{test_case}")
    print(*changes)