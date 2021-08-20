## 📒 오늘의 질답 및 과제 분석

- (지난 질문) Custom data loader - batch_size 문제

  - Tensor는 concatenate를 통해 value 삽입. ~ 가장 긴 값을 찾고 순차 삽입.
  - functional.pad 사용
  - hstack 사용

- 과제

  - 흑마법 구현 : forward.hook 사용
  - TitanicDataset 접근 : 성욱님의 코드 리뷰.
  - __getitem__ 에서 학습 데이터가 아닐 경우, y를 반환하지 말라? : y는 라벨. train=True 여부를 판단하고 getitem에서 조건문을 사용하기.
  - init 함수 구현에 대한 자세한 설명 요 : 학습 레이블을 잡았을 때, 레이블을 제외한 것들이 features(데이터 목록(string)). ~ 멘토님께 이어 질문하기.

🚀 논문 리뷰

- Transformer (Attention is All needs you)

  - 구성 흐름 및 질답(Q, K, V 생성) 진행.
  - 참조 ↓
  - 나동빈님 강의
  - https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a8f8b4e-926a-4fec-baf5-03c31ece02e4/Untitled.png
  - https://nlpinkorean.github.io/illustrated-transformer/


📎 멘토링 질문

- 다음주면 이미지 분류 대회. 어떤 모델을 사용할지, 참조 자료가 있을지?
- 데이터셋에 관한 질문.
