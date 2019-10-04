# 파이썬 필수스킬

> Python을 접하게 되면서 `Pandas`나 `Numpy`같이 훌륭한 라이브러리를 알게되는 것은 당연하다. 이런 라이브러리들이 삶을 윤택하게 해주는 것은 당연하지만, 너무 일찍 알게된 것은 아닐까? Python이 기본적으로 제공하는 강력한 기능 3가지에 대해서 알아보자.
>
> 1. `Lambda Function`, 2. `List Comprehension`, 3. Zip

## 1. Lambda Function

- `Lambda Function`은 가벼운 `User Defined Function`을 손쉽게 만들고 ad-hoc 처리를 용이하게 만들어줌

- **한줄로 손쉽게 정의**내리는 것을 목적으로 별도의 `def`이 필요 없음

- 제곱 연산을 수행하는 `UDF`를 예제로 들면 다음과 같음:

  ```python
  # regular function
  def square_with_def(x):
      output = x ** 2
      return output
  
  # lambda function
  square_with_lambda = lambda x: x **2
  
  ## implementation
  print('4 square with def : {}'.format(square_with_def(4)))
  print('4 square with lambda : {}'.format(square_with_lambda(4)))
  
  >>> 4 square with def : 16
  >>> 4 square with lambda : 16
  ```

- 당연히 결과는 같지만, `lambda`를 활용한 `function`이 훨씬 간결하고 손쉽게 정의 가능

- 짝수/홀수를 판별하는 `UDF` 예제를 하나 더 살펴보면 다음과 같음:

  ```python
  # regular function
  def is_even_with_def(x):
      if x % 2 ==0:
          return True
      else:
          return False
  
  # lambda function
  is_even_with_lambda = lambda x: x % 2 == 0
  ```

- 결과는 생략하였지만  같은 결과를 출력하게 됨

- 두 `UDF` 간의 정의 과정을 살펴보면 복잡한 경우는`regular function`이 효과적일 수 있겠지만, 간단하거나 ad-hoc 함수의 경우 `lambda function`을 활용해 보는 것도 상당한 시간 절약이 가능할 것

## 2. List Comprehensions

- `List Comprehensions`는 한줄에 `for-loop`를 돌리는 방법임

- 개인적으로도 Feature 전처리 때 자주 쓰는 기능이며 좀더 설명하기 전에 바로 예제를 통해 사용법을 보는 것이 더 나을 것 같음:

  ```python
  lst = ['Acer', 'Asus', 'Lenovo', 'HP']
  
  # regular function
  def starts_with_a(lst):
      valids = []
   
      for word in lst:
          if word[0].lower() == 'a':
              valids.append(word)
   
      return valids
   
   
  # list comprehension
  lst_comp = [word for word in lst if word[0].lower() == 'a']
  
  # results
  print('starts_with_a: {}'.format(starts_with_a(lst)))
  print('list_comprehension: {}'.format(lst_comp))
  >>> starts_with_a: ['Acer', 'Asus']
  >>> list_comprehension: ['Acer', 'Asus']
  ```

- `lst_comp`를 보면 반복할 object, 반복할 object가 담겨있는 리스트, 그리고 if문으로 조건을 거는 것까지 한줄에 담아서 for문을 간략하게 생성

## 3. Zip

- `Zip`의 경우 빈번하게 사용되는 내장함수는 아니지만, 매우 유용한 기능 중 하나

- `Zip`은 **2개 혹은 그 이상의 리스트를 동시에 반복할수 있게 해주며** 날짜나 시간 데이터를 다룰 때 매우 유용 (동일한 기간동안 동일간격으로 데이터가 존재)

- 예를 들어 몇주동안 2개의 매장에서 발생하는 매출을 비교할 때 아래와 같이 코딩하는 것이 가능

  ```python
  sales_north = [350, 287, 550, 891, 241, 653, 882]
  sales_south = [551, 254, 901, 776, 105, 502, 976]
  
  for s1, s2 in zip(sales_north, sales_south):
      print(s1 — s2)
      
  >>> -201
      33
      -351
      115
      136
      151
      -94
  ```

- 동일한 로직을 for문으로 구현하는 것도 가능하지만, `Zip` 기능을 활용하여 매우 간단하게 동일 기능 구현



참조: [3 Essential Python Skills for Data Scientists](https://towardsdatascience.com/3-essential-python-skills-for-data-scientists-b642a1397ae3)

