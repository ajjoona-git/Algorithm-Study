# str1의 문자 요소들을 key로, 개수를 value로 하는 dict 생성
# value는 .count() 메서드 활용
# str1의 문자를 pop해서
	# if pop한 문자 not in dict.keys(): dict.update()
# 이렇게 하려면 str1, str2를 리스트로 변환하는 게 낫겠다.

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # 문자열 str1, str2를 입력받는다.
    # str2는 추후 리스트의 메서드를 활용하기 위해 리스트로 변환한다.
    str1 = input()
    str2 = [ i for i in input() ]

    # 글자의 수를 저장할 dictionary를 생성한다.
    count_char = {}

    # 글자 개수 세기
    # str1을 순회하면서
    for char in str1:
        # count_char.keys()에 없으면
        if char not in count_char.keys():
            # char를 key로, str2에서 char의 수를 value로 값을 추가한다.
            count_char[char] = str2.count(char)
        
        # count_char.setdefault(char, str2.count(char))

    # 글자 개수의 최댓값을 저장할 변수 생성
    max_count = max(count_char.values())

    # 결과를 출력한다.
    print(f'#{test_case} {max_count}')