# 📙 Note

### 차트의 요소 3-1 ~ 3-4강

- Text in Viz

  - 시각표현이 줄 수 없는 설명 추가를 위해 필요.
  - 잘못된 전달에서 생기는 오해도 줄인다. 그러나 과다 사용은 지양.
  - Title : 가장 큰 주제 (subTitle 포함). set_title.
  - Label : 축에 해당하는 데이터. set_xlabel, set_ylabel.
  - Tick Label : 축에 눈금을 사용하여 스케일 정보 추가.
  - Legend : 범례. 한 그래프에서 2개 이상의 서로 다른 데이터를 분류. label = legend 형식으로 사용.
  - Annotation(Text) : 그 외 설명. ax.text || fig.text.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img00.PNG" alt="Anatomy of a Figure"></p>

-
  - Text 기본 속성 : family, size, fontsize, style, fontstyle, weight, fontweight.
  - Details : color, linespacing, backgroundcolor, alpha, zorder, visible.
  - Alignment : ha, va, rotation, multialignment.
  - Advanced : bbox.
  - 최대한 신속하고 정확하게 인식할 수 있는 가시 정보가 목표.

- Color in Viz

  - 첫 눈에 들어오는 정보 중 하나.
  - 다만 심미와 정보 전달의 목적은 다르다.
  - 가장 중요한 것은 독자에게 원하는 인사이트를 전달하는 것.
  - 이미 널리 사용하는 색에는 이유가 있다. (ex. 따뜻함은 빨강, 차가움은 파랑)

- Color Palette

  - 범주형(Categorical, Discrete, Qualitative) : 독립된 색상으로 구성되어 범주형 변수에 사용. 최대 10개 색상까지 권장하며 그 외는 기타로 묶기. 채도, 명도 조절이 아닌 색상 조절로 구분.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img01.PNG" alt="범주형"></p>

-
  - 연속형(Sequential) : 정렬된 값을 가지는 순서형, 연속형 변수에 적합. 단일 색조를 추천하며, 균일한 색상 변화가 중요. 깃허브 커밋 그래프가 예시.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img02.PNG" alt="연속형"></p>

-
  - 발산형 (Diverg) : 연속형과 유사하지만 중앙을 기준으로 발산하는 형태. 상반된 값이나 서로 다른 2개 데이터 표현에 적합. 양 끝으로 갈수록 색이 진해지며 중앙색은 편향되지 않는 게 중요.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img03.PNG" alt="발산형"></p>

- 색 사용 팁

  - 강조와 대비. 명도, 색상, 채도, 보색 대비를 적절히 이용하기.
  - 색각 이상에 대비. 적절한 색 배합이 이상적이지만 불가하다면 큐브 배치처럼 각도를 다르게 하는 등 대안 채용.

- Facet?

  - 분할. 화면 상에 View를 분할 및 추가하여 다양한 관점을 전달하기. 같은 데이터셋에 서로 다른 인코딩을 통해 다른 인사이트를 제공하여 같은 방법으로 동시에 여러 피쳐를 보거나 큰 틀에서 보이지 않는 세세한 부분들을 보기에 용이.

- Figure and Axes

  - Figure : 큰 틀. 언제나 1개.
  - Ax : 각 플롯이 들어가는 공간. 여러 개 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img04.PNG" alt="Figure and Axes"></p>

-
  - Subplot : plt.subplot(), plt.figure() + fig.add_subplot(), plt.subplots()
  - Grid Spec : fig.add_grid_spec(), fig.subplot2grid()
  - Inner Subplot : ax.inset_axes(), make_axes_locatable(ax)

- More Tips

  - Grid는 심플하게. 기본 그리드 외에도 사선, 방사형 등 다양한 형태가 있다.
  - 그래프의 이해를 돕기 위해 선, 면을 추가할 수도 있다.
  - 웹의 css처럼 설정을 한 번에 바꿀 수 있는 여러 테마도 있다. (ex. fivefhirtyeight)

### Multi-GPU 학습

- Multi-GPU

  - 성능 좋은 GPU가 많으니 여러 개 불러오자.
  - Node = 컴퓨터. Node 안에는 여러 GPU가 있을 수 있음. 한 대에 4~8대까지 들어갈 수 있다. 부럽다. (Single Node Multi GPU)
  - 학습 분산은 모델을 나누거나 데이터를 나누는 방식으로 나눈다.
  - 모델 병렬화 : 모델을 나누는건 예전부터 썼지만(alexnet) 모델의 병목, 파이프라인의 어려움으로 인해 모델 병렬화는 고난이도 과제.
  - 모델 병렬화를 잘못하게 된다면 효과를 볼 수 없다. 작업이 겹치지 않고 순서대로 진행(보기 중 위). 효과를 보려면 배치 처리를 잘 해야 한다(보기 중 아래).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img05.PNG" alt="모델 병렬화"></p>

-
  - 데이터 병렬화 : 데이터 쪼개서 각각학습, 각 로스율 그래디언트 계산, 결과의 평균을 합치기로 진행. minibatch 수식과 유사하나 한번에 여러 GPU에서 수행된다는 점이 다르다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img06.PNG" alt="데이터 병렬화"></p>

-
  - 파이토치에서 DataParallel은 단순히 데이터를 분배후 평균을 취하는데, 이 때 GPU 사용 불균형이 발생. 한 GPU에 병목이 발생해 배치 사이즈가 감소한다. 반면 DistributedDataParallel은 각 CPU마다 프로세스를 생성하여 개별 GPU에 할당한다. 기본적으로 DataParallel이나, 개별적으로 연산의 평균을 내는 점이 다르다.

### Hyperparameter Tuning

- Hyperparameter

  - 사람이 직접 지정해줄 값. learning rate, 모델 크기, optimizer 등.
  - 모델은 잘 되는 친구들이 이미 있다. 데이터는 많을수록 좋고. 그럼 내가 변화할 수 있는 값은? Hyperparameter.
  - 기본적인 세팅으로 학습 후 더 좋은 성능을 위함 바람과 여러 결과를 위해 처리해보기.
  - 가장 기본적인 방법은 grid vs random. 최근에는 베이지안 기반 기법(ex. BOHB)들이 주도.
  - grid : 어떤 값을 일정 범위 내에서 차례로 골라 찾기.
  - random : 랜덤 값 찾기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day14_img07.PNG" alt="grid vs random"></p>

- Ray

  - multi-node multi processing 지원 모듈. ML/DL의 병렬 처리를 위해 개발되었고 기본적으로 현재의 분산병렬 ML/DL 모듈의 표준이다. Hyperparameter Search를 위한 다양한 모듈 제공.

### PyTorch Troubleshooting

- OOM(Out Of Memory)

  - 왜? 어디서? 발생했는지 찾기 어려운 문제. '메모리가 어디서 터진걸까'를 찾기 위해 이전 상황을 알고 싶지만 파악이 어렵다.
  - 보통은 배치사이즈를 줄이고 전부 비운 후 다시 돌리면 해결.

- 그 외 문제 해결 팁

  - GPUUtil : nvidia-smi 처럼 GPU의 상태를 보여주는 모듈. iter마다 메모리가 늘어나는지 확인 가능(showUtilization). 메모리 누수가 어디서 발생하는지 알기 쉽다.
  - torch.cuda.empty_cache() : 사용되지 않은 GPU상 cache를 정리하여 가용 메모리를 확보. reset 대신 쓰기 좋다.
  - tensor로 처리된 변수는 GPU 상에 메모리를 사용한다. loop 연산 안에 있을 때 GPU에 computational graph를 생성(메모리 잠식). 1-d tensor 쓸거면 python 기본 객체로 변환하여 처리할 것.
  - del : 필요가 없어진 변수는 적절히 삭제할 것. python의 메모리 배치 특성상 loop 이 끝나도 메모리를 차지한다.
  - 가능 배치 사이즈 실험해 보기. 갑자기 OOM 발생? 일단 배치 사이즈 1로 실행.
  - torch.no_grad() : Inference 시점에서 사용. backward pass에서 메모리 버퍼가 발생하지 않는다.
  - colab에서 너무 큰 사이즈는 실행하지 말 것(linear, CNN, LSTM).
  - CNN의 대부분의 에러는 크기가 안 맞아서 생기는 경우.
  - tensor의 float precision을 16bit로 줄일 수도 있음.

# ✏️ Doodle

- 첫 번째 U스테이지가 끝났다. 마지막은 파이토치를 직접 돌리는 시간이 많았다. 그런데도 아직 완전히 파악은 못했다. 내가 모르는 새로운 언어를 배우는 느낌이야. 배울 때 어렵고, 발음하면 기쁘지만, 뒤돌면 잊는다. 모쪼록 P스테이지에서 내게도 팀에게도 도움이 될 수 있는 기회가 있길 바라며. 오늘의 끝은 오귀스트 르누아르.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Pierre_Auguste_Renoir_1883_Country_Dance.jpg"></p>
<p align="center">Pierre Auguste Renoir, &ltCountry Dance&gt, 1883. Oil on canvas, 180x90cm.</p>

- Day 14 마침.
