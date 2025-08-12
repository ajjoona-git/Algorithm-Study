# 22375. 스위치 조작

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    switches = list(map(int, input().split()))  # 초기 상태
    final_status = list(map(int, input().split()))  # 조작 후 상태

    count = 0  # 조작 횟수

    # switches를 순회하면서
    for i in range(N):
        # final_status와 다르면 스위치를 on/off 한다.
        if switches[i] != final_status[i]:
            count += 1
            for j in range(i, N):
                # 0이었다면 1, 1이었다면 0으로 바꿔준다.
                switches[j] = (switches[j] + 1) % 2

    print(f'#{tc} {count}')