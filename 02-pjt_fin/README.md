# 02-pjt

## problem review

## #A. 데이터 전처리
+ pandas를 이용하여 csv 파일을 읽어 올 수 있다.
+ pandas를 이용한 데이터 처리가 기존의 방법보다 빠른 속도를 제공해 준다고는 하는데, 오늘의 프로젝트 과정에서는 확인할 수 없었다.

## #B. 데이터 전처리–2021년 이후의 종가 데이터 출력하기
+ `.to_datetime` 를 이용하여, Date의 타입을 변경한 뒤,
+ pandas로 전처리된 데이터와 matplotlib의 간단한 기능들을 이용하여, 시각화자료를 만들 수 있습니다.
```py
  plt.plot(df['Date'], df['Close'])
# 그래프 제목 설정
plt.title('NFLX Close Price')
# x축 레이블 설정
plt.xlabel('Date')
# y축 레이블 설정
plt.ylabel('Close Price')
# x 축 설정(회전시키기)
plt.xticks(rotation=45)
# 그래프 표시
plt.show()
```

## #C. 데이터 분석 –2021년 이후 최고, 최저 종가 출력하기
+ `max()` : 최대값을 출력해 줍니다.
+ `df.loc[]` : 원하는 데이터를 선택할 수 있습니다.
```py
max_price = max(df.loc[:, 'Close'])
```
## #D. 데이터 분석 -2021년 이후 월 별 평균 종가 출력하기
+ `pd.DatetimeIndex` : Date 값을 list로 생성
+ `idx.to_period("M")` : Date의 '일' 제거한 '월' 데이터로 변경
+ `groupby(midx)` : 변경된 '월' >> '월'별로 데이터 그룹화
+ `numeric_only=True` : 평균값에 대해 df에 반영 
+ `reset_index()` : 그룹화된 출력값 그대로 데이터프레임 생성
+ `.astype(str)` : 이후 matplotlib을 통한 그래프를 그리기 위해 str type으로 변경
```py
datetimeIndex = pd.DatetimeIndex(df['Date'])
idx = pd.to_datetime(datetimeIndex)
midx = idx.to_period("M")
ef = df.groupby(midx).mean(numeric_only=True).reset_index()

ef['Date'] = ef['Date'].astype(str)
```
## #E. 데이터 시각화 –2022년 이후 최고, 최저, 종가 시각화하기
+ close , low , high 각각에 대한 그래프
+ 그외 내용은 앞선 내용과 동일
```py
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['High'], label='High')
```
## #What I learn today
Using Pandas, I efficiently read CSV files and understood that it offers faster data processing compared to traditional methods, though this project's scope didn't allow me to fully experience the speed improvement. This project helped me grasp the basic flow of data preprocessing, analysis, and visualization. Additionally, I improved my skills in effectively processing and visualizing data using the various features of Pandas and Matplotlib.

