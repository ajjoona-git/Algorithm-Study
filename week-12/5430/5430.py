# 5430. AC

"""
python3 224ms
---
시간제한 1초, 메모리제한 256MB
---
R(순서 뒤집기) 
D(첫 번째 수 버리기) - 빈 배열에서는 에러
1 <= 함수 p의 길이 <= 100,000
---
매번 뒤집고 pop하면 시간초과
-> 배열은 그대로 두고, left, right 포인터를 이용하자! 
    출력할 때는 left ~ right 슬라이싱
"""

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    p = input()  # 함수
    n = int(input())  # 배열의 길이
    input_str = input()  # 배열 [x1, ..., xn]

    # 함수만 보고 전처리하기
    # 1. D의 개수가 배열의 길이보다 크면 error
    if p.count("D") > n:
        print("error")
        continue
    # 2. "RR" 연속으로 있으면 원본이랑 똑같으므로 제거
    p = p.replace("RR", "")

    # 입력받은 배열 문자열을 리스트로 저장
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input_str.strip('[]').split(',')))

    # 인덱스 포인터
    left, right = 0, n - 1

    # 전처리된 함수를 순회하면서 명령 수행
    for command in p:
        # 순서 뒤집기 (R)
        if command == 'R':
            left, right = right, left
        # 첫 번째 수 버리기 (D)
        elif command == 'D':
            # 배열이 비어있으면 error
            if n == 0:
                print("error")
                break

            if left <= right:  # 정방향
                left += 1
            else:  # 역방향 (left > right)
                left -= 1
            n -= 1


    # 최종 배열 저장
    if n == 0:
        print([])
        continue

    if left < right:  # 정방향
        result = arr[left:right + 1]
    elif right == 0:  # (오류처리) 리스트의 시작점까지라면 stop을 생략 
        result = arr[left::-1]
    else:  # 역방향
        result = arr[left:right - 1:-1]

    print(f"[{','.join(map(str, result))}]")
