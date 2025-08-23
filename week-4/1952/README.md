# 1952. 수영장

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5PpFQaAQMDFAUq&probBoxId=AZjE2kOaAXDHBIO0&type=PROBLEM&problemBoxTitle=8%EC%9B%94+3-4%EC%A3%BC%EC%B0%A8%288%2F28%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=4)

## 💡 접근 방식

### 1. 사용 알고리즘
* **깊이 우선 탐색 (DFS) / 완전 탐색 (Brute-force Search)**
* **재귀 (Recursion)**
* **백트래킹 (Backtracking) / 가지치기 (Pruning)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 1월부터 12월까지 각 달에 대해 가능한 모든 이용권 구매 조합을 탐색하여 최소 비용을 찾는 문제로 접근합니다. 이는 모든 경우의 수를 탐색하는 완전 탐색(또는 DFS) 방식에 적합합니다.
2.  **재귀 함수 설계**: `calc_price(month, price)`라는 재귀 함수를 정의합니다. 이 함수는 `month`월까지 `price`의 비용이 누적되었을 때, 남은 기간(12월까지)의 최소 이용 요금을 계산하는 역할을 합니다.
3.  **종료 조건 (Base Cases)**:
    * **12월까지 계산 완료**: `month`가 13월 이상이 되면, 1년치 계획에 대한 하나의 완전한 비용 계산이 끝난 것입니다. 이때 계산된 총비용(`price`)을 현재까지의 최소 비용(`min_price`)과 비교하여 더 작으면 갱신합니다.
    * **가지치기 (Pruning)**: 재귀 호출 중간에 현재까지 누적된 비용(`price`)이 이미 `min_price`보다 크거나 같아진 경우, 더 이상 탐색을 진행해도 최소 비용을 찾을 수 없으므로 해당 경로의 탐색을 즉시 중단하고 반환(return)합니다.
4.  **재귀 호출 (탐색 확장)**:
    * 현재 `month`에 이용 계획이 없다면, 비용 추가 없이 다음 달로 넘어갑니다 (`calc_price(month + 1, price)`).
    * 이용 계획이 있다면, 현재 달에 대해 다음 4가지 이용권 구매 경우의 수를 모두 재귀적으로 호출하여 탐색합니다.
        1.  **1일권**: `(1일권 요금 * 이용일수)`를 `price`에 더하고, 다음 달(`month + 1`)로 넘어갑니다.
        2.  **1달권**: `1달권 요금`을 `price`에 더하고, 다음 달(`month + 1`)로 넘어갑니다.
        3.  **3달권**: `3달권 요금`을 `price`에 더하고, 3달 뒤(`month + 3`)로 넘어갑니다.
        4.  **1년권**: `1년권 요금`을 `price`에 더하고, 12달 뒤(`month + 12`)로 넘어갑니다. (이는 사실상 탐색을 종료하고 `min_price`를 갱신하는 효과를 줍니다.)
5.  **초기화 및 실행**: `min_price`를 매우 큰 값(또는 1년권 요금)으로 초기화한 뒤, `calc_price(1, 0)`을 호출하여 1월부터 탐색을 시작합니다. 모든 탐색이 끝나면 `min_price`에 최종 최소 비용이 저장됩니다.

---

## 💻 코드
* [1952.py](1952.py)