

# :orange_book: Note 
### 파이썬 AI 개발 환경 준비하기 :: [기초 복습] Python Basics for AI 1-1강 ~ 1-3강

- 기본적인 컴퓨터 시스템 From a Software Aspects

  - 컴퓨터 OS(Operating System) : 운영체제. 프로그램 동작을 위한 구동 환경.
  - 파일 시스템 : OS에서 파일을 저장하는 트리구조 저장 체계. 파일은 디렉토리와 파일로 구분.
  - 터미널 환경 : 콘솔창. CLI 화면.
  - 기본 윈도우 CMD 명령어(shell 명령어) : CD(cd), CLS(clear), COPY(cp), DEL(rm), DIR(ls)

- 파이썬 개요

  - 1991년 귀도 반 로섬이 발표했다.
  - 플랫폼 독립적인 인터프리터 언어 and 객체 지향 and 동적 타이핑 언어. 초기엔 C로 구현했다.
  - 동적 타이핑 언어이므로 프로그램 실행 시점에 데이터에 대한 타입을 결정.
  - 이해하기 쉬운 문법.
  - Life is short. You need Python.

- 파이썬 코딩 환경 구성

  - Miniconda and VSCode

### 파이썬 기초 문법 :: [기초 복습] Python Basics for AI 2-1강 ~ 2-4강

- 변수와 리스트
  - 변수는 데이터를 담는 그릇. 자료형으로 구분.
  - 리스트 : 시퀀스 자료형. 이중 리스트 = 행렬
  - Python의 리스트 : 다양한 자료형을 하나의 리스트에 삽입 가능. 패킹 & 언패킹 가능. 기본적으로 타 언어 리스트보다 유연하다.

- Function and Console I/O
  - 함수(Function) : 어떤 일을 수행하는 코드의 덩어리. 코드를 논리적인 단위로 분리. 캡슐화에 필수적. 함수 이름, 파라미터, 수행문, 리턴값으로 구성. 파라미터와 반환값은 각각 있거나 없을 수 있다.
  - Function type hints : 함수 사용자의 이해를 돕기 위한 장치. 시스템 전체적인 안정성 확보에 비필수적인 필수 요소.
  - Docstring : 함수 사용자의 이해를 돕기 위한 장치. 일반적으로 세 개의 따옴표로 Docstring 영역을 표시한다.
  - 콘솔창 입출력 : input()과 print()가 기본.
  - Python의 출력 : 기본적인 출력 외에 %string, format, f-string 등을 지원한다.

- 조건문과 반복문
  - 조건문과 반복문의 기본 개념은 모든 언어가 공유하는 그것. 파이썬도 다르지 않다. 다만 조금 더 유연한 for문. 생각하는 대로 적어라.
  - 재귀함수의

- 문자열 데이터
  - 문자열 데이터(String data) : 시퀀스 자료형. 영문자 한 글자는 1byte의 메모리 공간을 사용.
  - Python의 기본 입력은 String. 마찬가지로 유연하게 사용할 수 있다.

- 변수의 범위
  - 지역변수(Local variable) : 함수 내에서만 사용.
  - 전역변수(Global bariable) : 프로그램 전체에서 사용. 함수 내에서 새로 선언하면 지역변수로 대체. 함수 내에서 전역변수로 사용 시 global 키워드 사용 필수.

- 함수 작성 가이드 라인 (권장)
  - 함수는 가능하면 짧게 작성할 것.
  - 함수 이름에 함수의 역할, 의도가 명확히 드러나게 작성할 것.
  - 하나의 함수에는 유사 역할 코드만 포함할 것.
  - 인자로 받은 값 자체를 바꾸지 말 것. (임시 변수 사용)
  - 공통으로 사용되는 코드는 함수로 변환할 것.
  - 복잡한 수식과 조건을 식별 가능한 이름을 가진 함수로 변환할 것.
  - "컴퓨터가 이해할 수 있는 코드는 어느 바보나 다 짤 수 있다. 좋은 프로그래머는 사람이 이해할 수 있는 코드를 짠다. - 마틴 파울러 -"

### 벡터가 뭐에요? :: [기초 복습] AI Math 1강

- 벡터(Vector)
  - 숫자를 원소로 가지는 리스트(list) 또는 배열(array).
  - 공간에서 한 점. (1차원, 2차원, n차원)
  - 원점으로부터 상대적 위치.
  - 벡터에 숫자를 곱하면 길이만 변한다.
  - 같은 모양을 가질 때 덧셈, 뺄셈, 성분곱(Hadamard product)계산을 할 수 있다.
  - 두 벡터의 덧셈은 다른 벡터로부터 상대적 위치이동을 표현.

- 벡터의 노름(norm)
  - 원점에서부터의 거리.
  - L1-노름은 각 성분의 변화량의 절댓값을 모두 더한 것.
  - L2-노름은 피타고라스 정리를 이용해 유클리드 거리를 계산한 것. (각 성분의 변화량 제곱의 합의 1/2승)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day01_img00.PNG" alt="노름 계산식"></p>

-
  - 노름 종류에 따라 기하학적 성질이 달라진다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day01_img01.PNG" alt="노름 종류에 따른 기하학적 성질"></p>

-
  - 두 벡터 사이 거리는 벡터의 뺄셈을 이용하여 구한다.
  - 두 벡터 사이 거리는 제2 코사인 법칙으로 구한다. (내적) Proj(x)의 길이 = ||x||cosθ

### 행렬이 뭐에요? :: [기초 복습] AI Math 2강

- 행렬(Matrix)
  - 벡터를 원소로 가지는 2차원 배열.
  - 행(row)과 열(column)이라는 인덱스를 가진다.
  - 행렬의 특정 행(열)을 고정하면 행(열)벡터.
  - 전치행렬(Transpose matrix) : 행과 열의 인덱스가 바뀐 행렬. (X^T)
  - 벡터는 공간에서 한 점. 행렬은 여러 점들.
  - 같은 모양을 가질 때 덧셈, 뺄셈, 성분곱(Hadamard product)계산을 할 수 있다.
  
- 행렬의 곱셈
  - 행렬 곱셈(Matrix multiplication)은 i번째 행벡터와 j번째 열벡사 사이의 내적을 성분으로 가지는 행렬 계산. 넘파이의 내적은 수학에서 내적과 다름.
  - 행렬곱을 통해 벡터를 다른 차원의 공간으로 보낼 수 있다.
  - 행렬곱을 통해 패턴을 추출할 수 있고 데이터를 압축할 수 있다.
  - 모든 선형변환은 행렬곱으로 계산 가능.

- 역행렬(Inverse matrix)
  - 행렬 A의 역행렬은 A^-1로 표기.
  - AA^-1 = A^-1A = I(항등행렬)
  - 어떤 행렬 A의 연산을 거꾸로 되돌리는 행렬이 역행렬.
  - 역행렬은 행과 열 숫자가 같고 행렬식(determinant)이 0이 아닌 경우에만 계산 가능.
  - 역행렬을 계산할 수 없다면 유사역행렬(pseudo-inverse) 또는 무어-펜로즈(Moore-Penrose) 역행렬(A^+)을 이용한다.

- 선형회귀분석
  - np.linalg.pinv를 이용하여 연립방정식의 해를 구할 수 있다.
  - np.linalg.pinv를 이용하여 데이터를 선형모델로 해석하는 선형회귀식을 찾을 수 있다.
  - 유사 역행렬을 이용하여 y에 근접하는 y' 추출 가능.

# :pencil2: Doodle

  - 프리코스내용과 같은 강의. 파이썬 기본 문법보다 파이썬만의 고유 특성, 함수 작성 권장 가이드라인에 집중하여 다시 한번 훑었다. 반면 선형대수는 아무리 봐도 모자람이 없다. 본 지 벌써 몇년 짼데 아직도 어색하다. 아마 영원히 그럴 것. 기존엔 수기로만 작성했던 식이지만 더 빠른 답을 낼 겸, 파이썬 라이브러리를 정확하게 사용하는 방법도 익힐 겸 코드로 작성하며 확인했다. 오늘의 끝은 몬드리안.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Piet_Mondrian_1942_Broadway_Boogie_Woogie.jpg"></p>
<p align="center">Piet Mondrian, &ltBroadway Boogie Woogie&gt, 1942-43. Oil on canvas, 127x127cm.</p>
  
  - Day 1 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day2/Note.md "Day2 Note")
