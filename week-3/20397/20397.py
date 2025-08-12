# 20397: 돌 뒤집기 게임 2 

T = int(input())
for tc in range(1, T+1):
    # 돌의 수 N, 뒤집기 횟수 M
    N, M = map(int, input().split())
    # 돌의 초기상태
    stones = input().split()

    # M번 뒤집는다.
    for _ in range(M):
        i, j = map(int, input().split())

        # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 
        # 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
        # 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
        for step in range(1, j+1):
            # 마주보는 돌의 인덱스
            idx_l = i - step - 1
            idx_r = i + step - 1

            # 범위 체크
            if 0 <= idx_l < N and 0 <= idx_r < N:
                if stones[idx_l] == '1' and stones[idx_r] == '1':
                    stones[idx_l] = '0'
                    stones[idx_r] = '0'
                elif stones[idx_l] == '0' and stones[idx_r] == '0':
                    stones[idx_l] = '1'
                    stones[idx_r] = '1'
            else:
                break
        
    print(f'#{tc}', *stones)

        