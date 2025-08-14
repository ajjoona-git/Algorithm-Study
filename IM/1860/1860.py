# 1860. 진기의 최고급 붕어빵

# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 예약손님 수, M초 동안 K개의 붕어빵을 만든다.
    N, M, K = map(int, input().split())
    # reserved_time: N명의 픽업 예약 시간
    reserved_time = list(map(int, input().split()))
    # 예약시간 순으로 정렬
    reserved_time.sort()

    # 판매한 수량
    sold_stock = 0

    # 예약 손님 수만큼 붕어빵 제공 가능 여부를 판단한다.
    for i in range(N):
        # 현재 붕어빵의 수는 예약 시간동안 만든 붕어빵에서 판매수량을 뺀 값
        stock = (reserved_time[i] // M) * K - sold_stock
        
        # 판매할 붕어빵이 없다면 'Impossible'
        if stock <= 0:
            state = "Impossible"
            break
        # 판매했다면 판매한 수량 +1
        else:
            sold_stock += 1
    
    # 판매수량과 예약 손님 수가 일치하다면 'Possible'
    if sold_stock == N:
        state = "Possible"

    print(f'#{tc} {state}')