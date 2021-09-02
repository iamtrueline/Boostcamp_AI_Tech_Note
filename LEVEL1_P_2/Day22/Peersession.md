## 🔍 마스크 데이터 분류 대회

- Focal Loss에서 weight의 역할
- Loss function에서의 retain_graph

## 📒 데이터 전처리

- FaceDetection을 통해 전처리된 데이터에서 좋은 결과를 얻었음.
- CutMix를 활용하여 학습 진행해봄.
 
## 📎 DataLoader

- 전이학습 시 레이어 파라미터 변경 문제 → __repr__에만 반영되고 실제 모델에는 반영되지 않는 것으로 생각됨.
- mask, gender, age클래스를 나누는 방법에 대해 논의해 봄.
- 데이터 로드 시 Shuffle 옵션이 제대로 동작하지 않는 것을 확인했고, 이를 수정했을 때 모델 성능 개선이 되었음
