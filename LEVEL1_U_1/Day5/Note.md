# 📙 Note

### Numpy 기초 :: [기초 복습] Python Basics for AI 6강

- numpy

  - 행렬이나 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬의 고성능 과학 계산용 패키지. 이름은 Numerical Python의 약자.
  - Matrix와 Vector와 같은 Array 연산의 사실상 표준.
  - 파이썬은 인터프리터 언어이므로 큰 매트릭스에 대한 빠른 처리 속도를 위해 적절한 패키지 사용 권장.
  - 일반 리스트에 비해 빠르고 메모리 효율적.
  - 반복문 없이 데이터 배열에 대한 처리 지원.
  - 선형대수와 관련된 다양한 기능 제공.

- ndarray

  - np.array 로 선언.
  - 하나의 데이터 타입만 배열에 넣을 수 있다. 다이나믹 타이핑 지원 안 됨.
  - C의 Array를 사용하여 배열 생성.
  - dtype : 배열 전체의 데이터 타입 반환.
  - shape : 배열의 차원 구성을 반환. 0 = scalar, 1 = vector, 2 = matrix, 3 = 3-tensor, n = n-tensor
  - ndim : 차원 수 반환.
  - size : 데이터의 개수 반환.

- Handling shape

  - reshape : Array(배열)의 shape(차원 구성)의 크기 변경. element(원소)의 개수와 순서는 동일. -1은 나머지 값에 맞춰 자동 정렬.
  - flatten : 다차원 Array를 1차원으로 변경.

- Indexing & Slicing

  - 이차원 배열에서 [n, m] 표기법 제공. 앞은 row, 뒤는 col.
  - 행과 열을 나눠서 slicing 가능. Matrix의 부분집합 추출에 유용하다.

- Creation function

  - arange : Array의 범위를 지정하여 값의 리스트 생성.
  - zeros : 0으로 찬 ndarray 생성.
  - ones : 1로 찬 ndarray 생성.
  - empty : 비어있는 ndarray 생성. 메모리 초기화는 되지 않음.
  - identity : 단위 행렬 생성.
  - eye : 시작점을 정한 상태로 대각선이 1인 행렬 생성.
  - diag : 대각행렬의 값을 추출.
  - random sampling : 데이터 분포에 따른 샘플링으로 Array를 생성.

- Operation function

  - sum : 속성값 더하기.
  - axis : 모든 Operation function을 실행할 때 기준이 되는 차원축.
  - mean : 속성값 평균.
  - std :  속성값 표준 편차.
  - concatenate : numpy array를 붙이는 함구. vstack = 배열을 세로로 결합, hstack = 배열을 가로로 결합 등.

- Araay operations

  - numpy는 array간 기본적인 사칙 연산을 지원함.
  - dot : 행렬 기본 연산. Dot product.
  - transpose, T : 전치행렬.
  - Shape이 다른 배열 간 연산 지원. broadcasting. Scalar-Vector 뿐 아니라 Vector-Matrix 연산도 지원.
  - timeit: 주피터 환경에서 코드의 퍼포먼스 체크 함수.
  - 일반적으로 for loop < list comprehension < numpy 로 갈수록 속도가 빠르다. 1억 번 loop 돌 대 약 4배 이상 성능 차이.
  - 그냥 할당에서는 연산 속도 차이 없음.

- Comparisons

  - any : 하나라도 조건에 만족한다면 True
  - all : 모두가 조건에 만족한다면 True
  - numpy는 배열의 크기가 동일할 때 원소 간 비교 결과를 T/F로 반환.
  - logical_and, logical_not, logical_or 등.
  - np.where 절로 조건에 만족하는 값만 추출 가능.
  - argmax & argmin : Array 내 최댓값 또는 최솟값의 인덱스 반환. axis 기반 반환 가능.

- boolean & fancy index

  - boolean index : 특정 조건에 따른 값을 배열 형태로 추출. 비교 연한 함수들을 모두 이용 가능.
  - fancy index : array를 index value를 사용해서 값을 추출하는 방법. a[b]와 a.take(b)는 동일한 동작. 매트릭스 형태도 적용 가능.

- numpy data I/O

  - loadtxt & savetxt : text 데이터를 읽고 저장하는 기능.

---

### Pandas 기초 :: [기초 복습] Python Basics for AI 7-1 ~ 7-2강

- Pandas

  - 구조화된 데이터의 처리를 지원하는 파이썬 라이브러리. 파이썬계의 엑셀. 이름은 Panel Data의 약자.
  - numpy와 결합하여 강력한 스프레드시트 처리 기능 제공.
  - 인덱싱, 연산용 함수, 전처리 함수 제공.
  - 데이터 처리 및 통계 분석을 위해 사용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day05_img00.PNG" alt=""></p>

- 기본 활용

  - Series : DataFrame 중 하나의 Column에 해당하는 데이터의 모음 Object.
  - DataFrame : Data Table 전체를 포함하는 Object. numpy Array와 비슷하나 각 Column이 다른 타입의 정보를 담을 수 있다.
  - Series를 모아서 만든 Data Table = 기본 2차원.
  - Selection & Drop : 기본 인덱스 셀렉션과 다르지 않음. Drop은 .drop으로.

- Dataframe operations

  - 인덱스 기준으로 연산 수행. 겹치는 인덱스가 없을경우 NaN 값으로 반환.
  - Operation types : add, sub, div, mul

- lambda, map, apply

  - series type의 데이터에도 파이썬의 map 함수 사용가능.
  - function 대신 dict, sequence형 자료 등으로 대체 가능. 없는 값은 NaN.
  - replace : Map 함수의 기능중 데이터 변환 기능만 담당. 데이터 변환시 많이 사용.
  - apply : map과 달리, series 전체(column)에 해당 함수를 적용. 입력값이 series 데이터로 입력받아 handling 가능하며 내장 연산 함수 사용 시에도 동일. mean, std 지원. scalar 값 이외에 series값의 반환도 가능하다.

- 판다스 빌트인 functions

  - describe : Numeric type 데이터의 요약 정보를 보여줌.
  - unique : series data의 유일한 값을 list를 반환.
  - sum : 기본적인 연산 지원. 이 외 sub, mean, min, max, conut, median, mad, var 등 동일.
  - isnull : NaN 값이 인덱스 반환.
  - sort_values : column 값 기준으로 정렬.
  - Correlation(corr) & Covariance(cov) : 상관계수와 공분산 반환.

- Groupby

  - split > apply > combine을 거치는 group 연산.
  - 한 개이상의 column을 묶을 수 있음.
  - Groupby 명령의 결과물도 결국은 dataframe이므로 두 개의 column으로 groupby를 할 경우, index가 두 개 생성.
  - unstack() : Group으로 묶인 데이터를 matrix 형태로 전환.
  - swaplevel() : Index level을 변경.
  - Index level 을 기준으로 기본 연산 수행 가능.
  - grouped : Groupby에 의해 Split된 상태를 추출. 특정 key값을 가진 그룹의 정보만 추출하는 것도 가능. 추출된 그룹 정보엔 Aggregation, Transformation, Filtration 이렇게 세 가지 유형의 apply가 가능하고 각 기능은 요약 통계정보, 해당 정보 변환(요약 정보 아님, 개별 데이터 변환 지원), 특정 정보 제거(필터링, boolean 조건 필요).

- Pivot table & Crosstab

  - Pivot table : 엑셀 표 형태.
  - Crosstab : Pivot table의 특수 형태. 두 칼럼에 교차 빈도, 비율, 덧셈 등을 구할 때 사용.

- Merge & Concat

  - Merge : 고유값 기준으로 두 데이터를 하나로 합침. like join in SQL.
  - Concat : 같은 형태의 데이터를 단순히 합침.

- Persistence

  - Database connection : Data loading시 db connection 기능을 제공.
  - XLS persistence : Dataframe의 엑셀 추출 코드.
  - Pickle persistence : 가장 일반적인 파이썬 파일 persistence.

# ✏️ Doodle

- 첫 주의 마무리. 남은 시간엔 미리 들었던 강의의 복습, 선택 과제 작성. 주말은 참고 코드와 참조 강의들을 리뷰할 예정. 앞으로의 학습량은 이와 비슷하거나 늘어날거라고 한다. 중간 기말 시험은 없지만 유사한 대회가 있어서 여유부릴 시간이 없다. 일단 금요일은 이르게 마치기. 오늘의 끝은 고흐.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Vincent_van_Gogh_1890_Wheat_Field_with_Crows.jpg"></p>
<p align="center">Vincent van Gogh, &ltWheat Field with Crows&gt, 1890. Oil on canvas, 50.2x103cm.</p>

- Day 5 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day4/Note.md "Day4 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day6/Note.md "Day6 Note")
