# 📙 Note

### 파이썬으로 데이터 다루기 :: [기초 복습] Python Basics for AI 5-1강 ~ 5-2강

- 예외 처리

  - 예외(Exception)는 예상 가능한 예외, 예상이 불가능한 예외로 나뉨.
  - 예상 가능한 예외 : 발생 여부를 사전에 인지할 수 있는 예외. 사용자의 잘못된 입력, 파일 호출 시 파일 없음 등. 개발자가 반드시 명시적으로 정의해야 한다.
  - 예상 불가능한 예외 : 인터프리터 과정에서 발생하는 예외. 리스트의 범위를 넘어가는 값 호출, 정수를 0으로 나눔 등. 수행 불가 시 인터프리터가 자동으로 호출.
  - 예외 발생의 후속 조치를 위해 Exception Handling은 필수. 

- 파이썬의 예외 처리

  - 조건문.
  - try ~ except 코드.
  - 빌트인 에러코드명 지원(ex. ZeroDivisionError, IndexError 등).
  - try ~ except ~ else 구조도 가능. except가 없다면 else 실행.
  - try ~ except ~ else ~finally : finally는 무조건 실행.
  - raise : 강제로 Exception 발생.
  - assert : 특정 조건에 맞지 않은 경우 강제로 Exception 발생. 보통 값 확인 True/False로 판단.

- 파일 핸들링

  - 기본적인 파일 종류는 Text파일과 Binary파일. 각각 인간도 이해할 수 있는 형태인 문자열, 특정 프로그램에서만 실행 가능한 컴퓨터의 언어, 이진법 형식으로 저장된 파일. (Text 파일도 실제는 Binary, but ASCII/Unicode로 저장되어 사람이 읽을 수 있음)

- 파이썬의 파일 처리

  - open(), read(), close()
  - with 구문으로 사용하면 별도의 close() 없이 들여쓰기로 마침 가능. 편한 걸로 선택.
  - 모드 : r, w, a. file write 시에는 encoding 형식 추가.
  - 디렉토리 핸들링은 os 모듈을 사용한다.
  - pathlib : path를 객체로 다루는 모듈. 패스 형식자가 달라 발생하는 에러를 방지할 수 있음.
  - Pickle : 파이썬의 객체를 영속화(persistence)하는 빌트인 객체(import 필요). 테이터, 오브젝트를 실행 중 저장해서 이후 불러와 사용한다.

- 로그 핸들링

  - 로그 남기기(Logging) : 프로그램들이 실행되는 동안 일어나는 정보 기록. 기록된 로그를 분석하여 의미 있는 결과 도출. 실행시점에 남겨야 하는 기록, 개발시점에 남겨야 하는 기록으로 나뉜다.
  - logging : 파이썬의 기본 로그 관리 모듈.
  - 로그 레벨 : debug > info > warning > error > critical
  - debug : 개발 시 처리 기록을 남겨야 하는 로그 정보
  - info : 처리가 진행되는 동안의 정보
  - warning : 사용자가 잘못 입력한 정보로 처리는 가능하나 원래 개발 시 의도치는 않은 상황 정보
  - error : 잘못된 처리로 인해 에러가 났으나 프로그램은 동작할 수 있을 때 상황 정보
  - critical : 잘못된 처리로 데이터 손실이나 더 이상 프로그램이 동작할 수 없을 때 상황 정보
  - 기본은 warning부터 출력. 출력 레벨은 변경할 수 있다.

- 프로그램 실행 설정

  - configparser : 파일에 미리 설정. Key - Value 형태로 설정.
  - argparser : 실행시점에 설정. 콘솔 창에서 실행 시 세팅 정보를 저장.

- CSV(Comma Separate Value)

  - 필드를 쉼표(,)포 구분한 텍스트 파일
  - 엑셀 양식의 데이터를 프로그램에 상관없이 쓰기 위한 데이터 형식.
  - 쉼표 뿐 아니라 탭(TSV), 빈칸(SSV) 등으로 구분하기도 함. 통칭 CSV.
  - 보통 한 줄씩 처리.
  - 문장 내 쉼표 전처리, 한글 인코딩 처리 필요.
  - 파이썬에서 csv 객체 제공.

- Web(WWW, World Wide Web)

  - 데이터 송수신을 위한 HTTP 프로토콜 사용

- HTML(Hyper Text Markup Language)

  - 웹 상의 정보를 구조적으로 표현하기 위한 언어. HTML 소스파일을 컴퓨터가 다운로드 후 웹 브라우저가 해석 및 표시.
  - HTML도 일종의 프로그램으로 페이지 생성 규칙이 있다. 규칙을 분석하여 데이터의 추출이 가능하고 해당 데이터로 다양한 분석이 가능하다. 정규식 활용.
  - 파이썬에서 정규식 활용 : re 모듈로 활용 가능.

- XML(eXtensible Markup Language)

  - 데이터의 구조와 의미를 설명하는 태그를 사용하여 표시하는 언어.
  - HTML과 비슷한 문법.
  - 스키마와 DTD 등으로 메타정보를 표현, 용도에 따라 다양한 활용 가능.
  - 컴퓨터 간(ex.PC<->스마트폰) 정보를 주고받기 유용한 저장 방식.
  - 정규표현식으로 파싱 가능하지만 beautifulSoup을 많이 사용함.

- JSON(JavaScript Object Notation)

  - 원래 웹 언어인 자바스크립트의 데이터 객체 표현 방식.
  - 간결성으로 기계/인간이 모두 이해하기 편함.
  - 데이터 용량이 적고, Code로의 전환이 쉬움.
  - XML의 대체재로 많이 활용.
  - 파이썬에서 json 모듈을 사용하여 손쉽게 파싱 및 저장 가능.

### 베이즈 통계학 맛보기 :: [기초 복습] AI Math 8강

- 쿨백-라이블러(KL-Divergence) 발산
  - Q는 사전확률 분포, P는 사후확률 분포. P
  - P는 주로 참 분포, 실제 관찰 데이터. Q는 주로 가설, 모델, 그리고 P의 근사.
  - 쿨백-라이블러 발산은 항상 0 이상의 값을 갖는다. 두 확률 분포가 동일하면 값이 0.
  - 비대칭함수.

- 베이즈 정리
  - 조건부확률 P(A|B) : 사건 B가 일어난 상황에서 사건 A가 발생할 확률.
  - 베이즈 정리는 조건부 확률을 이용하여 정보를 갱신하는 방법을 알려준다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img00.PNG" alt="베이즈 정리"></p>

-
  - 위 식과 똑같은 표현으로 세타를 모델, D를 실제 데이터라고 가정할 때 아래 식과 같다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img01.PNG" alt="베이즈 정리 예제"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img02.PNG" alt="조건부확률의 시각화"></p>

-
  - 베이즈 정리를 통해 새로운 데이터가 들어왔을 때 앞서 계산한 사후확률을 사전확률로 사용하여 갱신된 사후확률을 계산할 수 있다. 베이즈 정리의 유용점중 하나.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img03.PNG" alt="베이즈 정리를 통한 정보의 갱신"></p>

- 조건부 확률과 인과관계

  - 조건부 확률만 가지고 인과관계를 추론하는 것은 불가능하다.
  - 아래는 조건부확률 기반 예측모형과 인과관계 기반 예측모형의 예측정확도 예시.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img04.PNG" alt="조건부확률, 인과관계 예측모형 비교"></p>

-
  - 인과관계는 데이터 분포의 변화에 강건하지만 높은 예측정확보 보증은 어려움.
  - 인과관계를 알아내기 위해서는 중첩요인(confounding factor)효과를 제거하고 원인에 해당하는 변수만의 인과관계를 계산해야 함. 안정적이고 믿을만한 결과를 위한 필수 과정. 이 과정을 생략하면 가짜 연관성(spurious correlation)이 도출.

### CNN 첫걸음 :: [기초 복습] AI Math 9강

- Convolution 연산 in CNN(Convolutional Neural Network)

  - 다층신경망에서는 각 뉴련들이 선형모델과 활성함수로 모두 연결된 구조. i마다 가중치가 있으므로 i가 바뀌면 가중치도 바뀐다. 
  - Convolution 연산은 고정된 가중치인 커널(kernel)을 입력벡터 상에서 커널 사이즈만큼 움직이면서 선형모델과 합성함수가 적용되는 구조. 가중치가 입력마다 있는 게 아니므로 파라미터 사이즈를 줄이는 데 효과적.
  - 수학적인 의미는 신호(signal)를 커널을 이용해 국소적으로 증폭 또는 감소시켜서 정보를 추출 또는 필터링 하는 것.
  - 엄밀히 말하면 CNN에서 사용하는 연산은 +를 사용하기 때문에 convolution이 아니라 cross-correlation이다.
  - 1차원 뿐 아니라 다양한 차원에서 계산 가능. 데이터의 성격에 따라 사용하는 커널이 달라진다. 텍스트는 1차원, 흑백 영상 2차원, 칼라 영상 3차원 등. 모두 위치에 따라 정해진 커널 값 자체는 바뀌지 않는다.

- 2차원 Convolution 연산

  - 마찬가지로 커널이 입력벡터 상에서 움직여가면서 선형모델과 합성함수 적용. 유리창을 닦듯이.
  - 입력 크기 (H, W), 커널 크기 (Kh, Kw), 출력 크기 (Oh, Ow)라 하면 출력크기는 다음과 같다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img05.PNG" alt="2차원 convolution 연산 출력 크기"></p>

-
  - 채널이 여러 개인 2차원 입력은 2차원 Convolution을 채널 개수만큼 적용. 이 때, 커널의 채널도 입력 채널수만큼 있어야 한다.
  - 커널이 한 개라면 출력의 채널 자체도 한 개. 출력의 채널 자체를 여러 개 만들려면 커널 개수를 늘리면 된다.
  - 3차원부터 행렬이 아닌 텐서로 부른다. 

- Convolution 연산의 역전파

  - 커널이 모든 입력 데이터에 공통으로 적용되기 때문에 역전파를 계산할 때도 Convolution 연산이 나온다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img06.PNG" alt="Convolution 연산의 역전파"></p>

### RNN 첫걸음 :: [기초 복습] AI Math 10강

- 시퀀스 데이터(Sequence Data)

  - 소리, 문자열, 주가 등의 데이터를 시퀀스 데이터로 분류.
  - 이벤트의 발생 순서가 중요. 독립동등분포 가정을 잘 위배하기 때문에 순서를 바꾸거나 과거 정보에 손실이 발생하면 데이터의 확률분포도 바뀐다. 맥락 없이 학습하기 어렵다.
  - 조건부확률로 앞으로 발생할 데이터의 확률분포를 다룰 수 있다. (베이즈 정리 사용)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img07.PNG" alt="Convolution 조건부확률로 시퀀스 데이터를 이용한 사후 발생 데이터 확률 분포 추정"></p>

-
  - 단, 시퀀스 데이터를 분석할 때 항상 모든 과거 정보들이 필요한 것은 아니다. 상황에 따라 탈락이 필요.
  - 따라서 시퀀스 데이터를 다루기 위해선 길이가 가변적인 데이터를 다룰 수 있는 모델이 필요.
  - 고정된 길이만큼의 시퀀스만 사용하는 경우, 자기회귀모델(AR, AutoregRessive model). 이 때 변수를 사전에 설정해야 함.
  - 직전 정보를 하나의 변수로, 직전 정보를 제외한 나머지 정보를 하나의 잠재변수로 설정하여 인코딩하는 것이 RNN.

- RNN(Recurrent Neural Network)

  - 가장 기본적인 RNN 모형은 MLP와 유사. W(1)과 W(2)는 입력과 상관 없이 불변.
  - 기존 MLP 모형은 하나의 시점(현재) 정보만 다룰 수 있다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img08.PNG" alt="MLP 모형"></p>

-
  - RNN은 이전 순서의 잠재변수와 현재의 입력을 활용하여 모델링. 마찬가지로 가중치행렬은 입력에 상관 없이 불변.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img09.PNG" alt="RNN 모형"></p>

-
  - BPTT(Backpropagation Through Time) : RNN의 역전파는 잠재변수의 연결그래프에 따라 순차적으로 계산한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img10.PNG" alt="RNN 순전파 역전파 모형"></p>

- BPTT

  - BPTT를 통해 RNN의 가중치 행렬의 미분을 하면 미분의 곱으로 이루어진 항이 계산됨. 시퀀스의 길이가 길어질수록 역전파 알고리즘의 계산이 불안정해지므로(무한대로 커지거나 무한대로 작아짐) Vanilla RNN은 길이가 긴 시퀀스 처리가 어렵다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img11.PNG" alt="RNN 가중치 행렬 미분 with BPTT"></p>

  - Truncated BPTT : 긴 시퀀스를 처리하기 위한 방법 중 하나. 장기 정보를 적절한 단위로 쪼개서 학습시키는 것이 아이디어. 전체 타임 스텝을 일정 구간으로 나눠 역전파.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day04_img12.PNG" alt="Truncated BPTT"></p>

# ✏️ Doodle

- 4일째. 입학 후 1주일째가 된 느낌이다. 딱 이 정도로 뿌듯했고, 이 정도로 이해 못했다. 급하게나마 기본 수학 모형을 훑었으니 부족하고 기억에 남지 않은 부분을 중심으로 추가 자료를 정리하려한다. 마스터 클래스에서 제시된 서치 가이드가 많은 도움이 된다. 코드 작성이 조금 늦어졌다. 숨은 나중에 두 번 몰아쉬자. 오늘의 끝은 뭉크.

<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Edvard_Munch_1894_Madonna.jpg"></p>
<p align="center">Edvard Munch, &ltMadonna&gt, 1894. Oil on canvas, 90x68cm.</p>

- Day 4 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day3/Note.md "Day3 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day5/Note.md "Day5 Note")
