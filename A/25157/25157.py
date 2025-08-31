# 25157. 소 잃고 외양간 고치기

def calculate_loss(day, curr_loss, broken, repairing):
    # 공격받은 외양간(취약 상태)만 수리할 수 있다.
    # 한번 수리하기 시작한 외양간은 중간에 멈출 수 없다.
    # 수리가 끝난 외양간은 더이상 취약 상태가 아니다.
    # 취약 상태인 외양간을 저장하는 큐(선입선출)
    global min_loss

    # 밤 사이 생긴 손실 계산
    # broken.add(attack[day-1])
    for cowshed in broken:
        curr_loss += loss[cowshed]

    # 종료 조건
    if day == M:
        min_loss = min(min_loss, curr_loss)
        return
    
    # 가지치기
    elif curr_loss >= min_loss:
        return

    # --- 아침이 밝았습니다. 외양간 고치기 시작. ---
    repairing['remain'] -= 1

    # 수리가 끝났다면 취약 상태에서 제거
    if repairing['status'] and repairing['remain'] <= 0:
        broken.remove(repairing['cowshed'])
        repairing['status'] = False
        
    # 수리 중인 외양간이 없다면, 수리를 시작하지.
    if not repairing['status']:
        for cowshed in broken:
            repairing = { 'status': True, 'cowshed': cowshed, 'remain': repair[cowshed] }
            calculate_loss(day + 1, curr_loss, broken.union({attack[day]}), repairing)
            continue
    
    calculate_loss(day + 1, curr_loss, broken.union({attack[day]}), repairing)


T = int(input())
for tc in range(1, T+1):
    # 외양간의 수 N, 총 기간 M
    N, M = map(int, input().split())
    
    # 각 외양간의 일일 손실량 loss와 수리 기간 repair    
    loss = [0] * (N + 1)
    repair = [0] * (N + 1)
    for i in range(1, N+1):
        loss[i], repair[i] = map(int, input().split())

    # d번째 날 밤에 공격받는 외양간의 번호 attack[d-1]
    attack = []
    for i in range(M):
        attack.append(int(input()))

    # 총 손실의 최소값 초기화
    min_loss = sum(loss) * M

    repairing = { 'status': False, 'cowshed': 0, 'remain': 0 }
    calculate_loss(1, 0, {attack[0]}, repairing)

    print(f'#{tc} {min_loss}')
