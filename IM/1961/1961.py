# 1961. 숫자 배열 회전 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr_rotated_90 = list(zip(*arr[::-1]))
    arr_rotated_180 = list(zip(*arr_rotated_90[::-1]))
    arr_rotated_270 = list(zip(*arr))[::-1]

    print(f'#{tc}')
    for i in range(N):
        print(*arr_rotated_90[i], sep='', end=' ')
        print(*arr_rotated_180[i], sep='', end=' ')
        print(*arr_rotated_270[i], sep='')