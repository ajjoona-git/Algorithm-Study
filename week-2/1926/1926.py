# 1926. 간단한 369 게임

N = int(input())

# 1부터 N까지의 숫자를 순회하면서
for i in range(1, N+1):
    # 문자열의 replace() 메서드를 활용하기 위해 문자열로 형변환한다.
    i_str = str(i)
    # 3, 6, 9인 부분을 -(박수)로 치환한다.
    i_str = i_str.replace('3', '-')
    i_str = i_str.replace('6', '-')
    i_str = i_str.replace('9', '-')

    # i_str에 박수와 숫자가 혼재되어 있다면 숫자를 제거한다.
    if '-' in i_str:
        # i_str = i_str.strip("1234567890")  # 양쪽 끝에 있는 숫자를 제거한다.
        num_of_parts = len(i_str.split('-'))  # '-'를 구분자로 한 덩어리의 수를 계산하고,
        i_str = '-' * (num_of_parts - 1)  # '-'의 수(=덩어리의 수 - 1)만큼 i_str에 재할당한다.

    print(i_str, end=' ')
