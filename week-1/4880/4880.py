# 4880. 토너먼트 카드게임

T = int(input())  # 테스트 케이스의 수

def who_is_winner(a, b):
    '''
    주어진 두 카드 인덱스(a, b)의 숫자를 비교하여 승자를 반환한다.
    카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
    숫자가 같은 경우(비긴 경우), 인덱스가 작은 값을 반환한다.
    a b 승자(a-b)
    1 2 b(-1)
    1 3 a(-2)
    2 3 b(-1)
    2 1 a(1)
    3 1 b(2)
    3 2 a(1)
    '''
    if cards[a] - cards[b] == -1:
        return b
    elif cards[a] - cards[b] == 2:
        return b
    else:
        return a

def cut_in_half(i, j):
    '''반복해서 그룹을 반으로 나눔 -> 재귀 함수
    주어진 인덱스 범위에서 그룹을 반으로 나누면서 승자를 반환한다.
    그룹이 1명이 되면 양 쪽의 카드를 비교한다.
    '''
    if j - i <= 1:
        return who_is_winner(i, j)
    
    a = cut_in_half(i, (i+j)//2)
    b = cut_in_half((i+j)//2+1, j)

    return who_is_winner(a,b)
    

for test_case in range(1, T+1):
    N = int(input())  # 전체 인원 수
    # 전체 인원의 카드를 저장할 리스트
    cards = list(map(int, input().split()))
    

    # 승자를 찾는다.
    # 이때 학생은 1번부터 시작하므로 인덱스에 +1을 해준다.
    winner = cut_in_half(0,N-1) + 1

    print(f'#{test_case} {winner}')
    