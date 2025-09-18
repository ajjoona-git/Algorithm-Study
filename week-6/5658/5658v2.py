# 5658. 보물상자 비밀번호
# 리스트 pop & insert(0)


def get_numbers():
    """만들 수 있는 모든 수를 10진수로 저장한 집합을 반환한다."""
    numbers = set()  # 만든 숫자를 저장
    side_len = N // 4  # 한 변의 길이

    for _ in range(side_len):
        for idx in range(0, N, side_len):
            hex_str = ''.join(passwords[idx:idx+side_len])
            numbers.add(int(hex_str, 16))
        passwords.insert(0, passwords.pop())
    
    return numbers


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    passwords = [i for i in input()]

    numbers = get_numbers()
    numbers_list = sorted(numbers, reverse=True)
    result = numbers_list[K-1]

    print(f'#{tc} {result}')