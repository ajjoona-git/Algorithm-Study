T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 색칠 영역을 담을 리스트(10x10) -> 0으로 초기화
    colors = [[0] * 10 for _ in range(10)]
    
    for _ in range(N):
        # 색칠 영역을 하나씩 받아와
        color_info = list(map(int, input().split()))
        color = color_info[-1]
        # 해당하는 칸의 색깔 번호를 더한다.
        for r in range(color_info[0], color_info[2]+1):
            for c in range(color_info[1], color_info[3]+1):
                colors[r][c] += color
                    
    # 색깔 번호가 3인 칸의 수를 센다.
    result = 0
    for i in range(10):
        result += colors[i].count(3)
    print(f'#{test_case} {result}')