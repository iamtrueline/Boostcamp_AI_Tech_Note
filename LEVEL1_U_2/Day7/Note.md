# 📙 Note

### Optimization

- 용어 정의

  - 일반화(Generalization) : Training error와 Test error 차이가 적다면 일반화 성능이 좋다고 한다. 이는 학습 데이터에서만 잘 동작하는 게 아니라 실제 실험 데이터에서 잘 동작함을 의미한다. 다만 일반화 성능이 좋다고 해도 학습 데이터 자체의 성능이 낮을 수도 있다.
  - Under-fitting vs Over-fitting : 학습데이터는 잘 맞추지만 테스트데이터 적용은 잘 안되는 경우 Over-fitting, 학습 자체가 부족해서 학습데이터도 못 맞추는 경우 Under-fitting.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img00.PNG" alt="Under-fitting vs Over-fitting 그래프 예시"></p>

-
  - Crossvalidation : 학습 데이터와 학습에 쓰이지 않은 검증 데이터를 둘 다 사용해서 검증. k-fold cross validation이 가장 일반적이다. 이는 데이터 셋(학습 + 검증)을 k개의 subset으로 나누고 k-1번 subset까지 학습 후 마지막 subset으로 평가한다. 이 때 각 Iteration마다 test set을 다르게 할당하여 총 k개의 '데이터 폴드 세트'를 구성하므로 모델을 학습 및 훈련하는데 총 k번의 Iteration이 필요한 것이 특징. 각 데이터 폴드 세트에 대해서 나온 검증 결과들을 평균내어 최종적인 검증 결과를 도출하는 것이 일반적.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img01.PNG" alt="Cross-validation 예시"></p>

-
  - Bias and Variance : Variance가 낮다는 건 출력이 일관적이라는 것(목표점이 아니라도). Bias가 낮다는 건 평균적으로 목표점에 접근한 것.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img02.PNG" alt="Bias and Variance"></p>

-
  - Bias and Variance Tradeoff : 학습데이터에 노이즈가 있다고 가정했을 때, cost는 bias^2, variance, noise를 각각 더한 값으로 한쪽이 줄어들면 한 쪽이 늘어난다. Bias와 Variance 모두 줄이는 건 어렵다.
  - Bootstrapping : 검증을 하기 전 Random sampling을 적용하는 방법. 데이터 중에서 중복을 허용하여 m개를 뽑고, 그들의 평균을 구하기를 여러 번 반복.
  - Bagging : Bootstrapping AGGregatING. bootstrapping을 통해 Over-fitting을 줄일 수 있다.
  - Boosting : 여러 모델을 만들어 시퀀셜하게 합쳐서(not 독립적) 하나의 모델을 구성.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img03.PNG" alt="Bagging and Boosting"></p>

- 경사하강법 배치 사이즈 정하기.

  - 배치 사이즈는 작은 게 일반적으로 좋다. 실험적으로, 크면 Sharp Minimum에 도달, 작으면 Flat Minimum에 도달. Shart Minimum 에 도달한다는 건 일반화 성틍이 낮다는 것.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img04.PNG" alt="Flat Minimum, Sharp Minimum"></p>

- 경사하강법 용어 정의

  - Momentum : 기존 경사하강법 그래디언트 방식에 기존 방향성을 가지고 있는 베타값(모멘텀)을 추가. Gradient Descent를 통해 이동하는 과정에 일종의 ‘관성’을 주는 것. 이 모멘텀과 기존 그래디언트가 합쳐진 그래디언트는 한 번 흘러가는 방향성을 유지하기 때문에 학습력이 좋아짐.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img05.PNG" alt="Momentum 추가 식"></p>

-
  - Nesterov Accelerated Gradient(NAG) : 기존 모멘텀은 현재 방향성을 사용하고 Nesterov Accelerate은 직후 계산된 값을 미리 사용. 멈춰야 할 적절한 시점에서 제동을 거는 데에 훨씬 용이. Local Minimum에 더 빠른 도달.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img06.PNG" alt="NAG 식"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img07.PNG" alt="Momentum, NAG 비교"></p>

-
  - Adagrad : 변수들을 update할 때 각각의 변수마다 step size를 다르게 설정해서 이동하는 방식. step size = 변화량. 파라미터의 변화량을 G에 저장. 각 파라미터를 보며 많은 변화가 있었을 경우 적게 변화, 적은 변화가 있었을 경우 많이 변화시키려는 시도. 이 때 G는 그래디언트들의 제곱을 더한 것으로 계속 커진다. 식에 따르면 분모가 커지니 W는 계속 작아진다(멈춤).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img08.PNG" alt="Adagrad 식"></p>

-
  - Adadelta : Adagrad의 확장. G가 계속해서 커지는 것을 막아보자. 전체 시간이 아니라 특정 타임 스탬프동안의 파라미터만 보는 것. Learning rate이 없다. 즉, 바꿀 수 있는 값이 없어서 많이 활용되진 않음.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img09.PNG" alt="Adadelta 식"></p>

-
  - RMSprop : Adagrad의 단점(G가 커짐)을 해결하기 위한 또 다른 방법. Adagrad식에서 gradient의 제곱값을 더해나가면서 구한 Gt 부분을 합이 아니라 지수평균으로 바꾸어서 대체한 방법. G가 무한정 커지지는 않으면서 최근 변화량의 변수 간 상대적인 크기 차이는 유지.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img10.PNG" alt="RMSprop 식"></p>

-
  - Adam(Adaptive Moment Estimation) : RMSProp과 Momentum 방식을 효과적으로 합친 알고리즘. Momentum 방식과 유사하게 지금까지 계산해온 기울기의 지수평균을 저장하며, RMSProp과 유사하게 기울기의 제곱값의 지수평균을 저장.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img11.PNG" alt="Adam 식"></p>

- Regularization(정칙화)

  - 학습을 방해. 학습 데이터 뿐 아니라 테스트 데이터에도 잘 적용되도록 하는 것이 목적.
  - Early Stopping : 일반적으로 지속적인 학습에서 학습 에러가 적어지면 테스트 에러가 커진다. 이 차이가 벌어지기 시작할 때 학습을 멈춰버리는 것.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img12.PNG" alt="Early Stopping"></p>

-
  - Parameter Norm Penalty : 비용함수에 제곱을 더하거나(L2) 절댓값을 더해서(L1) 웨이트의 크기에 제한을 준다.
  - Data Augmentation : 데이터가 많으면 일반적으로 성능이 좋다. 그러나 데이터는 한정적이므로 어떤 식으로든 늘려야 한다. 예를 들어 특정 이미지를 돌리고 구기고 하는 등.
  - Noiserobustness : 입력 데이터에 노이즈를 더한다. Data Augmentation과의 차이점? 단순히 입력 뿐 아니라 웨이트에도 노이즈 끼기.
  - Labelsmoothing : 학습 데이터를 두 개 뽑아 섞는다. Division Boundary를 부드럽게 만들어준다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img13.PNG" alt="Labelsmoothing 예시"></p>

-
  - Dropout : 랜덤하게 몇 뉴런의(ex. 50%) 웨이트를 0으로 바꾼다. 일반적으로 사용 시 성능이 올라감.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img14.PNG" alt="Dropout"></p>

-
  - Batch Normalization : 평균과 분산을 조정하는 과정이 별도의 과정으로 떼어진 것이 아니라, 신경망 안에 포함되어 학습 시 평균과 분산을 조정하는 과정 역시 같이 조절. 일반적으론 성능 향상에 도움. 이에 파생으로 한 레이어만, 특정 그룹만 Normalization 하는 형태가 있다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img15.PNG" alt="Batch Normalization 예시"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img16.PNG" alt="Batch Normalization 파생"></p>

# ✏️ Doodle

- 정규 수업 외 화상 강의 클래스가 많았던 날. 도메인 결정에 도움 받을 수 있는 인터뷰와 시각화에 관한 다른 개론이 주제였다. 도메인은 내가 더 원하는 걸 가는 게 정답이라고 한다. 잘 배울 수 있는 틀안에서 시작 강의를 뭐로 할지 정하는 일은 오히려 어렵다. 일단은 설문대로 NLP 고. 난 그게 더 마음에 들어. 선택 과제로 주어진 Vision Transformer, Adversarial Auto-Encoder 는 강의의 도움 없이 짜기 힘들다. 팀원이 있어 도움을 받을 수 있는 게 다행. 하지만 아직 완벽한 이해는 불가. 코드 뜯는 것도 시간이 많이 소요되니 많이 더 열심히 해야 할 것. 오늘의 끝은 라파엘로.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Raffaello_1509_The_School_of_Athens_.jpg"></p>
<p align="center">Raffaello, &ltThe School of Athens&gt, 1509-1511. Fresco, 500x770cm.</p>

- Day 7 마침.
