# 📙 Note

### Recurrent Neural Network and Language Modeling

- RNN

  - 시퀀스데이터가 입출력. 기본 구조는 이전 학습과 동일.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img00.PNG" alt="RNN basic structure"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img01.PNG" alt="RNN basic structure"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img02.PNG" alt="RNN basic structure"></p>

- Types of RNNs

  - One-to-one : Standard Neural Networks. 입출력이 단 하나인, 시퀀스 데이터가 아닌 일반적인 경우. ex) 사람의 몸무게, 키, 나이 등을 입력받고 그 사람의 고/저/정상혈압을 분류.
  - One-to-many : 입력은 하나, 출력은 여러 개. 대표적으로 Image Captioning. 하나의 이미지를 입력 받고 이미지에 대한 설명글에 필요한 단어들을 추출. 이 경우 첫 번에만 입력이 들어가므로 매 타임 스탭마다 들어가던 반복 입력은 0으로.
  - Many to one : 여러 입력값을 받아 최종 출력을 하나로. 대표적으로 Sentiment Classification. 이 예의 경우, 입력 문장의 각 단어를 워드 임베딩하여 각 타임스텝에서 받고, 결과적으로 하나의 아웃풋 도출.
  - Many to many : 입출력 모두 시퀀스 데이터. 대표적으로 Machine Translation. 이 경우는 입력을 다 받은 후 출력 생성을 하는 경우. Video classification on frame level의 경우, 입력과 동시에 출력 생성.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img03.PNG" alt="Types of RNNs"></p>

- Character-level Language Model

  - 언어 모델은 주어진 문자열 혹은 단어 순서를 바탕으로 다음 단어를 예측하는 테스크.
  - Many to many 형태.
  - 워드 임베딩 거친 후 언어 모델 수행.
  - 'hello' 예시. 'h'가 나올 땐 'e'를 예측해야 함.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img04.PNG" alt="Character-level Language Model with 'hello'"></p>

-
  - 위 예시 첫번째 아웃풋의 경우 'o'값이 제일 높으므로(4.1), 'e'값이(2.2) 가장 높아지는 방향으로 학습해야 함.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img05.PNG" alt="Character-level Language Model with 'hello'"></p>

-
  - 학습이 쌓일수록 출력값은 그럴듯해진다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img06.PNG" alt="모델의 학습 변화"></p>

- BPTT (BackPropagation Through Time)

  - BPTT : 기존 신경망의 역전파(backprop)와는 달리 타임 스텝별로 네트워크를 펼친 다음, 역전파 알고리즘을 사용.
  - 아주 많은 시퀀스가 주어질 때, 모든 아웃풋을 계산하고 로스 계산을 하려면 GPU가 눈물을 흘린다. -> 한 번에 학습할 데이터를 chunk로 잘라서 학습하는 것으로 해결.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img07.PNG" alt="BPTT-entire data"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img08.PNG" alt="BPTT-chunk data"></p>

-
  - Vanila RNN은 많이 사용되진 않는다. 역전파시 그래디언트가 너무 작아지거나, 반대로 너무 커져서 학습이 제대로 이뤄지지 않는 경우가 많기 때문. 이에 대한 해결은, BPTT에 조정을 가하는 것(Truncated BPTT). 그러나 이 또한 학습 데이터가 장기간에 걸쳐 패턴이 발생 할 땐 학습이 어렵다. 이제 대안은 RNN구조를 바꾸는 것(LSTM, GRU).
  - Truncated BPTT : BPTT는 전체의 타임 스텝마다 처음부터 끝까지 역전파를 하기 때문에 타임 스텝이 클 수록 계산량이 많아지는 문제가 있다. 이러한 계산량 문제를 해결하기 위해 전체 타임 스텝을 일정 구간으로 나눠 역전파를 하는 Truncated BPTT를 사용.

### LSTM and GRU

- LSTM (Long Short-Term Memory)

  - RNN의 히든 state에 cell-state를 추가한 구조.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img09.PNG" alt="LSTM"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img10.PNG" alt="LSTM"></p>

-
  - Cell state : 작은 linear interaction만을 적용시키면서 전체 체인을 계속 구동. LSTM은 cell state에 뭔가를 더하거나 없앨 수 있는 능력이 있는데, 이 능력은 gate라고 불리는 구조로 제어되며, 시그모이드 레이어와 Pointwise 곱셈으로 이루어져 있다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img11.PNG" alt="LSTM Cell state"></p>

-
  - Forget gate layer : LSTM의 첫 단계로는 cell state로부터 어떤 정보를 버릴 것인지를 정하는 것으로, sigmoid layer에 의해 결정된다. 이 단계에서 도출되는 값이 1이면 정보 보존, 0이면 비보존.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img12.PNG" alt="LSTM Forget gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img13.PNG" alt="LSTM Forget gate layer"></p>

-
  - Input gate layer : 다음 단계는 앞으로 들어오는 새로운 정보 중 어떤 것을 cell state에 저장할 것인지를 정한다. sigmoid layer인 input gate layer가 어떤 값을 업데이트지 정한 후 tanh layer가 새로운 후보값 벡터를 만든 후 cell state 업데이트를 준비.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img14.PNG" alt="LSTM Input gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img15.PNG" alt="LSTM Input gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img16.PNG" alt="LSTM Input gate layer"></p>

-
  - 이후 과거 state를 업데이트해서 새로운 cell state를 만든다.
  - Output gate layer : 마지막으로 무엇을 output으로 내보낼 지 정한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img17.PNG" alt="LSTM Output gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img18.PNG" alt="LSTM Output gate layer"></p>

- GRU (Gated Recurrent Unit)

  - LSTM의 구조를 경량화. 빠른 계산 시간. LSTM의 cell state와 hidden state를 일원화해서 hidden state vector만 존재. LSTM이나 그 경량화 버전 GRU나 동작은 비슷하니 필요하면 둘 다 돌려보기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img19.PNG" alt="GRU"></p>

-
  - Backpropagation in LSTM & GRU
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img20.PNG" alt="Backpropagation in LSTM & GRU"></p>

# ✏️ Doodle

- 분명 구면인데 익숙하지 않은 RNN. 볼 때마다 침침한 미분같은 친구. 설명을 들을 땐 일단 귀에 들어오지만 직접 구현 단계는 까마득하다. 강의와 관련된 논문을 요약하여 팀원과 공유하기로 했다. 남이 이해할 수 있는 글을 쓰려면 대체 얼마나 고민해야 하는걸까. 모쪼록 뭔가 얻을 수 있도록 열심히 좀 해. 오늘의 끝은 에른스트.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Max%20Ernst_1921_The_Elephant_Celebes.jpg"></p>
<p align="center">Max Ernst, &ltThe Elephant Celebes&gt, 1921. Oil on canvas, 125.4x107.9cm.</p>

- Day 26 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day25/Note.md "Day25 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day27/Note.md "Day27 Note")
