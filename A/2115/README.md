# 2115. 벌꿀채취

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5V4A46AdIDFAWu&probBoxId=AZiiM-4KAVbHBIT9&type=PROBLEM&problemBoxTitle=A%ED%98%95_%EC%B6%94%EC%B2%9C+%ED%95%99%EC%8A%B5+%EC%9E%90%EB%A3%8C&problemBoxCnt=24&&&&&&)

## 💡 접근 방식

### 1. 사용 알고리즘
* **완전 탐색 (Brute-force Search)**
* **조합 (Combinations)**

### 2. 문제 풀이 과정
1.  **문제 분할**: 문제를 두 단계로 나누어 접근합니다.
    * **Sub-problem**: 한 명의 일꾼이 M개의 벌통이 있는 특정 지역에서 얻을 수 있는 **최대 수익**을 계산하는 방법.
    * **Main-problem**: 두 명의 일꾼이 벌통을 채취할 **겹치지 않는 두 지역**을 선택하는 모든 경우의 수를 탐색하여, 두 수익의 합이 최대가 되는 경우를 찾는 것.

2.  **Sub-problem 해결 (`get_best_combo` 함수)**
    * M개의 벌통으로 이루어진 한 구역(`workspace`)이 주어졌을 때, 채취할 수 있는 꿀의 부분 집합을 모두 고려해야 합니다.
    * `itertools.combinations`를 사용하여 1개부터 M개까지의 벌통을 선택하는 모든 조합을 생성합니다.
    * 각 조합에 대해, 채취한 꿀의 총합이 용량(`C`)을 초과하는지 확인합니다.
    * 용량을 초과하지 않는 유효한 조합에 대해서만 수익(`각 꿀의 양의 제곱의 합`)을 계산하고, 이 중 가장 큰 값을 해당 구역의 최대 수익으로 결정하여 반환합니다.

3.  **Main-problem 해결 (전체 탐색)**
    * **완전 탐색**을 통해 두 일꾼이 벌통을 채취할 두 구역을 선택하는 모든 경우의 수를 탐색합니다.
    * 첫 번째 일꾼의 벌통 채취 구역(시작점 `(r1, c1)`)을 이중 `for`문으로 모두 선택합니다.
    * 각 `(r1, c1)`에 대해 `get_best_combo` 함수를 호출하여 첫 번째 일꾼의 최대 수익(`profit1`)을 계산합니다.
    * 두 번째 일꾼의 채취 구역(시작점 `(r2, c2)`)을 다시 이중 `for`문으로 탐색합니다. 이때 **첫 번째 일꾼의 구역과 겹치지 않도록** 시작점을 조정합니다.
        * 만약 같은 행(`r1 == r2`)이라면, 두 번째 일꾼의 시작 열(`c2`)은 `c1 + M`부터 시작합니다.
        * 다른 행이라면, `0`열부터 시작해도 됩니다.
    * 두 번째 일꾼의 최대 수익(`profit2`)도 같은 방식으로 계산한 후, 두 수익의 합(`profit1 + profit2`)을 기존의 최대 수익(`max_profit`)과 비교하여 갱신합니다.
    * 모든 조합을 탐색하고 나면 `max_profit`에 저장된 값이 최종 결과가 됩니다.


---

## 💻 코드
* [2115.py](2115.py)