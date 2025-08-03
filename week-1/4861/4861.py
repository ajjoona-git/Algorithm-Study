T = int(input())  # 테스트 케이스의 수

def is_palindrome(str):
    # 주어진 문자열(str)이 회문인지 확인하는 함수
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            return False
    return True

for test_case in range(1, T+1):
    # 글자판의 크기 N, 회문의 길이 M
    N, M = map(int, input().split())
    
    # 글자판 생성
    letters = [[] * N for _ in range(N)]
    for i in range(N):
        for letter in input():
            letters[i].append(letter)
    # 세로 문자열 탐색을 위한 글자판
    letters_col = list(map(list, zip(*letters)))

    # 글자판을 순회하면서 회문을 탐색한다.
    for i in range(N):
        for j in range(N):
		    # 가로 문자열    
            # 탐색할 문자열의 길이가 글자판을 넘어가지 않는 경우
            if len(letters[i][j:]) < M:
                pass
            else:
                if is_palindrome(letters[i][j:j+M]) is True:
                    result = letters[i][j:j+M]
                    
    		# 세로 문자열          
            if len(letters_col[i][j:]) < M:
                pass
            else:
                if is_palindrome(letters_col[i][j:j+M]) is True:
                    result = letters_col[i][j:j+M]
                    
    # 결과 출력
    print(f'#{test_case} {"".join(result)}')