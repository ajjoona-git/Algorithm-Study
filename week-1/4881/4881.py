T = int(input())  # 테스트 케이스의 수

def sumation(x, subtotal):
    '''
    주어진 행(x)에서 숫자를 하나 택하여 연산을 시작한다.
    현재까지의 합(subtotal)이 최소 합(min_sum)보다 커지면 연산을 종료한다.
    선택한 숫자의 행과 열의 visited를 True로 바꾸고, 현재까지의 합을 갱신한다.
    '''
    global min_sum
    
    # 종료 조건1: 현재까지의 합(subtotal)이 최소 합(min_sum)보다 커지면 연산을 종료한다.
    if subtotal >= min_sum:
        return
    
    # 종료 조건2: 모든 행의 숫자를 택했다면 연산을 종료한다.
    if x == N:
        # min_sum을 갱신한다.
        min_sum = subtotal
        return
        
    # 해당 행의 모든 열을 순회하면서
    for y in range(N):
        # visited == False이면,
        if not visited[y]:
            # 숫자를 택하고 연산을 계속한다.
            visited[y] = True
            sumation(x+1, subtotal + numbers[x][y])
            # 연산을 진행하다가 종료 조건으로 탈출하지 못한 경우
            # 다른 숫자를 택하기 위해 visited를 False로 바꿔준다.
            visited[y] = False

            
for test_case in range(1, T+1):
    N = int(input())  # 배열의 크기
    # 배열을 입력받아 2차원 리스트로 저장한다.
    numbers = [ [int(i) for i in input().split()] for _ in range(N) ]

	# 선택한 숫자의 열을 선택하지 않기 위한 리스트
    # 행은 중복해서 선택하지 않으므로 생략한다.
    visited = [False] * N
	
    # 배열 최소 합을 초기화한다.
    min_sum = float("inf")
    
    # 첫번째 행부터 연산을 시작한다.
    sumation(0,0)
    
    # 결과 출력
    print(f'#{test_case} {min_sum}')