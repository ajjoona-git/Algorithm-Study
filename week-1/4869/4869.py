T = int(input())  # 테스트 케이스의 수

def factorial(n):
    '''주어진 정수(n)의 팩토리얼 계산 값을 반환하는 함수'''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

for test_case in range(1, T+1):
    N = int(input())//10  # 직사각형의 폭/ 계산 편의를 위해 10으로 나눔
    number_of_cases = 0  # 경우의 수

    # 20x20 덩어리 개수에 따라 계산
    # 가능한 20x20 덩어리 개수 -> (N // 20)
    # 덩어리 1개 당 2가지 경우의 수 -> 20x20 1개, 10x20 2개(가로로)

    # (N // 20)번 반복하면서 경우의 수를 합산한다.
    # (덩어리 개당 2가지) ** (덩어리 개수) * (조각 수)!/(덩어리 수)!(10x20 수)!
    for i in range(N//2 + 1):
        # i는 20x20 덩어리의 수
        # j는 10x20 조각의 수
        j = N - i * 2
        number_of_cases += (2 ** i) * factorial(i+j)/(factorial(i)*factorial(j))

    # 결과 출력
    print(f'#{test_case} {int(number_of_cases)}')