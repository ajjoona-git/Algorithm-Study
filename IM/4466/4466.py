# 4466. 최대 성적표 만들기

def select_sort(arr, N, K):
    """길이가 N인 1차원 배열(arr)을 내림차순으로 K번 정렬하여 반환하는 함수"""
    for i in range(K):
        max_idx = i
        for j in range(i, N):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # K번째 값까지 내림차순으로 정렬
    select_sort(scores, N, K)

    # 총점의 최대값
    max_score = 0
    for score in scores[:K]:
        max_score += score

    print(f'#{tc} {max_score}')