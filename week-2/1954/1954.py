# 1954. 달팽이 숫자

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 달팽이의 크기
    snail = [ [0] * N for _ in range(N) ]  # 달팽이 초기화

    x, y = 0, 0  # 탐색 위치 초기화
    number = 1  # 할당할 숫자 초기화
    snail[x][y] = number  # 첫 번째 숫자 할당하고 시작

    # 달팽이를 모두 채울 때까지 다음 4가지 패턴을 반복한다.
    while number < N * N:
        # 1. y값 증가
        for j in range(y+1, N):
            if snail[x][j] == 0:
                number += 1
                snail[x][j] = number
            # 현재 위치에 값이 할당되어 있다면 다음 패턴으로 넘어간다.
            else:
                y = j - 1
                break
        else:
            y = j

        # 2. x값 증가
        for i in range(x+1, N):
            if snail[i][y] == 0:
                number += 1
                snail[i][y] = number
            # 현재 위치에 값이 할당되어 있다면 다음 패턴으로 넘어간다.
            else:
                x = i - 1
                break
        else:
            x = i

        # 3. y값 감소
        for j in range(y-1, -1, -1):
            if snail[x][j] == 0:
                number += 1
                snail[x][j] = number
            # 현재 위치에 값이 할당되어 있다면 다음 패턴으로 넘어간다.
            else:
                y = j + 1
                break
        else:
            y = j

        # 4. x값 감소
        for i in range(x-1, -1, -1):
            if snail[i][y] == 0:
                number += 1
                snail[i][y] = number
            # 현재 위치에 값이 할당되어 있다면 다음 패턴으로 넘어간다.
            else:
                x = i + 1
                break
        else:
            x = i
    
    # 결과를 출력한다.
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print()