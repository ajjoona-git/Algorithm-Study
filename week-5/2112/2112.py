# 2112. 보호 필름

# import sys
# sys.stdin = open("sample_input.txt")


def is_passed():
    """열 우선 탐색으로 연속된 K개 이상의 셀이 있는지 확인"""
    for c in range(W):
        count = 1
        for r in range(D-1):
            if cells[r][c] == cells[r + 1][c]:
                count += 1
            else:
                count = 1
            
            if count == K:
                break
        else:
            return False
    return True


def performance_test(count, row):
    """각 가로줄에 약품을 투입하지 않은 경우, 약품 A를 투입한 경우, 약품 B를 투입한 경우에 대하여
        성능검사를 통과하는 최소 약품 투입 횟수를 반환한다."""
    global result 

    # 가지치기: 현재 최소 투입 횟수보다 count가 크면 종료
    if count >= result:
        return
    
    # 종료 조건: 모든 가로줄의 상태를 정했을 때
    if row == D:
        if is_passed():            
            result = min(result, count)
        return 
    
    # 백트래킹 준비: 데이터 백업
    origin_row = cells[row]
    # 약품을 투입하지 않은 경우
    performance_test(count, row + 1)
    # 약품 A를 투입한 경우
    cells[row] = [0] * W
    performance_test(count + 1, row + 1)
    # 약품 B를 투입한 경우
    cells[row] = [1] * W
    performance_test(count + 1, row + 1)
    # 백트래킹: 데이터 원상복구
    cells[row] = origin_row


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    # 특성A는 0, 특성B는 1로 표시된다.
    cells = [list(map(int, input().split())) for _ in range(D)]

    if is_passed():
        print(f'#{tc} {0}')
        continue
    
    result = K
    performance_test(0, 0)
    print(f'#{tc} {result}')