# 1946: 간단한 압축 풀기 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5PmkDKAOMDFAUq&probBoxId=AZhi468aVsDHBINp&type=PROBLEM&problemBoxTitle=8%EC%9B%94+1%EC%A3%BC%EC%B0%A8%288%2F7%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=5)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열 순회(Array Traversal)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스를 순회합니다.
2.  각 테스트 케이스마다 압축을 푼 원본 문서를 저장할 `document` 리스트를 초기화합니다. 이 리스트는 각 행에 해당하는 문자들을 담는 역할을 합니다.
3.  압축 파일에 대한 정보(`N`개의 알파벳과 숫자 쌍)를 입력받는 `for` 반복문을 실행합니다.
4.  각 쌍에서 알파벳 `alpha`와 반복 횟수 `num`을 분리하고, `num`만큼 `alpha`를 `document` 리스트에 추가하는 과정을 반복합니다.
5.  `document` 리스트의 마지막 행의 길이가 `10`이 되면, 다음 알파벳은 새로운 행에 추가될 수 있도록 `document.append([])`를 사용하여 새 행을 만듭니다.
6.  `document` 리스트의 마지막 행의 길이가 `10` 미만이라면, 현재 행에 알파벳을 추가합니다.
7.  모든 알파벳을 추가한 후, `document` 리스트의 각 행을 순회하며 `"".join()`을 이용하여 문자들을 합쳐 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1946.py](1946.py)