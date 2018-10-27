# Data Extraction App

## 개요

방대한 분량의 데이터셋을 읽어들여 원하는 값을 추출하는 어플리케이션입니다. 주어진 csv 파일이 180MB 가까이 하는 거대한 데이터여서 일반적인 방식으로 파일을 읽어들여서는 퍼포먼스가 너무 떨어질 것 같다는 우려가 있었습니다. 그래서 python에서 데이터 분석에 많이 쓰이는 pandas 패키지를 이용하기로 했습니다.

## 기술 스펙
- python 3.7.0
- pandas 0.23.3

## 파일 구조

```
.
├ main.py // 실행 파일
└ requirements.txt // 의존성 패키지 문서
```

## 설치 및 실행

전역 python 혹은 가상환경 python을 설치한 뒤, 소스코드 디렉터리로 들어갑니다. 그리고 `requirements.txt`를 이용해 의존성 패키지를 설치합니다.

```
$ cd data-extraction
$ pip install -r requirements.txt
```

`test.csv` 파일을 디렉터리 안에 붙여넣기 한 다음, `main.py`를 실행합니다.

```
$ python main.py
```

## 사용법

특별한 사용법은 없습니다. 파일을 실행하면 모든 결과값과 총 실행 시간이 출력됩니다.

```
start_time: 2018-10-28 05:15:20.366888

Total number of rows: 4999999


Max value of each columns:
p0    99.0
p1    99.0
p2    99.0
p3    99.0
p4    99.0
p5    99.0
p6    99.0
p7    99.0
p8    99.0
p9    99.0
dtype: float64


Min value of each columns:
p0    0.0
p1    0.0
p2    0.0
p3    0.0
p4    0.0
p5    0.0
p6    0.0
p7    0.0
p8    0.0
p9    0.0
dtype: float64


Average value of each columns:
p0    49.508164
p1    49.496426
p2    49.505297
p3    49.482869
p4    49.507895
p5    49.512065
p6    49.510024
p7    49.504619
p8    49.504697
p9    49.504222
dtype: float64


Standard deviation value of each columns:
p0    28.854969
p1    28.874938
p2    28.859707
p3    28.871747
p4    28.868251
p5    28.846377
p6    28.876638
p7    28.871010
p8    28.857494
p9    28.866160
dtype: float64


Median value of each columns:
p0    50.0
p1    49.0
p2    50.0
p3    49.0
p4    50.0
p5    50.0
p6    50.0
p7    50.0
p8    50.0
p9    50.0
dtype: float64

-----Total elapsed time: 12.64737 seconds-----
```

총 실행시간은 10~12초 정도로 측정되는 편입니다. 이는 컴퓨터 환경에 따라 달라질 수 있습니다.
