# 1220. Magnetic

T = 10
for tc in range(1, T+1):
    N = int(input())  # 100
    table = [input().split() for _ in range(N)]

    # 계산 편의를 위해 시계방향으로 90도 회전
    # table의 왼쪽에 S극, 오른쪽에 N극이 위치한다.
    table_90 = list(zip(*table[::-1]))

    # 교착상태의 수 구하기
    # 공백('0') 제거 후 '2'-'1' 순서로 연속되는 경우
    count = 0
    for row in table_90:
        row_without_0 = ''.join(row).replace('0', '')
        for i in range(len(row_without_0) - 1):
            if row_without_0[i] == '2' and row_without_0[i+1] == '1':
                count += 1
        
    print(f'#{tc} {count}')
                
