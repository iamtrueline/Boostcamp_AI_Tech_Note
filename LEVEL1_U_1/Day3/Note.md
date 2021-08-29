# 📙 Note

### 파이썬 객체 지향 프로그래밍 :: [기초 복습] Python Basics for AI 4-1강 ~ 4-2강

- 객체 지향

  - 절차 지향이 프로그램이 진행되는 순서에 집중한다면 객체 지향은 프로그램의 주체, 행동과 속성에 주목.
  - 객체 : 실생활에서 일종의 물건. 속성(Attribute)과 행동(Action)을 가짐. 프로그램에서 이는 변수(Variable)와 함수(Method)로 표현.
  - 파이썬은 객체 지향 프로그램 언어.
  - 객체 지향 프로그래밍은 크게 클래스(Class)와 인스턴스(Instance) 구현으로 나뉜다.

- 파이썬 작성

  - 기본 작성 틀은 여타 객체 지향 언어 매뉴얼과 다르지 않다.
  - 객체 초기화 예약 함수 '__init__', 'self' 로 클래스 속성 추가.
  - 메소드는 반드시 'self'를 추가해야만 클래스 함수로 인정. self = 본 인스턴스, super = 부모 클래스

- 객체 지향 언어 특징

  - 상속(Inheritance) : 부모클래스로부터 속성과 메소트를 물려받은 자식 클래스를 생성하는 것.
  - 다형성(Polymorphism) : 같은 이름의 메소드의 내부 로직을 다르게 작성. 다이나믹 타이핑 특성을 가진 파이썬에서는 오버로딩은 정식으론 지원하지 않는다. 그러므로 파이썬 내 다형성은 오버라이딩(상속한 메소드를 변경하는 것)으로 본다.
  - 가시성(Visibility) : 객체의 정보를 볼 수 있는 레벨을 조절하는 것. 모든 사람이 모든 변수를 볼 필요는 없다. 캡슐화 또는 정보 은닉. 파이썬에서는 Private 변수, property decorator 등으로 조절. 보호가 필요한 정보는 카피 후 반환이 기본.

- First-class objects

  - 일등함수 또는 일급 객체
  - 변수나 데이터 구조에 할당이 가능한 객체
  - 파라미터로 전달, 리턴 값으로 사용이 가능.
  - 파이썬의 함수는 일급함수
 
- 모듈과 패키지

  - 모듈 : 어떤 대상의 부분 혹은 조각. 모듈을 모아 하나의 큰 프로그램을 개발. 파이썬에선 .py 파일.
  - 패키지 : 모듈을 모아놓은 단위, 하나의 프로그램. 하나의 대형 프로젝트를 만드는 코드의 묶음.
  - 모듈을 호출할 땐 필요한 내용만 골라서 호출 가능. (namespace and import)

- 파이썬 빌트인 모듈

  - 문자처리, 웹, 수학 등 다양한 모듈이 빌트인으로 제공된다. (ex. random, time 등)
  - import문으로 활용 가능.

- 패키지 작성

  - 다양한 모듈들의 합으로 완성되는 패키지.
  - 기능을 세부적으로 나누어 폴더를 만들고 -> 각 폴더별로 필요한 모듈 구현 -> 테스트 -> 폴더별 __init__.py 구성 -> __main__.py 파일 생성 -> 실행

- 가상환경(Virtual Environment)

  - 프로젝트 진행 시 필요한 패키지만 설치하는 환경.
  - 다양한 패키지 관리 도구를 사용. 대표적으로 virtualenv와 conda가 있다.

### 통계학 맛보기 :: [기초 복습] AI Math 7강

- 모수

  - 통계적 모델링은 적절한 가정 위에서 확률분포를 추정(inference)하는 것이 목표이며, 기계학습과 통계학이 공통적으로 추구하는 목표.
  - 유한한 개수의 데이터만 관찰해서 모집단의 분포를 정확하게 알아내는 것은 불가능. 따라서 근사적으로 확률분포를 추정해야 한다.
  - 모수적 방법론(parametric) : 데이터가 특정 확률분포를 따른다고 선험적으로(a priori) 가정한 후 그 분포를 결정하는 모수(parameter)를 추정하는 방법.
  - 비모수적 방법론(nonparametric) : 특정 확률분포를 가정하지 않고 데이터에 따라 모델의 구조 및 모수의 개수가 유연하게 바뀌는 방법론. 모수가 없는 것이 아니라 무수히 많거나 데이터에 따라 모수 개수가 바뀌는 것.

- 확률분포 가정

  - 확률분포는 히스토그램을 통한 모양 관찰로 가정한다.
  - 베르누이분포 : 데이터가 2개의 값(0 또는 1)만 가지는 경우
  - 카테고리분포 : 데이터가 n개의 이산적인 값을 가지는 경우
  - 베타분포 : 테이터가 0과 1 사이에서 값을 가지는 경우
  - 감마분포, 로그정규분포 등 : 데이터가 0 이상의 값을 가지는 경우
  - 정규분포, 라플라스분포 등 : 데이터가 실수 전체에서 값을 가지는 경우
  - 기계적으로 확률분포를 가정하는 것은 아니며, 데이터 생성 원리를 먼저 고려하는 것이 원칙.
  - 정규분포의 모수는 평균과 분산으로, 이를 추정하는 통계량(statistic)은 다음과 같다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img00.PNG" alt="정규분포 평균과 분산"></p>

-
  - 분산을 구할 때 N이 아니라 N-1로 나누는 이유는 불편(unbiased) 추정량을 구하기 위함. 평균의 경우 샘플이 치우쳐져 있더라도 여러 번의 샘플링을 거치면 다른쪽으로 치우쳐진 샘플도 나올 것이기 때문에 결론적으론 실제 평균과 비슷해질 것. 그러나 분산은 우연히 한쪽으로 치우쳐진 샘플링들만 뽑게 되면 분산이 과소평가된 상태로 유지된다. (각 샘플들이 다 다른 방향으로 있어도 분산은 결국 적게 나올 것.) 그렇다면 인위적으로 분모를 줄여서 분산을 크게 유도하는 수 밖에 없다.
  - 왜 하필 N-1로 나눌까? 크게 보고 싶으면 N-2나 N-3은 안되는가? 평균을 아는 상태에서 샘플 값 3개를 뽑는다고 가정할 때 이미 2개가 뽑혀 있다면 나머지 하나는 자동으로 정해진다. 이미 알고 있는 평균에 맞춰야 하니까(시간적 순서가 바뀌었지만, 가정하는 것). 즉 자유롭게 정할 수 있는 변수 수는 3개가 아니라 3-1 = 2개. ~ N개가 아니라 N-1. 샘플 분산에서 자유도는 N-1이기 때문에 하필 N-1로 나누는 것.
  - 표집분포(sampling distribution) : 통계량의 확률분포
  - 중심극한정리 표본평균의 표집분포는 N이 커질수록 정규분포를 따른다. 표집분포 != 모집단분포
  - 아래는 데이터 증가에 따른 베르누이분포의 표집분포
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img01.PNG" alt="데이터 증가에 따른 베르누이분포의 표집분포"></p>

- 최대가능도 추정법

  - 표본평균이나 표본분산은 중요한 통계량이나, 확률분포마다 사용하는 모수가 다르므로 적절한 통계량도 함께 달라짐.
  - 최대가능도 추정법(MLE, Maximum Likelihood Estimation) : 이론적으로 가장 가능성이 높은 모수를 추정하는 방법
  - 가능도 함수는 모수 세타를 따르는 분포가 x를 관찰할 가능성을 의미하며 대소비교만 가능하고 확률로 해석할 수 없다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img02.PNG" alt="가능도 함수"></p>

-
  - 데이터 집합 X가 독립적으로 추출되었을 경우 로그가능도를 최적화.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img03.PNG" alt="로그가능도 최적화"></p>

-
  - 데이터의 숫자가 수억 단위가 될 때 컴퓨터의 정확도로 가능도를 계산하는 것은 불가능. 데이터가 독립일 경우, 로그를 사용하면 가능도의 곱셈을 로그가능도의 덧셈으로 바꿀 수 있기 때문에 연산 가능. 
  - 경사하강법으로 가능도를 최적화할 때 미분 연산을 사용하는데, 로그가능도를 사용하면 연산량이 O(n^2)에서 O(n)으로 축소.
  - 대부분의 손실함수가 경사하강법을 이용, 음의 로그가능도(negative-log-likelihood)를 최적화.
  - 최대가능도 추정법은 불편수정량을 보장하진 않는다. (N-1로 나누지 않으니까)

- 정규분포에서의 최대가능도 추정법

  - 정규분포를 따르는 확률변수 X로부터 독립적인 표본 {x1, ..., xn}을 얻었을 때 최대가능도 추정법을 이용하여 모수 추정.
  - 정규분포의 모수는 평균과 분산.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img04.PNG" alt="정규분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img05.PNG" alt="정규분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img06.PNG" alt="정규분포에서의 최대가능도 추정법"></p>

- 카테고리분포에서의 최대가능도 추정법

  - 카테고리분포를 따르는 확률변수 X로부터 독립적인 표본 {x1, ..., xn}을 얻었을 때 최대가능도 추정법을 이용하여 모수 추정.
  - 카테고리분포의 모수는 확률. 모두 더하면 1.
  - 카테고리분포에서 MLE는 경우의 수를 세어 비율을 구하는 것.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img07.PNG" alt="카테고리분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img08.PNG" alt="카테고리분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img09.PNG" alt="카테고리분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img10.PNG" alt="카테고리분포에서의 최대가능도 추정법"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img11.PNG" alt="카테고리분포에서의 최대가능도 추정법"></p>

- 딥러닝에서의 최대가능도 추정법

  - 딥러닝 모델의 가중치를 세타 = (W'1, ..., W'L) 라 표기했을 때 분류 문제에서 소프트맥스 벡터는 카테고리분포의 모수 (p1, ..., pk)를 모델링한다.
  - 원핫벡터로 표현한 정답레이블 y = (y1, ..., yk) 을 관찰데이터로 이용해 확률분포인 소프트맥스 벡터의 로그가능도를 최적화할 수 있다.
  - 원핫벡터 속 원소는 하나만 1, 나머지는 0.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img12.PNG" alt="딥러닝에서의 최대가능도 추정법"></p>

- 확률분포의 거리

  - 기계학습에서 사용되는 손실함수들은 모델이 학습하는 확률분포와 데이터에서 관찰되는 확률분포의 거리를 통해유도.
  - 두 확률분포(P(x), Q(x))사이의 거리 계산 함수 : 총변동 거리 (TV, Total Variation distance), 쿨백-라이블러 발산(KL, Kullback-Leibler Divergence), 바슈타인 거리(Wasserstein Distance)
  - 쿨백-라이블러 발산은 다음과 같이 정의하고 분해한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img13.PNG" alt="쿨백-라이블러 발산 정의"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img14.PNG" alt="정쿨백-라이블러 발산 분해"></p>

-
  - 분류 문제에서 정답레이블을 P, 모델 예측을 Q라 두면 최대가능도 추정법은 쿨백-라이블러 발산을 최소화하는 것과 같다.

# ✏️ Doodle

- 코드 작성보다 강의 수강과 정리가 훨씬 길었던 날. 강의엔 기초(라고 써있지만...)개념들이 오목조목 잘 들어가 있지만 너무 짧은 감이 없지 않다. 가이드라인 제시로는 훌륭. 다른 것들도 항상 그랬으니 잘 따라가자. 연산 자체보다 용어가 생소해서 진도가 더뎠다. 식을 보면 뭘 말하고 싶은지 감 잡을 수 있도록 찾아볼 것. 쿨백-라이블러 발산은 정리가 부족하다. 다른 개념들보다 강의 자료 가중치가 미묘하게 높았으니 그냥 넘어가는 것보다 더 알아보고 다음 장을 펴는 게 나을 것 같다. 나 말고 다른 사람에게 물어볼 수 있다는 건 정말 신나는 일이야. 일단 마감이 우선인 과제부터 작성 후 강의 수강 예정. 오늘의 끝은 드가.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Edgar_Degas_1874_The_Dance_Class.jpg"></p>
<p align="center">Edgar Degas, &ltThe Dance Class&gt, 1874. Oil paint on canvas, 83.5x77.2cm.</p>

- Day 3 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day2/Note.md "Day2 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day4/Note.md "Day4 Note")
