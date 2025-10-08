# 150370. 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    
    # {약관 종류: 유효기간} 딕셔너리 형태로 저장
    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)

    # 약관 만료일 계산
    for i in range(len(privacies)):
        start_date, contract = privacies[i].split()
        start_date = list(map(int, start_date.split('.')))  # [YYYY, MM, DD]
        
        end_date = start_date[:]
        end_date[1] += terms_dict[contract]
        end_date[2] -= 1
        
        if end_date[2] == 0:
            end_date[2] = 28
            end_date[1] -= 1
        
        if end_date[1] > 12:
            end_date[0] += end_date[1] // 12
            end_date[1] %= 12
        
        if end_date[1] == 0:
            end_date[1] = 12
            end_date[0] -= 1

        end_date_str = f"{end_date[0]}.{end_date[1]:02}.{end_date[2]:02}"
        if today > end_date_str:
            answer.append(i+1)
            
    return answer