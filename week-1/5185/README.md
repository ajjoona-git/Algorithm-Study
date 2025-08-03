# 5185: 이진수 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTtiyIqd_wDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **진법 변환**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  각 테스트 케이스마다 16진수의 자리 수 `N`과 16진수 문자열 `hexa`를 입력받습니다.
3.  16진수 문자열 `hexa`를 순회하면서 각 문자를 4자리 이진수로 변환해야 합니다.
4.  16진수 문자를 `10`진수로 변환하기 위해 Python의 내장 함수 `int(문자, 16)`을 활용합니다. 이 함수는 'A'와 같은 문자를 자동으로 10 이상의 정수로 변환해 줍니다.
5.  변환된 10진수 값을 2진수로 변환하는 과정을 반복합니다.
    * 4자리 이진수를 얻기 위해 4번 반복하는 `for`문을 사용합니다.
    * 10진수 값을 2로 나눈 나머지를 이진수의 가장 뒤쪽부터 저장합니다.
    * 10진수 값을 몫으로 갱신하는 과정을 반복하여 이진수 한 자리를 완성합니다.
6.  변환된 4자리 이진수를 문자열로 합쳐서 최종 결과 리스트에 추가합니다.
7.  모든 16진수 문자에 대한 변환이 끝나면, 결과 리스트를 `"".join()`을 이용하여 하나의 문자열로 합쳐 출력 형식에 맞게 출력합니다.


---

## 💻 코드
* [5185.py](5185.py)