# 기출 복원. 탑 쌓기

import sys
sys.stdin = open("input.txt")


def sort_desc(arr):
    """주어진 1차원 배열(arr)을 내림차순으로 정렬하는 함수 (선택 정렬 사용)"""
    n = len(arr)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr


def calculate_expense(top):
    """주어진 1차원 배열(top)의 인덱스와 값의 곱을 합한 값을 반환하는 함수"""
    expense = 0
    for index, value in enumerate(top):
        expense += index * value
    return expense

T = int(input())
for tc in range(1, T+1):
    # N: 전체 화물의 수, W1: 탑1의 높이, W2: 탑2의 높이
    N, W1, W2 = map(int, input().split())
    # weights: N개의 화물의 무게
    weights = list(map(int, input().split()))

    # 1. 화물의 무게를 내림차순으로 정렬
    weights_desc = sort_desc(weights)

    # 2. 무게순으로 정렬한 화물을 탑1과 탑2에 순차적으로 배정 
    #    (낮은 층수에 무거운 화물이 쌓일 수 있도록 한다.)
    # 계산의 편의를 위해 top1과 top2의 0번째 값을 0으로 초기화한다.
    top1 = [0]
    top2 = [0]
    for i in range(N):
        # 번갈아 배정하기 위해 홀수/짝수번째 화물을 탑1/탑2에 배정한다.
        if i % 2 == 0:
            # 1. 짝수번째 & 탑1 배정 가능 -> 탑1
            if len(top1) <= W1:
                top1.append(weights_desc[i])
                continue
            # 2. 짝수번째 & 탑1 배정 완료 -> 탑2
            elif len(top2) <= W2:
                top2.append(weights_desc[i])
                continue
        else:
            # 3. 홀수번째 & 탑2 배정 가능 -> 탑2
            if len(top2) <= W2:
                top2.append(weights_desc[i])
                continue
            # 4. 홀수번째 & 탑2 배정 완료 -> 탑1
            elif len(top1) <= W1:
                top1. append(weights_desc[i])
                continue

    # 3. 최저 비용을 계산한다.
    min_expense = calculate_expense(top1) + calculate_expense(top2)

    print(f'#{tc} {min_expense}')