## 🔍 이전 질문 리뷰

- Question - SGD의 연산량이 GD보다 연산량이 더 많아서 덜 효율적이지 않는가?
  - 경사하강법의 종류 : BGD(Batch Gradient Descent), SGD(Stochastic Gradient Descent), MSGD(Mini-batch Stochastic Gradient Descent, 지난 시간에 SGD라고 생각했던 것) => 그러므로 정확한 용어로 사용하면 MSGD의 연산량이 BGD보다 연산량이 더 효율적인가? *통용적으로 SGD라고 하면 MSGD를 뜻한다.
  - iteration : mini_bach를 한 번 학습한 것 *BGD는 mini_bach가 total_data이고 SGD는 1개이고 MSGD에서는 지정한 mini_bach 개수이다.
  - epoch : total_data를 한 번 학습을 끝낸 것

- Answer
  - iteration의 횟수는 BGD가 가장 적지만 1 iteration을 하는데 시간이 가장 오래 걸리며 SGD는 1 iteration 당 1개의 데이터만 학습시키므로 1 epoch를 하는데 많은 iteraion이 필요하다. MSGD의 경우는 mini_batch의 수에 따라 1 epoch 당 iteraion의 수를 결정하므로 현실적인 HW성능을 고려할 수 있다는 점에서 효율성이 좋을 것이다.
  - 효율적이려면 가중치 W를 학습시키는 시간의 복잡도가 낮을수록 좋다.
  -iteration당 시간 복잡도 *(total_data : 데이터의 총 개수, d : 임의의 일부 데이터 사이즈, batch size : 사용자가 저한 mini_batch 크기)
  - GD : O( total_data *^2)
  - SGD : O(1 * d^2)
  - MSGD : O(batch size * d^2 )

## 📒 금일 질문 목록

- 왜 ReLU가 비선형 함수인가?
  - 선형함수의 특징 
  - 그래프로 그렸을때 직선이어야 한다. 즉, 선이 중간에 꺾이면 안된다. 
  - 매트릭스로 표현할때 표현이 가능해야 한다.
  - 함수가 중첩이 되더라도 선형이 된다.  
  - ex) f(x) = ax + b, f(f(x)) = f(ax+b) = a(ax+b) + b = a^2 * x + ab + b
  - 동차성 : f(ax) = a(fx)과 가산성 : f(x1 + x2) = f(x1) + f(x2)을 만족해야 한다.

- sigmoid와 ReLU 차이
  - sigmoid를 많이 사용할 시, gradient vanishing 현상이 나타날 수 있다. 
  - sigmoid 미분시 값이 커질수록 값이 작아지므로 gradient vanishing 현상이 나타날 수 있다. 
  - ReLU(x의 값이 0 이상일때) 미분값이 1임으로 중첩을 많이 하더라도 gradient vanishing현상이 나타나지 않는다. => 따라서 sigmoid보다 relu가 활성화 함수를 여러 번 중첩을 할 때 좋은 성능을 낸다.

- KL-Divergence 
  - 분산이 다를때 사용한다.

## 📎 멘토링시간 질문 정하기

- AI 직무에 학부생이 살아남을 수 있나?
- AI과정에 통계학에 대한 지식? 얼마나 필요한가? 어떤 곳에 활용될 수 있는가?
- 박기훈 멘토님의 현재 직무, 하고 계신 일은 무엇인가요?
- 멘토활동 어떻신가요?
- 부스트캠프 기간 중에 커리어에 도움이 될만한 활동 추천 내용이 있나요?
- 멘토활동을 참여하게 된 계기.
- 네트워킹데이? 커넥팅데이? : 어떤식으로 진행 되었는지, 무엇을 하는지에 대해서
