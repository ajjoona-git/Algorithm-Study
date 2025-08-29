import sys
sys.stdin = open("sample_input.txt")


def check():
    """
        오로지, 시험 통과 가능 여부만 본다.
        1. 세로로 순회 즉, 평소와 x, y 순서가 바뀌어야 한다.
        2. 이번 열을 조사하면서, 몇 번 시험에 통과했는지 체크
        3. 시험 통과한 횟수가 K가 되면, 다음 열로 넘어가야 한다.
    """
    for c in range(W):
        cnt = 1
        is_possible = False
        for r in range(1, D):
            # 내 값이 이전 값이랑 같으면 누적 1 증가
            if data[r][c] == data[r-1][c]:
                cnt += 1
            # 다르면 cnt 1로 초기화
            else:
                cnt = 1
            
            if cnt >= K:
                is_possible = True
                break
        
        # 이번 c에 대해서 모든 r을 조사했지만,
        # 여전히 is_possible 하지 못하면? 조사 의미없다.
        # else:
        if not is_possible:
            return False
        
    return True



def search(row_idx, acc_count):
    """
        row_idx: 몇 번째 행에 약물 투여 여부
        acc_count: 지금까지 몇 번 약물을 투약했는지
    """
    global result  # 최소 약물 투여 횟수
    
    # 최소 약물 투여 횟수보다 현재 약물 투여 횟수가 많거나 같은 경우..
    # 그럼.. 내가 row_idx번째를 조사하고 있든 말든..
    # 남아있는 두꼐가 있든 말든.. 조사할 필요가 없다!
    # --- 가지치기 --- 유망성 없음.
    if acc_count >= result: return

    # 종료 조건
    if row_idx == D:
        # 모든 경우 다 시도해본 뒤, 어쨋든 D까지 도달한 시점
        # 이번 회차.... 통과 가능합니까?
        if check():
            result = min(result, acc_count)
        return

    # 이번 회차는? 모르겠고 일단 다음 회차를 만드는 법?

    # row_idx가 1 증가한다. -> 다음 행에 대해 조사하러 가겠다,
    # 1. 약 안 넣기
        # acc_count가 안 늘어나면 된다.
    search(row_idx + 1, acc_count)
    # 약 넣기 전에 원본 좀 채취해 둘게요..~
    origin_row = data[row_idx][:]


    # 2. A 약 넣기
        # acc_count가 늘어나면 된다.
    data[row_idx] = [0] * W
    search(row_idx + 1, acc_count + 1)

    # 3. B 약 넣기
        # acc_count가 늘어나면 된다.
    data[row_idx]= [1] * W
    search(row_idx + 1, acc_count + 1)
    
    # 여기까지 돌아올 때까지 origin_row는 local 영역에 잘 살아있다.
    # 데이터 원상복구
    # --- backtracking ---
    data[row_idx] = origin_row



T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]
    # 최종 결과값을 초기에 세팅할 때는 무엇으로 해야 할까?
    result = K  # 문제를 가장 바보같이 해결했을 때의 결과값
    # 아마 어떠한 함수를 통해서 문제 해결
    search(0, 0)

    print(f'#{tc} {result}')
