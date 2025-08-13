# 백준 1244. 스위치 켜고 끄기

import sys
# sys.stdin = open("input.txt")


# N: 스위치 개수
N = int(sys.stdin.readline().strip())
# switches: 스위치 초기 상태
# 켜져 있으면 '1', 꺼져있으면 '0'
switches = sys.stdin.readline().strip().split()  

# M: 학생 수
M = int(sys.stdin.readline().strip())

# M명의 학생에 대한 정보
for _ in range(M):
    # 학생의 성별 sex, 학생이 받은 수 num
    # sex: 남학생은 1로, 여학생은 2
    sex, num = map(int, sys.stdin.readline().strip().split())

    # 1. 남학생인 경우
    if sex == 1:
        # 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
        # 이때 스위치의 번호는 1부터 시작하므로 인덱스는 num-1이다.
        for i in range(num-1, N, num):
            if switches[i] == '1':
                switches[i] = '0'
            else:
                switches[i] = '1'

    # 2. 여학생인 경우
    else:
        # 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
        # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
        # 그 구간에 속한 스위치의 상태를 모두 바꾼다.
        i = 0
        while i < N:
            i += 1
            # 탐색할 좌우 인덱스
            idx_l = num - i - 1
            idx_r = num + i - 1

            # 인덱스 범위가 넘어가는 경우 탐색을 종료한다.
            if not (0 <= idx_l and idx_r < N):
                i -= 1
                break

            # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾는다.
            if switches[idx_l] == switches[idx_r]:
                continue
            # 조건에 맞지 않으면, 탐색을 종료한다.
            else:
                i -= 1
                break

        # 탐색할 좌우 인덱스
        idx_l = num - i - 1
        idx_r = num + i - 1

        # 구간에 속한 스위치의 상태를 모두 바꾼다.
        for i in range(idx_l, idx_r+1):
            if switches[i] == '1':
                switches[i] = '0'
            else:
                switches[i] = '1'
    
# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
for i in range(N):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()