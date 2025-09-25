# 4013. 특이한 자석

from collections import deque
import sys
sys.stdin = open("sample_input.txt")


def calculate_points():
    """획득한 점수를 계산한다."""
    point = 0
    for i in range(4):
        # N극이면 0점
        if magnetics[i][0] == 0:
            continue
        # S극이면 1/2/4/8점
        else:
            point += 2 ** i
    return point


def is_attracted():
    """서로 붙어있는 날의 자성이 다른지 여부를 저장한 리스트를 반환한다."""
    attracted = [False] * 3
    for i in range(3):
        if magnetics[i][2] != magnetics[i+1][-2]:
            attracted[i] = True
    return attracted


def rotate_magnetic(mag_idx, dir):
    """자석을 1회 회전시킨다.""" 
    attracted = is_attracted()

    # 회전하는 자석 본인
    mag_dq = deque(magnetics[mag_idx])
    mag_dq.rotate(dir)
    magnetics[mag_idx] = list(mag_dq)

    # 오른쪽 자석의 회전 여부 확인
    right_idx = mag_idx
    new_dir = -1 * dir
    while right_idx < 3:
        # if magnetics[right_idx][2] == magnetics[right_idx + 1][-2]:
        if not attracted[right_idx]:
            break
        mag_dq = deque(magnetics[right_idx])
        mag_dq.rotate(new_dir)
        magnetics[right_idx] = list(mag_dq)
        right_idx += 1
        new_dir *= -1
    
    # 왼쪽 자석의 회전 여부 확인
    left_idx = mag_idx - 1
    new_dir = -1 * dir
    while left_idx > 0:
        # if magnetics[left_idx - 1][2] == magnetics[left_idx][-2]:
        if not attracted[left_idx]:
            break
        mag_dq = deque(magnetics[left_idx])
        mag_dq.rotate(new_dir)
        magnetics[left_idx] = list(mag_dq)
        left_idx -= 1
        new_dir *= -1

    print(magnetics)



T = int(input())
for tc in range(1, T+1):
    K = int(input())
    # 날의 자성은 N 극이 0 으로, S 극이 1 로 주어진다.
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    # [회전할 자석의 번호, 회전 방향]
    # 회전방향은 1 일 경우 시계방향이며, -1 일 경우 반시계방향이다.
    rotates = [list(map(int, input().split())) for _ in range(K)]
    print(magnetics)
    for mag_num, dir in rotates:
        rotate_magnetic(mag_num-1, dir)
    
    point = calculate_points()
    print(f'#{tc} {point}')
