# 테스트 케이스의 수
T = int(input())

# 테스트 케이스별로 실행한다.
for test_case in range(1,T+1):
    N = int(input())  # 테스트 케이스의 번호
    scores = list(map(int, input().split()))  # 학생들의 점수 리스트
    numbers_count = {}  # {'점수': '빈도수'} 로 구성된 딕셔너리
    
    # 점수 리스트를 순회하면서 점수와 빈도수를 기록한다.
    for score in scores:
        if score in numbers_count:  # 이미 딕셔너리에 기록된 점수라면
            numbers_count[score] += 1  # 빈도수를 1 증가한다.
        else:  # 처음 나오는 점수라면
            numbers_count[score] = 1  # 빈도수는 1로 새로 기록한다.
    
    # 최빈값을 찾기 위해 딕셔너리의 value들 중 최댓값을 찾는다.
    max_count = max(numbers_count.values())
    # 빈도수의 최댓값(max_count)를 기준으로 key(점수)를 찾아 리스트에 저장한다.
    # 그 중 가장 높은 점수를 반환한다.
    modes = []
    for score, count in numbers_count.items():
        if count == max_count:
            modes.append(score)
    
    print(f'#{N} {max(modes)}')