T = int(input())  # 테스트 케이스 개수
 
for test_case in range(1, T+1):
    N = int(input())  # 카드 장수
    cards = input()  # 카드 숫자가 여백없이 주어진다.(str)
     
    # cards 에서 숫자 하나씩 순회하면서
    # card_list 에 카운트를 저장한다.
    # 이때 card_list의 인덱스가 카드의 숫자를, 값이 카운트를 의미한다.
    card_list = [0] * 10
    for card in cards:
        card_number = int(card)
        card_list[card_number] += 1
     
    # card_list에서 값이 가장 큰 인덱스(=가장 많은 카드의 숫자)
    max_count_number = -1
    max_count = 0
    for i in range(9, -1, -1):
        if card_list[i] > max_count:
            max_count_number = i
            max_count = card_list[i]
     
    print(f'#{test_case} {max_count_number} {max_count}')