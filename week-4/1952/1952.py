# 1952. 수영장

def calc_price(month=1, price=0):
    """각 달의 이용 게획별로 비용을 계산하고 최소 비용을 갱신한다."""
    global min_price

    # 종료 조건 1: 12월까지 모두 계산한 경우
    if month > 12:
        if min_price > price:
            min_price = price
        return
    
    # 종료 조건 2: 현재 금액이 최소 금액보다 큰 경우
    if price >= min_price:
        return
    
    # 이번달 이용 계획이 없는 경우, 다음달로 넘어간다.
    if monthly_plan[month] == 0:
        calc_price(month + 1, price)
    
    # 그렇지 않은 경우, 이번달 이용권을 구매한다.
    # 1. 1일권
    calc_price(month + 1, price + monthly_plan[month] * membership[0])
    
    # 2. 1달 이용권
    calc_price(month + 1, price + membership[1])

    # 3. 3달 이용권
    calc_price(month + 3, price + membership[2])

    # 4. 1년 이용권
    calc_price(month + 12, price + membership[3])


T = int(input())
for tc in range(1, T+1):
    # membership: 이용권 요금 (1일, 1달, 3달, 1년 순)
    membership = list(map(int, input().split()))
    # monthly_plan: 이용 계획 (0, 1월 ~ 12월)
    monthly_plan = [0] + list(map(int, input().split()))
    # is_paid: 각 달의 이용권 구매 여부를 체크
    is_paid = [0] * 13

    min_price = float('inf')
    calc_price(1, 0)

    print(f'#{tc} {min_price}')
