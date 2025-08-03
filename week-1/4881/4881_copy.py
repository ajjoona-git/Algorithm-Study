T = int(input())  # 테스트 케이스의 수

def make_tuples(arr):
    '''주어진 2차원 리스트의 값을 (값, 행 인덱스, 열 인덱스) 튜플로 저장한 후,
    값의 오름차순으로 정렬하여 반환한다.'''
    n = len(arr)
    tuples = []
    for i in range(n):
        for j, value in enumerate(arr[i]):
            tuples.append((value, i, j))
    tuples.sort()
    return tuples


def sumation(numbers, i):
    '''주어진 2차원 배열(numbers)에서 시작 위치(x,y)부터 최소 합을 계산하여 반환하는 함수'''
    # 최소 합을 저장할 변수
    total = 0
    # 지금껏 고른 숫자의 수
    count = 0

    x = sorted_tuples[i][1]
    y = sorted_tuples[i][2]
    # 배열 전체에서 최소값을 찾아 연산을 시작한다.
    # for number, x, y in sorted_tuples[i:]:
    # 해당 숫자가 0으로 초기화되지 않았다면, 연산을 진행한다.
    if numbers[x][y]:
        # 숫자 합을 갱신하고,
        total += number
        # 해당 숫자의 행, 열 값을 0으로 초기화한다.
        for i in range(N):
            numbers[x][i] = 0
            numbers[i][y] = 0
        # 해당 숫자는 초기화하지 않는다.
        numbers[x][y] = number
        sumation(numbers, i+1)

    # return total
        count += 1
    # N개의 숫자를 모두 골랐다면 숫자 합을 반환한다.
    if count == N:
        return total
    
for test_case in range(1, T+1):
    N = int(input())  # 배열의 크기
    # 배열을 입력받아 2차원 리스트로 저장한다.
    numbers = [ [int(i) for i in input().split()] for _ in range(N) ]

    # 최소 숫자 합을 담을 리스트
    sums = []

    # 전체 배열을 정렬하여 튜플 형태로 저장한 리스트
    sorted_tuples = make_tuples(numbers)

    # 전체 배열을 정렬한 후에 최소값부터 반복하여 계산한다.
    for i in range(len(sorted_tuples)):
        number, x, y = sorted_tuples[i]
        numbers_copy = numbers[:]
        sum = sumation(numbers_copy, i)
        print(i, (number, x, y), sum)
        if sum != None:
            sums.append(sum)
        
    print(sums)
    
    print(f'#{test_case} {min(sums)}')