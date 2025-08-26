# 2112. 보호 필름

from itertools import combinations
import sys
sys.stdin = open("sample_input.txt")


def get_max_len(column):
    """주어진 리스트(column)에서 연속된 문자의 최대 길이를 반환하는 함수"""
    max_len = 0
    curr_len = 1
    for i in range(1, D):
        # 현재 셀과 이전 셀이 같은 경우, 길이 +1
        if column[i] == column[i-1]:
            curr_len += 1
        # 현재 셀과 이전 셀이 다른 경우, 최대 길이 갱신 후 길이 초기화
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
    return max_len


def is_passed(section):
    """모든 column에 대해 성능검사 통과 여부를 반환하는 함수"""
    # section을 전치한 리스트
    trans_section = list(zip(*section))
    for i in range(W):
        max_len = get_max_len(trans_section[i])
        if max_len < K:
            return False
    return True


def inject_drug(section, r, type):
    """section의 r번째 가로줄에 약품을 주입했을 때 변화한 단면 정보를 반환하는 함수"""
    section = section[:r] + [[type] * W] + section[r+1:]
    return section


def cnt_check(section, row, cnt):
    """row행부터 약물을 주입한다."""
    if cnt == K:
        return
    print(cnt, row)
    for r in range(row, D):
        print("  ", r)
        for type in range(2):
            # section = inject_drug(section, r, type)
            print("    ", type)
            if is_passed(inject_drug(section, r, type)):
                return cnt
    
    # 약물 2개 이상일 때부터 어카지,,,
    cnt_check(inject_drug(section, r, 0), row+1, cnt+1)


# def solve():
#     drug_cnt = 0
#     # 성능검사를 통과할 때까지 반복한다.
#     while drug_cnt <= K:
#         drug_cnt += 1
#         # 약품을 투입할 가로줄 인덱스 조합을 생성한다.
#         row_combos = list(combinations(range(D), drug_cnt))
#         for row_combo in row_combos:
#             # for row in row_combo:
#                 # section_with_a = inject_drug(section, row, '0')
#             # 1. 약품A('0')를 투입
#             if is_passed(inject_drug(section, row_combo, '0')):
#                 return drug_cnt
#             # 2. 약품B('1')를 투입
#             if is_passed(inject_drug(section, row_combo, '1')):
#                 return drug_cnt



T = int(input())
for tc in range(1, 1+1):
    # 두께 D, 가로 W, 합격기준 K
    D, W, K = map(int, input().split())
    # 보호 필름 단면의 정보 (DxW)
    # (특성A는 0, 특성B는 1)
    section = [list(map(int, input().split())) for _ in range(D)]


    if is_passed(section):
        print(f'#{tc}', 0)
        break
    
    drug_cnt = cnt_check(section, 0, 1)
    print(f'#{tc} {drug_cnt}')
        
        