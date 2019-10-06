# 판다스로 EDA하기

- 데이터를 처음 접하면 EDA 과정을 거치는 것은 당연한 수순

- 일반적으로 EDA 하는 과정은 아래와 같음

  > - `head()`, `tail()`, 또는 `sample()`을 활용하여 데이터의 전반적인 형태 파악
  > - `<data>.describe()`를 활용하여 기초 통계 파악
  > - `<data>.corr()` 을 활용하여 변수간 상관관계 파악
  > - 외 기타 시각화를 통해 데이터 파악

- 위의 모든 과정이 `pandas_profiling` 라이브러리 하나면 해결

___

- `pandas_profiling`은 `pandas`와는 별개의 라이브러리로 `pip`를 통해 설치가 필요

- 다시 돌아와서 `pandas_profiling`으로 EDA를 하려면 아래 한줄로 해결 가능:

  ```python
  import pandas as pd
  import pandas_profiling
  pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv').profile_report()
  ```

  ![](https://miro.medium.com/max/600/1*bF8cMGoXOeDXKmKqqVsHHg.gif)

- Descriptive anlaysis부터 distribution, correlation, missing value 등 주요한 정보를 리포트로 반환

- `html`로 리포트만 따로 저장하려면 아래와 같이 명령어 기입

  ```python
  profile = df.profile_report(title='Pandas Profiling Report')
  profile.to_file(output_file="output.html")
  ```

  