## 🍅 AI Math 10강 퀴즈 - RNN 첫걸음 1~5

### 1. 다음 보기 중 시퀀스 데이터와 가장 거리가 먼 데이터를 고르시오.

- 답 : 이미지 데이터
- 해설 : 이미지 데이터는 시퀀스 데이터와 거리가 멀다.

### 2. 다음과 같은 시퀀스 데이터 X가 주어졌을 때, 다음 보기 중 베이즈 법칙에 따라 전개한 X에 대한 확률분포를 고르시오. X = [X1, X2, ... , XT]
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day05_img01.PNG" alt="보기"></p>

- 답 : 2
- 해설 : 베이즈 법칙에 따라 전개하면 2번식이다.

### 3. RNN의 잠재변수는 다음 순서의 잠재변수를 모델링하기 위한 입력 값으로 사용될 수 있는가?

- 답 : 예
- 해설 : 사용될 수 있다.

### 4. 시퀀스 길이가 길어지는 경우, Vanila RNN에서 발생할 수 있는 기울기 소실문제를 해결하기 위한 방안이 아닌 것을 고르시오.

- 답 : CNN (Convolutional Neural Network)
- 해설 : 기울기 소실문제를 해결하기 위한 방안은 LSTM, GRU가 있다.

### 5. BPTT를 통해 RNN의 가중치행렬의 미분을 계산했을 때, 아래 식의 항들 중 시퀀스 길이가 길어졌을 때 불안정해지기 쉬운 항을 고르시오.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day05_img02.PNG" alt="보기"></p>

- 답 : 2
- 해설 : 2번 항이 불안정해지기 쉽다.
