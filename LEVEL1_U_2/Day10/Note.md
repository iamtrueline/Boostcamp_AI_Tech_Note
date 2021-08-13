# 📙 Note

### Sequential Models - Transformer

- Transformer

  - 시퀀셜 모델은 왜 다루기 어려울까? 같은 뜻이라도 어딘가 잘리거나(Trimmed), 중간에 뭔가 빠지거나(Omitted), 순서가 바뀔 수(Permuted)있는 데, 이런 데이터는 다루기 어렵다.
  - 트랜스포머(Transformer)는 attention 구조를 활용하여 시퀀스를 다루는 모델. 첫 시작은 기계어 번역이었다. 현재는 다방면에서 활용중.
  - 어떤 문장(시퀀스)이 주어질 때 다른 문장(시퀀스)으로 변경.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img00.PNG" alt="Transformer"></p>

-
  - 입력 시퀀스, 출력 시퀀스 개수와 도메인이 다를 수 있다.
  - RNN의 경우 들어간 개수만큼 재귀적으로 동작하지만 Transformer는 한 번 동작(encoder 단).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img01.PNG" alt="Transformer"></p>

- Transformer - Encoders

  - 인코더 구조 : Self-Attention -> Feed Forward Neural Network -> Next Encoder
  - Self-Attention : 주어진 인풋에 각각에 따른 벡터가 주어질 때, 하나의 벡터 뿐 아니라 나머지 벡터도 같이 고려. 특정 단어가 다른 단어와 어떤 관계성이 있는 지 고려하는 것. 단어마다 주어지는 벡터는 3개(Queries, Keys, Values). 각 단어가 주어질 때, 현재 인코딩할 단어의 Queries와 나머지 단어의 Keys를 내적하여 유사도를 구하고 Score 벡터를 생성하여 담는다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img02.PNG" alt="Self-Attention"></p>

-
  - Score 벡터는 Keys(Queries 벡터 차원과 같다) 벡터의 차원에 루트를 취한 값으로 나누고 Softmax를 거쳐 Nomalize. 이렇게 나온 것이 attention rate. 최종적으로 Value 벡터와 weighted sum 하여 최종값을 추출.
  - 행렬로 표현하면 다음과 같다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img03.PNG" alt="Self-Attention in matrix"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img04.PNG" alt="Self-Attention in matrix"></p>

-
  - Multi-headed attention(MHA) : Attention을 여러 번. 하나의 인풋에 대해 쿼리, 키, 밸류를 여러 개 생성. N번 반복하면 N개의 attention이 나오게 됨. 이 때 출력 차원을 맞추기 위한 후처리로 행렬곱 사용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img05.PNG" alt="Transformer 차원 맞추기"></p>

-
  - 인코딩 값 자체에 시퀀셜 정보는 들어가 있지 않다. 같은 단어가 다른 순서로 주어진 문장이 들간다해도, 주어진 입력이 같다면 같은 값이 나오니까. So, positional encoding 필요.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img06.PNG" alt="Positional encoding"></p>

- Transformer - Decoders

  - 인코더로부터 처리를 거친 키와 밸류값을 전달받는다.
  - 기본적으로 디코더와 반대 과정.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img07.PNG" alt="Encoder and Decoder"></p>

-
  - Transformer는 기존엔 번역 분야에서만 활용되다가 최근 이미지 분류 등 다양한 분야에서 활용 중. 당연히 변형은 유.

### Generative Models 1

- 단순히 모델 생성이 전부일까?

  - Generation : sample 생성.
  - Density estimation : 닮은 정도(확률값) 측정. 즉, 단순 생성 뿐 아니라 분류 모델을 포함.
  - Unsupervised representation learning : feature learning. 특징점 잡기.

- Basic Discrete Distributions

  - 확률값을 표현하는 데 필요한 파라미터는 카테고리-1 개.
  - 동전의 앞면 확률이 p 라면 뒷면은 p-1.
  - 주사위 확률을 표현할 때도 필요한 파라미터는 5.
  - 바이너리 데이터만 보더라도 필요한 파라미터는 2^n -1개. 즉, 너무 많다. 많으면 학습이 어려움. 이걸 어떻게 줄일까?
  - 모든 state가 독립적이라 가정하고 그냥 n으로 줄여버리기 -> 파라미터는 줄지만 표현력이 떨어진다. 그래서 등장하는 게 이 둘의 중간 어딘가, Conditional Independence.

- Conditional Independence

  - 두 개의 확정적 이론
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img08.PNG" alt="Chain rule and Bayes' rule"></p>

-
  - 가정
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img09.PNG" alt="Conditional Independence"></p>

-
  - Chain rule을 통하면 파라미터는 위와 같이 여전이 2^n -1.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img10.PNG" alt="Chain rule ex."></p>

-
  - Markov assumption : 파라미터가 바로 직전의(i+1 번째 파라미터가 i번째 픽셀의)게만 dependent하다는 가정. 이 경우 파라미터는 2n -1 로 축소.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img11.PNG" alt="Markov assumption"></p>

- Auto-regressive Model

  - 체인룰로 파라미터를 표현
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img12.PNG" alt="Auto-regressive Model"></p>

- NADE(Neural Autoregressive Density Estimator)

  - 입력 차원이 달라짐에 따라 weight이 바뀌는 Neural Network + n번째 파라미터를 위해 n-1번째 파라미터 정보만 필요한 Autoregressive.
  - NADE는 단순히 generation만 수행할 뿐 아니라 임의의 인풋에 대한 density를 계산할 수 있다.(explicit model)
  - Continuous Random Variables 의 경우 마지막에 Gaussian mixture model 활용.

- Pixel RNN

  - RNN +  Autoregressive.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img13.PNG" alt="Pixel RNN example"></p>

-
  - ordering에 따라 Row LSTM(상단 정보만을 활용), Diagonal BiLSTM(예측에 이전 정보를 다 활용한 RNN)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img14.PNG" alt="Row LSTM and Diagonal BiLSTM"></p>


# ✏️ Doodle

- 두 번째 주의 마지막 날. 시간이 빠르게 간다. 출근할 땐 안 그러던데. 재밌는 시간만 빨리 가는 게 아니라 소화 목표가 많은 날도 시간이 빨리 간다. 목표치만큼 달성했느냐에 답변한다면 '그렇지 않다'지만 충분히 만족은 한다. 다만 난도가 어렵고 공부량이 부족했으니 주말에 춤추기는 글렀다. 오늘의 끝은 마네.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Edouard_Manet_1863_Luncheon_on_the_Grass.jpg"></p>
<p align="center">Edouard Manet, &ltLuncheon on the Grass&gt, 1863. Oil on canvas, 208x264.5cm.</p>

- Day 10 마침.
