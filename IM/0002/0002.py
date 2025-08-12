# 기출 복원. 채점 시스템 만들기

import sys
sys.stdin = open("input.txt")


def grade(answers):
    """
    학생의 답안(answers)에서 얻을 수 있는 점수를 반환하는 함수
    
    처음으로 문제를 맞으면 1점, 그 다음 연속으로 답을 맞으면 앞 문항이 얻은 점수에 + 1 점을 추가하고,
    틀린경우 다시 0점으로 초기화하여 같은 방식으로 계산한다.
    """
    score = 0  # 해당 학생의 점수
    subscore = 0  # 한 문제당 점수

    # 답안을 순회하면서 전체 점수를 계산한다.
    for i, answer in enumerate(answers):
        if answer == correct_answers[i]:  # 정답
            subscore += 1
        else:  # 오답
            subscore = 0
        # 현 문항에서 얻은 점수를 전체 점수에 추가한다.
        score += subscore

    return score



T = int(input())
for tc in range(1, T+1):
    # N: 학생 수, M: 문항 수
    N, M = map(int, input().split())
    # correct_answers: M개 문항에 대한 답안 리스트
    correct_answers = tuple(map(int, input().split()))
                           
    # scores: 학생들의 점수 리스트
    scores = [0] * N

    # N명의 학생들의 점수를 계산한다.
    for i in range(N):
        # answers: M개 문항에 대한 학생의 답안 리스트
        answers = list(map(int, input().split()))
        scores[i] = grade(answers)
    
    # 최고점과 최저점의 차이를 출력한다.
    print(f"#{tc} {max(scores) - min(scores)}")
