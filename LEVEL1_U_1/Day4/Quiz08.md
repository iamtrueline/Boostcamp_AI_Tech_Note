## 🍅 AI Math 9강 퀴즈 - CNN 첫걸음 1~5

### 1. 다음 보기 중, 연속적인 변수에 대한 함수 f, g사이의 convolution을 나타내는 수식으로 가장 적절한 것을 고르시오.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img15.PNG" alt="보기"></p>

- 답 : 3
- 해설 : 연속적인 변수에 대한 함수는 3번이다.

### 2. 입력 벡터 x 와 가중치 벡터 V가 다음과 같이 주어질 때, 다음 보기 중 올바른 h를 고르시오. 이 때, k는 V의 사이즈이고, 인덱스는 1부터 시작한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img16.PNG" alt="보기"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img17.PNG" alt="보기"></p>

- 답 : 1
- 해설 : 주어진 식대로 전개하면 h는 1번이다.

### 3. 벡터 x와 h가 다음과 같이 주어질 때, y1값을 구하시오. m은 h의 원소의 개수이고, 인덱스는 1부터 시작한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img18.PNG" alt="보기"></p>

- 답 : 14
- 해설 : y1 = x1 X h1 + x2 X h2 = 14

### 4. 입력 행렬 X와 커널 K가 다음과 같이 주어질 때,  Y(1,2)값을 구하시오.  m은 K의 행 사이즈,  n 은 K의 열 사이즈이고, 인덱스는 1부터 시작한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img19.PNG" alt="보기"></p>

- 답 : 5
- 해설 : Y(1,2) = K(1,1)*X(1,2) + K(1,2)*X(1,3) + K(2,1)*X(2,2) + K(2,2)X(2,3) = 0 + 2 + 3 + 0 = 5

### 5. 입력 행렬 X와 커널 K가 다음과 같이 주어질 때, Y(2,2) + Y(3,3)값을 구하시오. m은 K의 행 사이즈,  n은 K의 열 사이즈이고, 인덱스는 1부터 시작한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img20.PNG" alt="보기"></p>

- 답 : 9
- 해설 : Y(2,2) + Y(3,3) = (1 + 3) + (3 + 4 - 2) = 9
