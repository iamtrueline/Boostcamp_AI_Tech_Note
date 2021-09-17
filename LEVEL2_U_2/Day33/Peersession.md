## 📝 개인 학습

- 9강 강의 및 실습 코드 리뷰

## 🔎 Further Reading

- GPT-1
- BERT : Pre-training of deep bidirectional transformers for language understanding, NAACL’19
- SQuAD: Stanford Question Answering Dataset
- SWAG: A Large-scale Adversarial Dataset for Grounded Commonsense Inference

## 🎤 논문 리뷰 발표 및 질답

- GPT-1 발표 (강진선)
- BERT 발표 (이노아)
- in GPT, fine tuning에서 lr값을 왜 작게 취하는지? -> 논의.
- in BERT, 분류 문제를 풀 때 마스킹이 된 데이터를 인풋으로 받으면 원래 BERT의 테스크인 LM이랑 특성이 달라서 학습이 어렵다고 알고 있었는데, 마스킹 한것이 단순히 단어가 unknown 처리됐을 때랑 다른 건가? -> pre-training 단 입장에서는 인풋으로 무엇이 들어오든 결국 유사할 거 같다. 그러나 인풋에 따른 테스크의 목적이 다른 것이므로 과제 자체는 구분될 것이다.
- in BERT, 과연 NSP가 정말 효과가 있을까? -> 추가 학습

## 🍸 멘토링

- 시간 변경 : 1시
- 질문 : 다음주도 멘토링이 있나요?
- positional encoding 정리
- 앞으로 나올 논문들의 전체적인 흐름(각 논문들의 주요 차이 등) 소개
- 학습 논문을 위주로 구현해 볼만한 코드 추천
- 유익한 수다
