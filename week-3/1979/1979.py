# 1979: 어디에 단어가 들어갈 수 있을까

def count_length_hor(r, c):
    """주어진 좌표(r, c)에서 가로 방향으로 흰색 부분의 길이를 탐색하고,
        해당 길이가 K라면 word_count를 +1 하는 함수"""
    global word_count

    if not chk_h[r][c] and puzzle[r][c] == '1':
        chk_h[r][c] = True
        len = 1

        # 가로 길이
        while c+len < N and puzzle[r][c+len] == '1':
            chk_h[r][c+len] = True
            len += 1
        if len == K:
            word_count += 1
        
    else:
        len = 0
    
    return


def count_length_ver(r, c):
    """주어진 좌표(r, c)에서 세로 방향으로 흰색 부분의 길이를 탐색하고,
        해당 길이가 K라면 word_count를 +1 하는 함수"""
    global word_count

    if not chk_v[r][c] and puzzle[r][c] == '1':
        chk_v[r][c] = True
        len = 1

        # 세로 길이
        while r+len < N and puzzle[r+len][c] == '1':
            chk_v[r+len][c] = True
            len += 1
        if len == K:
            word_count += 1
        
    else:
        len = 0
    
    return


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # puzzle: 흰색 부분은 1, 검은색 부분은 0
    puzzle = [input().split() for _ in range(N)]

    word_count = 0
    chk_h = [[False] * N for _ in range(N)]
    chk_v = [[False] * N for _ in range(N)]

    # 퍼즐을 순회하면서 길이 탐색
    for r in range(N):
        for c in range(N):
            count_length_hor(r, c)
            count_length_ver(c, r)

            
    print(f'#{tc} {word_count}')
            