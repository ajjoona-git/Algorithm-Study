# 4615. 재미있는 오셀로 게임


def reverse_color(color):
    """color가 1이면 2를, 2이면 1을 반환하는 함수"""
    if color == 1:
        return 2
    else:
        return 1
    

T = int(input())
for tc in range(1, T+1):
    # N: 보드의 크기(NxN), M: 돌을 놓는 횟수
    N, M = map(int, input().split())
    
    # N+1xN+1 보드판
    # 인덱스와 좌표를 맞추기 위해 0 인덱스를 패딩
    # (0: 돌 없음, 1: 흑돌, 2: 백돌)
    board = [[0] * (N+1) for _ in range(N+1)]
    
    # 보드판 초기 세팅
    board[N//2][N//2] = 2
    board[N//2][N//2+1] = 1
    board[N//2+1][N//2] = 1
    board[N//2+1][N//2+1] = 2
    
    # 인접한 돌 탐색을 위한 8방향 델타 (북쪽부터 시계방향)
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    

    # 돌을 놓을 위치(c, r)와 돌의 색(1: 흑돌, 2: 백돌)
    # 이때 c와 r의 범위는 1 ~ N
    for _ in range(M):
        c, r, color = map(int, input().split())
        board[r][c] = color

        # 뒤집어야 할 돌을 임시 저장할 세트
        # 한 번 돌을 놓을 때, 중복되는 돌은 한번만 뒤집기 위해 세트로 지정함
        stones = set()

        # 8방향으로 인접한 돌 탐색
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            
            temp = []
            # 유효한 좌표이면서 상대편 돌이면, 
            # 내 돌 사이에 있는지 확인하고 뒤집기 대기명단(stones)에 추가
            while (
                0 < nr <= N
                and 0 < nc <= N
                and board[nr][nc] == reverse_color(color)
            ):
                temp.append((nr, nc))
                nr += dr[i]
                nc += dc[i]
                
                if 0 < nr <= N and 0 < nc <= N and board[nr][nc] == color:
                    stones.update(temp)
                    break
                

        # 뒤집어야 할 돌이 있다면 뒤집기
        while stones:
            i , j = stones.pop()
            board[i][j] = color

            # 내 돌 사이에 있지 않았는데 돌을 뒤집은 경우
            # 내 돌이 나올때까지 백스텝하면서 다시 돌 뒤집기
            # else:
            #     if board[nr][nc] != color:
            #         while nr - dr[i] == r and nc - dc[i] == c:
            #             board[nr - dr[i]][nc - dc[i]] = reverse_color(board[nr - dr[i]][nc - dc[i]])
            #             nr -= dr[i]
            #             nc -= dc[i]
    
    # 모든 턴이 끝난 후 흑돌과 백돌의 수
    black, white = 0, 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1
    
    print(f'#{tc} {black} {white}')
                
