# 4861: 회문 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQQXcKQHkDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **문자열 슬라이싱**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스를 순회합니다.
2.  각 테스트 케이스마다 글자판의 크기 `N`과 회문의 길이 `M`을 입력받고, `N x N` 크기의 글자판 `letters`를 2차원 리스트로 저장합니다.
3.  **회문 판별 함수** `is_palindrome(str)`을 정의하여, 주어진 문자열이 회문인지 여부를 판별합니다.
    * 문자열의 앞부분과 뒷부분을 절반만큼 비교하여 일치하면 `True`, 아니면 `False`를 반환합니다.
4.  글자판의 **가로 방향**으로 길이가 `M`인 모든 문자열을 탐색합니다.
    * `letters` 리스트를 순회하며 `letters[i][j:j+M]`과 같이 문자열을 슬라이싱하여 회문인지 확인합니다.
5.  **세로 방향**으로도 탐색하기 위해, `zip(*letters)`을 활용하여 행과 열을 바꾼 새로운 2차원 리스트 `letters_col`을 생성합니다.
    * 이 `letters_col`을 가로 문자열 탐색과 동일한 방식으로 순회하며 회문을 찾습니다.
6.  가로 또는 세로 탐색 과정에서 회문이 발견되면, 해당 회문 문자열을 `result` 변수에 저장합니다.
7.  모든 탐색이 끝나면 `result`에 저장된 회문 문자열을 `"".join(result)`로 합쳐서 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4861.py](4861.py)