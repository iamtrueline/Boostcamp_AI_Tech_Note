# Federated Learning

- 다수의 로컬 클라이언트와 하나의 중앙 서버가 협력하여 데이터가 탈중앙화된 상황에서 글로벌 모델을 학습하는 기술.
- Data를 서버로 보내는 것이 아니라 모바일 환경에 그대로 두는 방법.즉, 글로벌 모델을 학습하고, 이 ‘모델 학습의 결과’를 서버에서 종합하는 형태.
- 즉답이 필요할 때, 프라이버시 보호가 필요할 때 유용.
- 서버에서는 Aggregation model이 동작하며 model weight를 각 모바일 환경에 전달 -> 각 모바일 디바이스는 해당 환경에서의 데이터를 이용해 weight를 업데이트하고 서버로 전송 -> Aggregation model은 다시 이 weights들을 받아 합치고 다시 학습 사이클이 시작.
- 분산 학습은 데이터를 먼저 중앙에서 모은 다음, 여러 컴퓨팅 리소스로 분산을 시키는 형태로, 데이터 불균형이 일어나지 않지만 연합 학습은 일어날 수 있다.
