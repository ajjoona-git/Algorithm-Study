# 1946. 간단한 압축풀기

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 알파벳과 숫자 쌍의 수
    
    # 압축을 푼 원본 문서 (너비는 10으로 고정)
    document = [[0] * 10]

    # 알파벳과 숫자 쌍을 하나씩 받아와 압축을 푼다.
    for _ in range(N):
        alphabet, num = input().split()
        # 숫자만큼 반복하면서 원본 문서에 알파벳을 추가한다.
        for _ in range(int(num)):
            # 원본 문서의 마지막 줄의 길이가 10이라면
            if len(document[-1]) >= 10:
                # 다음 줄에 입력한다.
                document.append([alphabet])
            # 원본 문서의 마지막 줄의 길이가 10 미만이라면
            else:
                # 마지막 줄에 추가한다.
                document[-1].append(alphabet)
	
    # 결과를 출력한다.
    print(f'#{test_case}')
    # 원본 문서의 첫 번째 줄은 0으로 초기화되어 있기 때문에
    # 그 다음 줄부터 출력한다.
    for i in range(1, len(document)):
        print(''.join(document[i]))