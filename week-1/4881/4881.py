T = int(input())  # 테스트 케이스의 수

def resize(arr, i, j):
    '''주어진 배열(arr)에서 주어진 행(i)과 열(j)을 삭제한 배열을 반환한다.'''
    if len(arr) <= 1:
        return []
    
    # 원본 배열을 복사하여 진행한다.
    resized_arr = arr[:]
    # 행을 제거한다.
    del resized_arr[i]
    # 열을 제거하기 위해 행렬을 바꾼다.
    resized_arr = list(map(list, zip(*resized_arr)))
    # 행을 제거한다.
    del resized_arr[j]
	# 다시 원상복귀한다.
    resized_arr = list(map(list, zip(*resized_arr)))

    return resized_arr


def find_minimum(arr):
    '''주어진 2차원 배열(arr)의 최소값의 인덱스를 반환하는 함수
    이때 각 행별 최대값과 최소값의 크기가 가장 큰 행의 최소값을 반환한다.
    '''
    # n = len(arr)  # 배열의 크기
    # # 최소 값을 담을 변수를 초기화한다.
    # min_value = arr[0][0]
    # x, y = 0, 0

    # # 배열을 순회하면서
    # for i in range(n):
    #     for j in range(n):
    #         # 현재 값이 최소 값보다 작다면
    #         if arr[i][j] < min_value:
    #             # 최소값을 갱신하고 인덱스를 저장한다.
    #             min_value = arr[i][j]
    #             x, y = i, j
    
    x = arr.index(max(arr, key=lambda x: max(x) - min(x)))
    min_value = min(arr[x])
    y = arr[x].index(min_value)

    return min_value, x, y


for test_case in range(1, T+1):
    N = int(input())  # 배열의 크기
    # 배열을 입력받아 2차원 리스트로 저장한다.
    numbers = [ [int(i) for i in input().split()] for _ in range(N) ]

    # 최소 숫자 합을 담을 리스트
    sums = []


    min_sum = 0
    while numbers:
        # # 종료 조건: 배열의 크기가 0이면 연산을 종료한다.
        # if len(numbers) == 0:
        #     break

        # 최소 값을 찾는다.
        min_num, x, y = find_minimum(numbers)
        
        # 숫자를 하나 택하면 숫자 합을 갱신하고,
        min_sum += min_num
        # 해당 숫자의 행,열을 삭제한 N-1xN-1 크기의 배열을 생성한다.
        numbers = resize(numbers, x, y)

        # 종료 조건: min_sum 값이 최소 합보다 커지면 연산을 종료한다.
        # if min_sum > min(sums):
        #     break
    else:
        # 연산을 끝까지 마쳤다면 sums 리스트에 값을 저장한다.
        sums.append(min_sum)
    
    print(f'#{test_case} {min(sums)}')