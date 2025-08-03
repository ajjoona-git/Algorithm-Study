T = int(input())  # 테스트 케이스 개수

def binary_search(l, r, target):
    '''
    이진 탐색으로 target을 찾기까지 탐색 횟수를 반환하는 함수
    '''
    c = int((r+l) / 2)
    count = 1
    # 이진 탐색을 진행한다.
    while c != target:
        # c의 값 갱신
        c = int((r+l) / 2)
        count += 1

        # c의 값과 타겟 넘버를 비교해서 l, r을 갱신한다.
        if c < target:
            l = c
        elif c > target:
            r = c
    return count

def who_is_winner(A, B):
    '''
    A와 B의 크기를 비교하여 더 작은 값을 반환하는 함수
    단, 크기가 같을 경우 0을 반환한다.
    '''
    if A < B:
        return "A"
    elif A > B:
        return "B"
    else:
        return "0"
    
for test_case in range(1, T+1):
    # 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb를 입력받는다.
    P, Pa, Pb = map(int, input().split())
    
    # A와 B의 탐색 횟수를 저장
    count_a = binary_search(1, P, Pa)
    count_b = binary_search(1, P, Pb)
        
    # A와 B의 탐색 횟수 비교
    result = who_is_winner(count_a, count_b)
    print(f'#{test_case} {result}')