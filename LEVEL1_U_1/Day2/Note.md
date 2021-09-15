# :orange_book: Note

### 파이썬 기초 문법 II :: [기초 복습] Python Basics for AI 3-1강 ~ 3-2강

- 파이썬 기본 자료 구조

  - 스택(Stack) : LIFO(Last In First Out). 입력은 Push, 출력은 Pop. 리스트를 사용하여 스택 구조를 활용 가능. Push = append(), Pop = pop().
  - 큐(Queue) : FIFO(First In First Out). 역시 리스트를 사용하요 큐 구조를 활용 가능. Push = append(), Pop = pop(0).
  - 튜플(Tuple) : 값의 변경이 불가능한 리스트. 리스트의 모든 기능을 쓸 수 있지만, 변환만 불가. 타 변수 할당용으론 활용 가능하다. 선언 시 일반 괄호 (). 값이 하나라면 반점 필수.
  - 집합(Set) : 값은 순서 없이 저장하며 중복을 불허하는 자료 구조. 합집합(union), 교집합(intersection), 차집합(difference) 연산을 지원한다.
  - 사전(Dictionary) : 고유 키(Key)와 값(Value)을 가지는 자료 구조. 키는 중복 불허. 키-값 쌍은 dict.items()로 호출. 기본값을 지정하려면 defaultdict 사용.

- 확장 자료 구조 (Collections)

  - List, Tuple, Dictdp 대한 확장 자료 구조. 사용자에게 편의성과 실행 효율을 제공. 필요할 때 import하여 활용한다.
  - Deque : Stack과 Queue를 지원하는 모듈로 List에 비해 빠른 자료 저장 방식을 지원한다. rotate, reverse 등 Linked List 특성을 지원, 기존 List의 함수를 모두 지원.
  - OrderedDict : 기본 Dict와 달리 입력한 순서대로 dict를 반환하는데, 최신 버전은 굳이 필요 없음. 기본 Dict도 순서가 보장된다.
  - Counter : 시퀀스형 구조 내 자료의 개수를 dict 형태로 반환. Set 연산을 지원한다.
  - Namedtuple : Tuple 형태로 자료 구조체를 저장.

- Pythonic code

  - split & join : 기본은 빈칸을 기준으로 문자열을 나누고 잇기.
  - list comprehension : 기존 리스트를 이용해서 다른 리스트 만들기. 일반적으로 for + append보다 속도가 빠름.
  - enumerate : 리스트에서 값을 추출할 때 번호를 붙여서 추출.
  - zip : 두 개의 리스트 값을 병렬로 추출.
  - lambda : 익명 함수. 다사용 비권장 - 테스트와 코드 해석이 어려움.
  - map : 시퀀셜 데이터를 특정 함수에 매핑. 두 개 이상의 리스트에도 적용 가능. 실행 시점에서 값을 생성.
  - reduce : 리스트에 똑같은 함수를 적용하여 통합. 사용 지양 분위기로 import 필요.
  - iterable objects : 시퀀셜 데이터 주소값(초기는 시작점)을 받아 다음 주소를 가진 채 활용. iter, next 함수 기본 지정.
  - generator : iterable object를 특수한 형태로 사용해주는 함수. 값이 사용되는 시점에 메모리 반환하므로 메모리 절약, 대용량 데이터 연산에 유리. 큰 데이터나 파일 데이터를 처리할 땐 반드시 고려하자. yield 함수 기본 지정.
  - 가변인자 (variable-length asterisk) : 개수가 정해지지 않은 변수를 함수의 인자를 쓰자. 입력된 값은 tuple로 활용. 변수명 앞에 포인터(C 포인터 아니고 asterisk) 기호로 표시. tuple이나 dict를 이걸로 싸매서 날리면 자동으로 unpacking. 포인터 두 개면 키워드 가변 인자로, 함수 호출 시에 따로 키워드를 지정한다. 여러 개를 같이 쓸 거면 순서는 꼭 지키기.
  - Keyword arguments : 함수에 넣는 인수에 이름을 지정하면 꼭 순서대로 들어가지 않아도 된다.
  - default arguments : 함수에 넣는 인수가 모자라면 기본 지정된 값으로 연산한다. 당연히 없으면 에러.
  - 왜 쓰는데? : 짧은 코드, 빠른 이해, 높은 효율.

---

### 경사하강법 (순한맛) :: [기초 복습] AI Math 3강

- 미분(differentiation)

  - 변수의 움직임에 따른 함숫값의 변화를 측정하기 위한 도구. 최적화에서 제일 많이 사용하는 기법.
  - 미분 = 변화율의 극한(limit)으로 정의.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img00.PNG" alt="미분"></p>

-
  - In Python, sympy.diff()로 계산
  - 함수 f의 주어진 점(x, f(x))에서의 접선의 기울기를 구한다.
  - 한 점에서 미분값을 더하면 함숫값 증가, 미분값을 빼면 함숫값 감소.
  - 경사상승법(gradient ascent) : 미분값을 더해 함수의 극댓값을 찾는 방법.
  - 경사하강법(gradient descent) : 미분값을 빼 함수의 극솟값을 찾는 방법.
  - 경사상승법, 경사하강법 모두 극값에 도달하면 움직임을 멈춘다.
  - 컴퓨터로 미분 계산 시 정확한 0 도출은 불가하므로 종료값을 적절히 설정해야 한다.
  - 변동 미분값에 곱하는 학습률에 따라 알고리즘의 수렴 속도와 정확도가 결정된다.

- 편미분(partial differentiation)

  - 벡터가 입력인 다변수함수의 경우 이용. 특정 값 하나에 대해서만 미분. 이때 다른 값은 상수 취급한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img01.PNG" alt="편미분"></p>

-
  - 마찬가지로 In Python, sympy.diff()로 계산
  - 각 변수 별로 편미분을 계산한 그레디언트 벡터(gradient vector)를 경사하강법, 경사상승법에 사용할 수 있다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img02.PNG" alt="그레디언트 벡터 예시"></p>

-
  - 그레디언트 벡터는 한 점에서 극댓값(극솟값)에 가장 빨리 가까워지는 방향으로 구성된다.

---

### 경사하강법 (매운맛) :: [기초 복습] AI Math 4강

- 경사하강법

  - 선형모델이 아닌 다른 모델에도 적용 가능한 최적화 방법.
  - 선형회귀 계수 구하기 : 선형회귀의 목적식을 최소화하는 베타값을 찾아야 하므로 목적식을 베타로 미분. 1/n으로 나눈 후 제곱함에 유의(평균값)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img03.PNG" alt="선형회귀 계수 구하기"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img04.PNG" alt="선형회귀 계수 구하기"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img05.PNG" alt="선형회귀 계수 구하기"></p>

-
  - 이에, 목적식을 최소화하는 베타값을 구하는 경사하강법 알고리즘은 다음과 같다. 경사'하강'법이므로 베타(t+1) = 베타(t)에서 미분값을 빼는 것. 람다는 학습률.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img06.PNG" alt="베타값 구하기"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img07.PNG" alt="베타값 구하기"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img08.PNG" alt="베타값 구하기"></p>

-
  - L2노름을 최소화하는 벡터나 L2노름의 제곱을 최소화하는 최적화 방향은 같다. 결괏값이 같음. 따라서 원리적으로 L2노름을 목적식으로 사용해도 되지만 L2노름의 제곱을 사용해도 된다.
  - 종료값은 특정 값이어도 되고 학습 횟수여도 된다. 다만 학습 횟수일 경우 적절히 커야 유의미.
  - 경사하강법 사용의 키 = 적절한 학습률과 학습 횟수.
  - 이론적으로 경사하강법은 미분가능하고 볼록(convex)한 함수에 대해선 적절한 학습률과 학습횟수를 선택했을 때 수렴이 보장.
  - 비선형회귀 문제에선 목적식이 볼록하지 않을 수 있으므로 수렴이 보장되지 않음. 딥러닝을 사용하는 경우 대부분 비선형회귀.

- 확률적 경사하강법(SGD, Stochastic gradient descent)

  - 업데이트에 모든 데이터를 사용하는 대신 데이터 한 개 또는 일부(미니배치, MiniBatch)를 활용.
  - 볼록이 아닌 목적식을 최적화 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img09.PNG" alt="SGD 최적화"></p>

-
  - 딥러닝의 경우 경사하강법보다 실증적으로 더 낫다.
  - 모든 데이터를 활용하는 결과와 같은 수는 없지만 매우 유사.
  - 전체 데이터 연산의 시간복잡도가 O(d^2 n)일 때, b개의 미니배치를 사용할 경우 O(d+2 b)로 감소.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img08.PNG" alt="미니배치 활용"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img10.PNG" alt="미니배치 활용"></p>

-
  - 미니배치를 사용할 경우 원래 목적식 그레디언트 모양과 다르고 각 모양이 고정되어있지 않다. 때문에 특정 목적식에서 극솟값으로 판단되더라도 다른 목적식에서는 그렇지 않을 수 있다. 볼록하지 않은 목적식의 경우 이런 극솟값 탈출이 필수.
  - 정확하지 않은 방향이지만 결론적으로는 빠르게 최솟값을 향하는 방향.
  - 미니배치 사이즈에 따라 수렴 속도가 달라지며, 미니배치 사이즈가 너무 작을 시 기존 경사하강법보다 수렴 속도가 더 느릴 수도 있다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img11.PNG" alt="경사하강법과 미니배치 비교표"></p>

-
  - 덩치 큰 데이터를 상대하려면 미니 배치로 쪼개는 게 하드웨어적으로 유리. 다만 너무 작게 쪼개면 상대하다가 타임 아웃.
  
---  
  
### 딥러닝 학습방법 이해하기 :: [기초 복습] AI Math 5강

- 신경망(neural network)

  - 비선형모델.
  - 선형모델과 활성함수(activation function)를 합성한 함수. 활성함수를 쓰지 않으면 딥러닝은 선형모형과 차이가 없다.
  - 잠재벡터 z의 각 노드에 개별적으로 활성함수를 적용하여 새로운 잠재벡터 H를 도출.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img12.PNG" alt="잠재벡터 H 도출"></p>

-
  - 잠재벡터 H를 다시 한 번 선형변환하면 잠재벡터 O 도출 = 2층 신경망.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img13.PNG" alt="잠재벡터 O 도출"></p>

-
  - 이를 반복하면 다층 신경망 = 다층 퍼셉트론 = MLP(Multi-Layer Perceptron)
  - 이론적으로는 2층 신경망으로도 임의 연속함수 근사 가능. (universal approximation theorem)
  - 그러나 층이 깊을수록 목적함수를 근사하는데 필요한 뉴런(노드)의 숫자가 훨씬 빨리 줄어들어 효율적인 학습 가능.
  - 층이 깊을수록 최적화는 어려워진다.

- 활성함수

  - 비선형 함수.
  - 시그모이드(sigmoid)함수나 tanh 함수는 전통적으로 많이 쓰이던 활성함수이나 딥러닝에선 ReLU 함수를 많이 쓴다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img14.PNG" alt="활성함수"></p>

- 소프트맥스 연산

  - 모델의 출력을 확률로 해석할 수 있게 변환해주는 연산.
  - 분류 문제를 풀 때 선형모델과 소프트맥스 함수를 결합하여 예측
  - 단, 학습이 아니라 추론을 할 땐 원핫(one-hot) 벡터로 최댓값을 가진 주소만 1로 출력하는 연산 사용. not 소프트맥스.
  - 지수함수를 사용하므로 Python 내 활용 시 overflow 처리 필요.

- 역전파 알고리즘 (<-> 순전파 알고리즘)

  - 딥러닝이 각 층에 사용된 파라미터를 학습하는 방법.
  - 역전파 알고리즘은 합성함수 미분법인 연쇄법칙(chain-rule) 기반 자동미분(auto-differentiation)을 사용.
  - 컴퓨터가 각 노드의 텐서 값을 기억해야한다. (순전파에선 필요 없다.)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img15.PNG" alt="연쇄법칙"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img16.PNG" alt="연쇄법칙"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img17.PNG" alt="연쇄법칙"></p>

---

### 확률론 맛보기 :: [기초 복습] AI Math 6강

- 확률론

  - 딥러닝은 확률론 기반의 기계학습 이론에 바탕을 둠.
  - 기계학습에서 사용되는 손실함수(lossfunction)들의 작동원리는 데이터 공간을 통계적으로 해석해서 유도.
  - 회귀분석에서 손실함수로 사용되는 L2노름은 예측오차의 분산을 가장 최소화하는 방향으로 학습.
  - 분류문제에서 사용되는 교차엔트로피(cross-entropy)는 모델예측의 불확실성을 최소화하는 방향으로 학습.
  - 분산 및 불확실성을 최소화하기 위해 필요한 측정법.

- 이산확률변수 and 연속확률변수

  - 확률변수가 가질 수 있는 모든 경우의 수를 고려하여 확률을 더해 모델링.
  - 데이터 공간에 정의된 확률변수의 밀도(density) 위에서의 적분을 통해 모델링.
  - 두 분포 모두 가진 경우도 있음.

- 확률분포

  - 결합분포는 데이터를 모델링.
  - 주변확률분포는 입력 x에 대한 정보만. y에 대한 정보는 없다.
  - 조건부확률분포는 데이터 공간에서 입력 x와 출력 y 사이의 관계를 모델링. P(y|x) 는 입력변수 x에 대해 정답이 y일 확률. 이때, 연속확률분포라면 확률이 아니라 밀도로 해석.

- 기댓값(expectation)

  - 확률분포가 주어지면 데이터를 분석하는데 사용 가능한 여러 종류의 통계적 범함수(statistical functional)를 계산 가능.
  - 기댓값은 데이터를 대표하는 통계량. 확률분포를 통해 다른 통계적 범함수를 계산하는데 사용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img18.PNG" alt="통계적 범함수 계산"></p>

-
  - 기댓값을 이용해 분산, 첨도, 공분산 등 여러 통계량을 계산 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img19.PNG" alt="분산"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img20.PNG" alt="첨도"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img21.PNG" alt="공분산"></p>

- 몬테카를로 샘플링(Monte Carlo)

  - 많은 경우, 기계학습 문제에선 확률분포가 비명시적.
  - 몬테카를로 샘플링은 데이터를 이용하여 기댓값을 추정하는 방법. 이산형 연속형 모두 성립.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day02_img22.PNG" alt="몬테카를로 샘플링"></p>

-
  - 독립추출이 보장되면 대수의 법칙(Law of large number)에 의해 수렴성을 보장한다.

# :pencil2: Doodle

- 어제에 이은 기본 복습. 학부 수업 첫 시간에 훑고 지나갔을 내용인데 아쉽게도 기억이 나지 않는다. 간결하게 놓치면 안될 부분만 짚어주는 강의라서 정리하기 좋다. 항상 수식 작성에 약해서 마무리는 직접 연산해보려 한다. 실제 학습에선 기계에게 시키겠지만, 유의미하길 바라며. 내가 정말 이해했다면 남한테 설명해줄 수 있어야 한다. 그런데 아직은 아니야. 코드 과제 자체는 아직 어렵지 않아 구현에 큰 품이 들지 않았다. 아마 놀라지 않게 워밍업으로 준비된 게 아닐까? 오늘의 끝은 알폰스 무하.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Alfons_Mucha_1896_Summer.jpg"></p>
<p align="center">Alphonse Maria Mucha, &ltDecorative panel from The Seasons - Summer&gt, 1896. Oil on panel, 103x54cm.</p>

- Day 2 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day1/Note.md "Day1 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day3/Note.md "Day3 Note")
