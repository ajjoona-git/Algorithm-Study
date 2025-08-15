# 4881. 배열 최소 합

def sum_array(arr, row, subtotal):
    """주어진 2차원 배열(arr)에서 row 이상의 행에서 숫자를 하나씩 골라 최소합을 반환하는 함수"""
    global min_sum

    # 탈출 조건
    if row == N:
        min_sum = min(min_sum, subtotal)
        return
    
    if subtotal > min_sum:
        return
    
    for col in range(N):
        if visited_col[col] is False:
            visited_col[col] = True
            sum_array(arr, row+1, subtotal+arr[row][col])
            visited_col[col] = False
            
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 한 번 선택한 열은 선택 후보에서 제외하기 위함
    visited_col = [False] * N
    min_sum = float('inf')
    sum_array(arr, 0, 0)

    print(f'#{tc} {min_sum}')