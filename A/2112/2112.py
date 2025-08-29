# 2112. 보호 필름

# import sys
# sys.stdin = open("sample_input.txt")


def is_passed(section):
    """모든 column에 대해 성능검사 통과 여부를 반환하는 함수"""
    # column 하나씩 순회 (열 우선 순회)
    for j in range(W):
        curr_len = 1  # 연속된 셀의 길이
        for i in range(1, D):
            # 현재 셀과 이전 셀이 같은 경우, 길이 +1
            if section[i][j] == section[i-1][j]:
                curr_len += 1
            # 현재 셀과 직전 셀이 다른 경우, 길이 초기화
            else:
                curr_len = 1

            # 길이가 K 이상이면 더 이상 검사할 필요가 없이 pass
            if curr_len >= K:
                break
            
        # break가 한번도 실행되지 않았다는 것은 곧 성능검사에 통과하지 못한 것
        # 하나라도 통과하지 못하면 더 이상 검사할 필요 없이 False 반환
        else:
            return False
    return True
    


def select_row_status(row_idx, drug_cnt):
    """
    현재 행(row_idx)에 대해서 다음 세 가지 경우를 재귀 호출하며 탐색하고(3^D), 
    성능검사에 통과할 수 있는 최소 약품 투여 회수를 갱신하는 함수
        1) 약품을 넣지 않는 경우, 
        2) 약품A를 투입한 경우, 
        3) 약품B를 투입한 경우
    """
    global min_drug
    
    # 종료 조건: 현재 행(row_idx)이 최대 인덱스(D-1)를 넘어가는 경우,
    #            모든 행에 대해 약품 투입 여부가 결정되었으므로
    #            성능검사 진행 후 최소 횟수(min_drug)를 갱신한다.
    if row_idx > D - 1:
        if is_passed(section):
            min_drug = min(min_drug, drug_cnt)
        return


    # 가지치기: 현재 약품 투여 횟수(drug_cnt)가 최소 횟수보다 작을 경우,
    #           더 이상 탐색할 가치가 없다.
    if drug_cnt >= min_drug:
        return


    # 1) 약품을 넣지 않는 경우
    select_row_status(row_idx + 1, drug_cnt)

    # 백트래킹 준비: 현재 행의 원본을 복제해둔다.
    row_backup = section[row_idx]

    # 2) 약품A를 투입한 경우
    section[row_idx] = [0] * W
    select_row_status(row_idx + 1, drug_cnt + 1)

    # 3) 약품B를 투입한 경우
    section[row_idx] = [1] * W
    select_row_status(row_idx + 1, drug_cnt + 1)

    # 백트래킹: 현재 행의 데이터 원복
    section[row_idx] = row_backup



T = int(input())
for tc in range(1, T+1):
    # 두께 D, 가로 W, 합격기준 K
    D, W, K = map(int, input().split())
    # 보호 필름 단면의 정보 (DxW)
    # (특성A는 0, 특성B는 1)
    section = [list(map(int, input().split())) for _ in range(D)]

    # 최소 약품 투약 횟수를 성능검사 기준으로 초기화
    min_drug = K

    # 각 줄의 투약 여부에 따른 성능검사를 진행 
    select_row_status(0, 0)

    print(f'#{tc} {min_drug}')