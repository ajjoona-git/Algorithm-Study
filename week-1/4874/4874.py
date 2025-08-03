T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # Forth와 연산 결과를 저장할 리스트를 생성한다.
    forth = input().split()
    num_stack = []

    # 주어진 문자열을 순회하면서
    for char in forth:
        # 1. '.'이면 스택에서 숫자를 꺼내 출력한다.
        if char == '.':
            if len(num_stack) == 1:
                result = num_stack.pop()
            # num_stack에 숫자가 없거나 두 개 이상 남아있다면 error 출력
            else:
                result = 'error'
            break
        # 2. 숫자면 num_stack에 추가한다.
        elif char.isdecimal():
            num_stack.append(int(char))
        # 3. 연산자면 num_stack에서 숫자 2개를 꺼내 계산한 후, 계산한 값을 num_stack에 추가한다.
        else:
            try:
                a = num_stack.pop()
                b = num_stack.pop()
                if char == '+':
                    num_stack.append(b+a)
                elif char == '-':
                    num_stack.append(b-a)
                elif char == '*':
                    num_stack.append(b*a)
                elif char == '/':
                    num_stack.append(int(b/a))
            except Exception:
                # 꺼낼 숫자가 없다면 error 출력
                result = 'error'
                break

    # 결과 출력
    print(f'#{test_case} {result}')