# 2805. 농작물 수확하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        row = [int(i) for i in input()]
        farm.append(row)

    # 대칭의 중심이 되는 인덱스
    center = N // 2
    # 총 수익
    profit = 0

    # center까지 폭을 늘려나가면서 합산한다.
    for i in range(center):
        for j in range(center - i, center + i + 1):
            profit += farm[i][j]
    # center이후로는 폭을 줄여가면서 합산한다.
    for i in range(center, N):
        for j in range(i - center, N - i + center):
            profit += farm[i][j]
    
    print(f'#{tc} {profit}')
            
