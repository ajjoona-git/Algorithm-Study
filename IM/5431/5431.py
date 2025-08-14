# 5431. 민석이의 과제 체크하기 

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 과제를 제출한 학생의 번호
    submitted = list(map(int, input().split()))
    # 현재까지 과제를 제출하지 않은 학생들의 번호
    students = list(range(1, N+1))

    for num in submitted:
        # students 리스트에서 과제를 제출한 학생의 번호는 제거한다.
        students.remove(num)

    # 리스트에 1번부터 N번까지 순차적으로 저장되어 있기 때문에 따로 정렬은 하지 않는다.
    print(f'#{tc}', *students)
