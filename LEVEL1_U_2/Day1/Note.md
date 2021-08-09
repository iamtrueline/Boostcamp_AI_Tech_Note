# :orange_book: Note 

### 딥러닝 기본 용어 설명 - Historical review

- 인공지능

  - 인간의 지능을 모방.
  - 다량의 데이터를 통해 학습하고 알고리즘을 갖추는 것.
  - 딥러닝은 기계학습 안에, 기계학습은 인공지능 안에 속한 개념.

- 딥러닝

  - Key : Data, Model, Loss Function, Algorithm.
  - Data : 풀고자 하는 문제에 따라 정해지는 범위 및 속성.
  - Model : 주어진 Data로 학습을 하는 기계학습 알고리즘.
  - Loss Function : 학습 목표의 근사치에 접근하기 위한(최적화) 응용식.
  - Algorithm : 어떤 문제를 풀기 위해 명확히 명시된 구체적인 계산법.

- 딥러닝 역사

 - 2012 > AlexNet :  2012년에 이미지 인식 대회 ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 우승을 한 CNN. 딥러닝을 활용해 첫 번째로 수상했음.
 - 2013 > DQN : 딥마인드가 강화학습으로 아타리 아케이드 게임을 풀 때 사용한 방식.
 - 2014 > Encoder / Decoder
 - 2014 > Adam Optimizer : 학습 시 가장 무난하게 사용할 수 있는 Optimizer. 특히 사용할 수 있는 자원이 한정적일 때.
 - 2015 > Generative Adversarial Network(GAN) : 비지도 학습에 사용되는 인공지능 알고리즘.
 - 2015 > Residual Network : 네트워크를 깊게 쌓을 수 있도록 만들어준 구조.
 - 2017 > Transformer
 - 2018 > BERT (fine-tuned NLP models) : Bidirection을 사용하는 NLP 모델.
 - 2019 > BIG Language Models : 1,750억 개의 파라미터로 구성된 모델.
 - 2020 > Self Supervised Learning : 비지도 학습.

### 뉴럴 네트워크 - MLP (Multi-Layer Perceptron)

- 신경망

  - 정의 : 뉴럴 네트워크(neural network)는 신경회로 또는 신경의 망(網)으로, 현대적 의미에서는 인공 뉴런이나 노드로 구성된 인공 신경망.
  - 인공지능은 테마는 기본적으로 인간의 지능을 모방하는 것이지만, 반드시 인간의 뇌와 동일한 방법론을 쓸 필요는 없다. 비행기가 반드시 새 모양이어야 날 수 있는 게 아니듯.
  - 인공지능에서 신경망은 특정 목표에 근사하는 값을 도출하기 위해 행렬 연산, 비선형 연산, +a가 반복적으로 일어나는 연산.

- 딥러닝 네트웍스

  - 보통 인공지능 문제에선 다차원 인풋 아웃풋을 다룬다. 이는 행렬 연산 = 선형 변환 뿐 아니라 비선형 변환도 포함한다.
  - 딥러닝은 신경망을 여러 층 쌓는 것. MLP.
  - Activation functions : 선형 결합 후 비선형 변환을 통해 더 적합한 결과를 도출하기 위해 사용하는 function. (ex. ReLU, Sigmoid)
  - Loss function? 실제값과 예측값 사이의 오차를 줄이는 것이 목표. 이 때, 몇 개 뜨는 이상치의 값을 맞추려하다 보면 전체 결과가 틀어질 수 있음. 문제마다 최적의 Loss function은 다르다. 적절한 것을 적절하게 골라보기.

### Introduction to Visualization 1-1 ~ 1-3강

- 데이터 시각화

  - 데이터를 그래픽 요소로 매핑하여 시각적으로 표현하는 것.
  - 왜 시각화 하는지, 누구를 대상으로 한느지, 어떤 데이터를 시각화할지, 어떤 흐름으로 인사이트를 전달할지, 내용에 맞는 효과적인 방법을 사용하는지, UI측면에서 만족스러운 디자인을 가지는지 고려해야한다.
  - 연구에서 다루는 시각화와 개발에서 다루는 시각화는 다름.
  - 100점은 없다.
  - 지금까지 연구되고 사용된 시각화 모범 사례를 통해 좋은 시각화를 만들 수 있다.

- 데이터 in 시각화

  - 데이터 시각화를 위해서는 데이터가 우선적으로 필요.
  - 시각화를 진행할 데이터 : 데이터셋 관점(global), 개별 데이터 관점(local)
  - 데이터셋 종류 : 정형 테이터, 시계열 데이터, 지리 데이터, 관계형(네트워크)데이터, 계층적 데이터 등.
  - 정형 데이터 : 일반적으로 CSV로 다룰 수 있는 데이터. 가장 쉽게 시각화할 수 있는 데이터셋. 통계적 특성과 feature 사이 관계, 데이터 간 관계, 데이터 간 비교 사용.
  - 시계열 데이터 : 시간흐름에 따른 데이트. 기온, 주가 등 정형데이터와 음성,비디오와 같은 비정형 데이터 존재. 시간 흐름에 따른 추세(Trend), 계절성(Seasonality), 주기성(Cycle) 등을 살핌.
  - 지리 데이터 : 거리, 경로, 분포 등 다양한 실사용. 지도 정보와 실제 전달한 데이터 간 조화가 중요.
  - 관계 데이터 : 객체와 객체 간의 관계를 시각화. 객체는 Node로, 관계는 Link로. 크기, 색 수 등으로 가중치 표현. 특히 계층적 데이터는 관계 중에서도 포함 관계가 분명한 데이터로, Tree, Treemap, Sunburst 등이 대표적.
  - 데이터의 종류는 대표적으로 4가지 > 수치형(연속형, 이산형), 범주형(명목형, 순서형)으로 나뉜다.

- 시각화

  - 마크와 채널 : 마크는 점, 선, 면으로 이루어진 데이터 시각화. 채널은 각 마크를 변경할 수 있는 요소들.
  - 전주의적 속성(Pre-attentive Attribute) : 주의를 주지 않아도 인지하게 되는 요소. 동시에 사용하면 인지하기 어렵다. 적절한 시각적 분리(visual pop-out) 필요.

# :pencil2: Doodle

- 딥러닝의 개괄과 시각화의 기본을 훑어보는 날. 파이토치 사용이 능숙치 않아 백지 코딩이 불가능. 프리코스 강의가 열려있으니 추천받은 지점부터 수강해야겠다. 옛날에 썼던 문서와 깃허브를 둘러보니 생각보다 문자 이미지 인식 관련한 프로젝트가 많았다. 기성 숫자 인식 -> 필기 숫자 인식 -> 필기 한글 인식 순서로 만들다가 한글 인식은 마무리를 못했다. 내일 NLP와 CV 도메인에 대한 길잡이가 제공된다고 한다. 완료가 좋을까, 시작이 좋을까? 일단 새로운 한 주 워밍업 종료. 오늘의 끝은 모네.

<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Claude_Monet_1875_Woman_with_a_Parasol_Madame_Monet_and_Her_Son.jpg"></p>
<p align="center">Claude Monet, &ltWoman with a Parasol – Madame Monet and Her Son&gt, 1875. Oil on canvas, 100x81cm.</p>

- Day 1 마침.
