# 2383. 점심 식사시간

"""
각 사람에게 가장 가까운 계단을 찾는다 -> 배정한다?
    - 문제 예시에서 사람 5는 1번계단이 가까운데 2번 계단으로 감.

계단은 2개로 고정.
계단을 내려가고 있는 사람은 선입선출 -> 큐
큐의 길이는 3, (계단 내려갈 때까지 남은 시간, 사람번호)를 저장하자.
    계단 내려갈 때까지 남은 시간이 0이면 dequeue
    아니면 다시 enqueue

각 사람에게 각 계단까지의 거리를 (거리, 사람번호, 계단번호) 순서로 힙큐에 저장할까
힙큐 기준 2순위도 필요하겠다. 두번째 계단까지의 거리 차를 추가하자.
힙큐에 (거리, 거리차(계단1-계단2), 사람, 계단) 넣자.
    거리가 짧고, 거리차가 큰 사람부터 pop
아닌가, 가까이에 있는 사람들이 먼저 길이가 긴 계단으로 이동해야 전체 시간이 짧아질 것 같다.

결국 완전탐색인가...
각 사람이 계단 1을 이용하는 경우, 계단 2를 이용하는 경우
    (계단까지의 거리, 계단 번호)를 리스트에 저장, 정렬
    짧은 거리부터 이동
    계단에 사람이 꽉차있으면 대기
    도착한 사람 리스트의 길이가 사람 수라면 종료
계단에 있는 사람은 따로 큐로 관리한다.
"""


def get_initial_position():
    """사람의 위치와 계단의 위치를 저장한다."""
    people = []
    stairs = []
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 1:
                people.append((x, y))

            elif grid[x][y] > 1:
                stairs.append((grid[x][y], x, y))

    return people, stairs


def calculate_distance():
    """계단까지의 거리를 계산한다."""
    distances = [[] for _ in range(M)]

    _, sx1, sy1 = stairs[0]
    _, sx2, sy2 = stairs[1]

    for idx, (px, py) in enumerate(people):
        d1 = abs(px - sx1) + abs(py - sy1)
        d2 = abs(px - sx2) + abs(py - sy2)
        distances[idx].extend([d1, d2])

    return distances


def update_stair(stair):
    """계단 상황을 업데이트한다."""
    new_stair = []

    while stair:
        left_time, idx_person = stair.pop()
        new_left_time = left_time - 1
        if new_left_time == 0:
            continue
        new_stair.append((new_left_time, idx_person))

    return new_stair


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = get_initial_position()
    M = len(people)  # 사람 수

    arrived = []  # 도착한 사람들을 저장


