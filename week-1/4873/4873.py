T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # 문자열을 입력받는다.
    str = input()
    
    # 1. 문자열을 저장할 리스트(stack) stack을 만든다.
    stack = []

    # 2. 주어진 문자열 str을 순회하면서
    for char in str:
        try:
            # 현재 문자와 stack.pop()을 비교한다.
            former_char = stack.pop()
            # 일치하면, 계속 순회
            if char == former_char:
                continue
            # 일치하지 않으면, 
            else:
                # stack.pop()을 다시 추가하고 현재 문자도 stack에 추가한다.
                stack.extend([former_char, char])
                # print(stack)
        except IndexError:
            # stack이 비어있다면 현재 문자를 추가한다.
            stack.append(char)

    # 3. 문자열 순회가 종료된 후에 stack의 길이를 출력한다.
    print(f'#{test_case} {len(stack)}')