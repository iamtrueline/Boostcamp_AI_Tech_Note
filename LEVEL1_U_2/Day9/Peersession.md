## 📎 새로운 캠퍼님에게 그라운드룰 소개

- 모더레이터 순서에 대해서 소개(강진선 -> 김범수 -> 박승찬 -> 심우창 - 우원진 -> 최성욱 -> 배민환)
- 코드리뷰를 위한 github 초대
 
## 🔍 이전 질문 리뷰

- 이전 시간에 대한 질문은 당일날 해결해서 생략
 
## 📒 금일 질문 목록

- 선택과제 3번(승찬님이 하시다가 막히거나 잘 이해되지 않았던 부분)

  - 이유 : gaussian을 제대로 이용하지 못해서 그런 것 같다.
  - Gaussian mixture를 왜 사용하는지 그리고 어떻게 사용해야 하는지에 대해서 궁금하다.
  - 주어진 MDN class를 참고하여 과제를 수행했다. <- 이상한 값이 섞여서 나왔다.

- 선택과제 3번 추가 질문

  - hidden layer로 들어가서 n_gaussians으로 나오기 때문에 이 부분을 통해서 shape를 맞춰줬다(코드상에 맞춰져 있었다).
  - 행렬곱인것 같다.

- foward부분에서 shape를 어떻게 맞춰줬는지?
- 코드상에 x.mm이 무엇을 의미하는지? 

- 선택과제 3번 참고 자료
  - 진선님이 참고하신 블로그(https://mikedusenberry.com/mixture-density-networks)

- 필수과제(MHA)에서 Q,K,V의 개수에서 K와 V는 같아야 되지만 Q는 달라도 된다 - 라고 하셨는데 이 부분이 잘 이해가 되지 않는다.

  - 선택 과제에 대해서 해설 듣고 거기서도 이해가 안 되면 주말에 찾아보고 그것으로도 해결이 안되면 멘토님에게 물어보기 

- LSTM에서 update cell이랑 output gate가 이해가 잘 안되었습니다. 

  - forget gate : 이전의 hidden state와 가중치를 시그모이드 해준 결과이다.
  - input gate : 전 hidden state와 가중치를 시그모이드 해주고. hidden state에서 
  - update cell : 이전 cell state에서 다음으로 전달할 cell state구하는 방법으로 과거에 잊어버릴것(ft(이전 hidden state 시그모이드를 거친 값) * Ct-1(이전 cell state))은 잊어버리고 새로 기억할것(it(이전 hidden state 시그모이드를 거친 값) * Ct(hidden state가 tanh를 거친 값))은 기억하자
  - output gate : ot(이전 hidden state에서 시그모이드 거친 값) * (다음 cell state에서 tanh를 거친값)이다.

## 📎 선택과제 정답 살펴보기

- 선택과제 3 - softmax함수 인자로 dim을 주는게 어떤 의미인가? 

  - softmax연산을 해당 dim을 기준으로 한다.

- 선택과제 1 - residual부분 -> 통합적인 구조를 만들고 싶을때 사용
- 선택과제 1 - attention list부분
- 선택과제 1 - encoder부분에서 MHA 후 norm하기 전 원래값 더해주는 부분
