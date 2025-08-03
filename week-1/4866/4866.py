T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # 괄호를 저장할 리스트 생성
    parentheses = []
    # 정상적으로 짝을 이루었는지 결과값을 저장할 변수
    is_pair = 1

    # 입력받은 문자열을 순회하면서
    for char in input():
        # 1. 여는 괄호 `(` 또는 `{` 이면
        if char == '(' or char == '{':
            # 리스트에 추가한다.
            parentheses.append(char)
            # print(parentheses)
        # 2. 닫는 괄호 `)` 또는 `}` 이면
        # 리스트에서 pop 한 값과 비교하여
        # 짝이 맞지 않으면 is_pair = 0
        elif char == ')':
            # 리스트가 비어있는 경우 is_pair = 0
            if not parentheses:
                is_pair = 0
                break
            elif parentheses.pop() != '(':
                    is_pair = 0
                    break
        elif char == '}':
            # 리스트가 비어있는 경우 is_pair = 0
            if not parentheses:
                is_pair = 0
                break
            elif parentheses.pop() != '{':
                    is_pair = 0
                    break
            
    # 문자열 순회를 끝까지 마친 경우 
    else:
        # parentheses 리스트에 값이 남아있으면
        if parentheses:
            # 짝이 맞지 않은 것
            is_pair = 0

    # 결과 출력
    print(f'#{test_case} {is_pair}')