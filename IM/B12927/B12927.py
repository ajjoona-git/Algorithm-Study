# 백준 12927. 배수 스위치

import sys
# sys.stdin = open("input.txt")


def flip_switch(i):
    """i번 스위치를 눌렀을 때의 변화를 나타내는 함수
    i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다."""
    for j in range(i, N+1, i):
        if switches[j] == 'Y':
            switches[j] = 'N'
        else:
            switches[j] = 'Y'


# switches: 스위치 초기 상태
# 켜져 있으면 'Y', 꺼져있으면 'N'
# 인덱스와 스위치 번호를 맞추기 위해 0번 인덱스에 무의미한 값(1)을 패딩
switches = [1] + [i for i in sys.stdin.readline().strip()]

# N: 스위치의 개수 (1 ~ N번 스위치까지 존재)
N = len(switches) - 1

# 스위치를 누른 횟수
count = 0

# i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.
for i in range(1, N+1):
    if switches[i] == 'Y':
        count += 1
        flip_switch(i)
    else:
        continue

print(count)