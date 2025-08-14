# 6190. 정곤이의 단조 증가하는 수 | D3

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열 순회(Array Traversal)** 및 **단조 증가 검사**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 배열의 크기 `N`과 숫자 리스트 `numbers`를 입력받습니다.
2.  이 문제는 두 수의 곱 중 단조 증가하는 수 중에서 가장 큰 값을 찾는 문제입니다.
3.  `for` 반복문을 사용하여 `numbers` 리스트에서 두 개의 다른 숫자 `numbers[i]`와 `numbers[j]`를 선택합니다.
4.  선택된 두 숫자의 곱을 `number` 변수에 저장하고, 이 숫자가 단조 증가하는 수인지 확인합니다.
5.  숫자가 단조 증가하는지 확인하기 위해, `str(number)`로 문자열로 변환한 후 각 자릿수를 리스트에 저장합니다.
6.  각 자릿수를 순회하면서 `digits[k] > digits[k+1]`인 경우(단조 증가하지 않는 경우) `break`를 통해 반복문을 종료합니다.
7.  `break`가 실행되지 않고 반복문이 정상적으로 완료되면, 해당 `number`는 단조 증가하는 수이므로 `results` 리스트에 추가합니다.
8.  모든 두 숫자의 곱에 대한 검사가 끝난 후, `results` 리스트가 비어있지 않다면 `max(results)`로 가장 큰 값을 찾아 출력합니다.
9.  `results` 리스트가 비어있다면, 단조 증가하는 수가 없다는 뜻이므로 `-1`을 출력합니다.

---

## 💻 코드
* [6190.py](6190.py)


---
## 임시 변수 설정의 중요성
### 초기 코드
테스트 케이스 50개 중 9개 정답

```python
# 두 수의 곱이 단조 증가하는 수인지 확인
for i in range(N):
    for j in range(i+1, N):
        # 두 수의 곱
        number = numbers[i] * numbers[j]
        # 각 숫자의 자릿수
        digits = [int(i) for i in str(number)]
        for i in range(len(digits)-1):
            # 단조 증가하지 않음
            if digits[i] > digits[i+1]:
                break
        else:
            results.append(number)
```

### 문제 해결
임시 변수 `i`가 중첩돼서 제대로 연산되지 않음!!!!!

```python
# 두 수의 곱이 단조 증가하는 수인지 확인
for i in range(N):
    for j in range(i+1, N):
        # 두 수의 곱
        number = numbers[i] * numbers[j]
        # 각 숫자의 자릿수
        digits = [int(char) for char in str(number)]
        for k in range(len(digits)-1):
            # 단조 증가하지 않음
            if digits[k] > digits[k+1]:
                break
        else:
            results.append(number)
```