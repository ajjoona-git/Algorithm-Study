# 15486. 퇴사 2


"""
시간 제한 2초, 메모리 제한 512MB

1 ≤ N ≤ 1,500,000
1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000

"각 날짜별로 얻을 수 있는 최대 수익을 기록한다."

=> 시간 초과 O(N^2)
"""

N = int(input())
daily_profit = [0] * (N + 1)  # 각 날짜별로 얻을 수 있는 최대 수익을 기록한다.

# 상담 일정을 순회하면서
for day in range(N):
    term, profit = map(int, input().split())

    # 상담 종료일(end_date)을 기준으로 수익을 계산합니다.
    end_date = day + term

    # 상담 종료일이 N일 이후라면 무시합니다.
    if end_date > N:
        continue

    # 상담 종료일에 얻을 수 있는 수익을 갱신합니다.
    if daily_profit[day] + profit > daily_profit[end_date]:
        # 이후 모든 날의 최대 수익을 같이 갱신합니다.
        for d in range(end_date, N + 1):
            daily_profit[d] = daily_profit[day] + profit

    # print(daily_profit)

print(daily_profit[-1])

