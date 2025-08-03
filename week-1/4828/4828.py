T = int(input())
  
for test_case in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))
  
    result = max(number_list) - min(number_list)
    print(f'#{test_case} {result}')