## 🔍 이전 질문 리뷰

- ViT(Visual Transformer): 금일(21210811) 19시 멘토링 시간에 질문하기로 함.
- 각 Patch를 차원이 줄여진 잠재 벡터(latent vector)로 볼 수 있는가?
- MNIST dataset 사용 기준 각 (4,4)의 크기의 Patch 49개가 생성된다. 

## 📒금일 질문 목록

- CNN 수강 관련 질문
  - Dense layer를 잘 이해하지 못하겠다.
  - Fully Connected Layer과 같은 것.
  - Dense layer의 가중치 또한 학습이 진행되는가?
  - 에러에 따라 모든 (Conv, FCN)의 가중치들의 학습이 진행된다.
  - Convolution 연산에서 가중치의 차원은 (kernel_W, kernel_H, in_channel, out_channel)과 같다.  그렇다면 in_channel 기준으로 같은 값으로 연산이 진행되는지(Broadcasting) 또는 각 in_channel마다 다른 값을 가지는지 궁금하다.
  - 강의에서 학습할 가중치의 개수가 “kernel_W * kernel_H * in_channel * out_channel” 이라고 설명한 것으로 미루어 보아, 각각 다른 in_channel 가중치는 각각 다른 값을 가질 것이라고 생각된다.
  - e.g. in_channel 기준 각각 다른 가중치의 값은 다음과 같다. (parameter[0,0,:,0])

## 📎 선택과제 3번 살펴보기

- Mixture_density_Network_문제
  - 일대일 대응이 아닌 그래프에 대해 회귀(근사)를 어떻게 할 것인가?
  - 위 식에서 변수 y의 의미
  - 가우시안 분포의 변수로 생각됨.
  - 또한 위의 식은 x, y축이 서로 바뀐 것으로 생각됨.
  - 과제 설명 중 MSELoss(Mean Squared Error Loss)를 사용하지 못한다고 했다. 이에 관한 질문.
  - 로그 우도(Log Likelihood)를 사용하려고 한 것 같다.
  - Gumbel softmax sampling에 대해 알고싶다.

## 📎 ViT 관련 추가 질문

- Q, K, V 가 각각 의미하는 것이 무엇일까?
- 단어와의 연관성, cosine 유사도 관련 설명 진행함
