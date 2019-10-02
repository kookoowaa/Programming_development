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



## 3. Zip





참조: [3 Essential Python Skills for Data Scientists](https://towardsdatascience.com/3-essential-python-skills-for-data-scientists-b642a1397ae3)

