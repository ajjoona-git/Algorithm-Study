# 9251. LCS

"""
시간 제한 2초, 메모리 제한 256MB
---
두 수열(최대 1000자) -> 모두의 부분 수열이 되는 수열 중 가장 긴 것

- line1을 기준으로 line2를 순회했더니, 가장 긴 것이 아닌 경우도 발생 (오답)
    - 반례: ABCDE / BCEAB
- 1)line1을 기준으로, 2)line2를 기준으로, 두 번 순회하여 길이를 비교 (오답)
- line1을 기준으로 하되, pointer1을 0부터 시작할 때와 그 이상에서 시작할 때를 비교 (오답)
    - 반례: VREGDFELK / VLSKD => VD (정답: VLK)
- 3번 + 2번 (오답)
"""

def find_lcs(line1, line2):
    """line1을 기준으로 line2를 순회하면서 일치하는 문자를 찾는다.(투포인터)"""
    global max_length
    n1, n2 = len(line1), len(line2)

    for start in range(n1):
        # 만약 남아있는 문자열의 길이가 max_length보다 작다면 종료한다.
        if n1 - start <= max_length:
            return

        # 관련 변수 초기화
        lcs = 0
        pointer2 = 0

        # line1을 기준으로 찾을 문자를 지정한다.
        for pointer1 in range(start, n1):
            # 백트래킹을 위해 가장 최근 포인터를 기록해둔다.
            latest = pointer2

            # 일치하는 문자를 찾는다.
            while pointer2 < n2 and line2[pointer2] != line1[pointer1]:
                pointer2 += 1
            
            # 일치하는 문자를 찾지 못했다면 최근 포인터로 돌아간다.(백트래킹)
            if pointer2 == n2:
                pointer2 = latest
            # 찾았다면 lcs에 기록하고 포인터를 한 칸 이동한다.
            else:
                lcs += 1
                pointer2 += 1
                
            # lcs를 모두 찾았다면(line2에서 마지막 문자까지 찾았다면) 종료한다.
            if pointer2 == n2:
                break

        # max_length를 갱신한다.
        max_length = max(max_length, lcs)


str1 = input().strip()
str2 = input().strip()

max_length = 0
find_lcs(str1, str2)
find_lcs(str2, str1)

# lcs의 길이를 출력한다.
print(max_length)

