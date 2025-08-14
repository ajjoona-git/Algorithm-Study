# 6190. 정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 두 수의 곱 중 단조 증가하는 수
    results = []

    # 두 수의 곱이 단조 증가하는 수인지 확인
    for i in range(N):
        for j in range(i+1, N):
            # 두 수의 곱
            number = numbers[i] * numbers[j]
            # 각 숫자의 자릿수
            digits = [int(char) for char in str(number)]
            for k in range(len(digits)-1):
                # 단조 증가하지 않음
                if digits[k] > digits[k+1]:
                    break
            else:
                results.append(number)

    # 단조 증가하는 두 수의 곱 계산
    if results:
        result = max(results)
    else:
        result = -1

    print(f'#{tc} {result}')