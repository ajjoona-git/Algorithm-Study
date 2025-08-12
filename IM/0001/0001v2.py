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


T = int(input())
for tc in range(1, T+1):
    # N: 전체 화물의 수, W1: 탑1의 높이, W2: 탑2의 높이
    N, W1, W2 = map(int, input().split())
    # weights: N개의 화물의 무게
    weights = list(map(int, input().split()))

    # 1. 화물의 무게를 내림차순으로 정렬
    weights_desc = sort_desc(weights)

    # 2. 탑의 높이 제한에 따라 화물의 무게에 곱해줄 계수(탑의 층)를 구한다.
    # (전체의 최저 비용만 계산하면 되기 때문에 탑에 배정할 필요가 없다.)
    coeffecient = list(range(1, W1+1)) + list(range(1, W2+1))
    # 계수를 오름차순으로 정렬
    coeffecient = sort_desc(coeffecient)[::-1]

    # 3. 최저 비용을 계산한다.
    min_expense = 0
    for i in range(N):
        min_expense += coeffecient[i] * weights_desc[i]

    print(f'#{tc} {min_expense}')