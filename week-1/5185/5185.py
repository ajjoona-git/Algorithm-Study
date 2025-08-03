# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
	# 자리 수 N, 16진수 hexa
	N, hexa = input().split()
	# 이진수를 담을 빈 리스트 생성
	# 16진수 1자리가 2진수 4자리로 표시된다.
	binary_list = []
	
	for i in hexa:
		# 4자리 2진수를 저장할 리스트 생성
		# 2진수의 앞자리는 0으로 채우기 위해 0으로 초기화한다.
		binary_number = [0] * 4
		
		# A~F로 표시된 숫자를 10진수로 변경(A: 65)
		try:
			i = int(i)
		except:
			i = ord(i) - 55

		# 10진수를 2진수로 변경
		# 2로 나눈 나머지를 뒤에서부터 저장한다.
		for j in range(4):
			binary_number[3-j] = i % 2
			i = i // 2
			
		binary_list.append(binary_number)
	
	# 테스트 케이스 번호와 답을 출력한다.
	print(f'#{test_case}', end=' ')
	for i in range(int(N)):
		for j in range(4):
			print(binary_list[i][j], end='')
	print()