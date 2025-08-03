# 4864: 문자열 비교 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQRytKQJ0DFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **문자열 검색(String Search)**
* **구현(Implementation)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  문자열 `str1`이 `str2`에 포함되는지 확인하는 기능을 **함수 `is_included`로 정의**하여 코드의 가독성을 높이고 재사용이 가능하게 합니다.
3.  `is_included(str1, str2)` 함수는 파이썬의 **`in` 연산자**를 활용합니다. `if str1 in str2:`를 통해 `str1`이 `str2`의 부분 문자열인지 간결하게 판별할 수 있습니다.
4.  `str1`이 `str2`에 포함되면 `1`을, 포함되지 않으면 `0`을 반환하도록 함수를 구현합니다.
5.  각 테스트 케이스마다 `str1`과 `str2`를 입력받습니다.
6.  정의한 `is_included` 함수를 호출하여 결과를 `result` 변수에 저장합니다.
7.  테스트 케이스 번호와 함께 `result` 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [4864.py](4864.py)