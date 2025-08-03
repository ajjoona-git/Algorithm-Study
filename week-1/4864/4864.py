T = int(input())  # 테스트 케이스의 수
 
def is_included(str1, str2):
    '''
    주어진 문자열 str1, str2에 대하여 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 함수
    첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다
    '''
    if str1 in str2:
        return 1
    else:
        return 0
 
for test_case in range(1, T+1):
    # 비교할 문자열 str1과 str2를 입력받는다.
    str1 = input()
    str2 = input()
     
    # 함수를 이용해 두 문자열을 비교한다.
    result = is_included(str1, str2)
     
    print(f'#{test_case} {result}')
