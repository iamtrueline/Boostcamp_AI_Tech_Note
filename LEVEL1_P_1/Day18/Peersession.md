## 🔍 마스크 데이터 분류 대회

- 다양한 시도

  - VGG → DenseNet활용하여 성능 증가
  - Crop만 진행 → 성능 증가 x
  - ResNet50활용 (Parameter의 수를 봤을 때, 적절한 것 같다)
  - Crop진행 → Shape의 문제 발생 → Shape이 같아야 Batch를 뽑아올 수 있는 것으로 보이나 어떻게 Shape을 맞춰줘야 하는지에 대해서는 미지수.
  - ResNext50_32x4d 활용
  - 얼굴 위치에 대한 분포도를 바탕으로 평균, 분산을 활용하여 적당한 Crop 진행 → 얼굴이 해당 위치에 있었으면 했지만 잘 나오지는 않음
  - 전처리를 활용하여 주름을 구분해낼 수 있다.(Contrast, Sharpness, Brightness, Color)

- 해 볼 시도

  - OverSampling
  - SMOTE → 직접 적용하기에 어려움이 있지만 시도 해볼 것이다.
  - Label이 작은 것을 랜덤 복제하여 Sampling 시도

- 질답

  - KFold는 Data 수가 너무 적을 때, Validation Set의 Robustness를 주기 위해서 활용하는 방안인데 코드에 직접 입력할 때 성능의 개선이 이루어졌다. 왜 그럴까?
  - → 이전 Fold에서의 개선된 Parameter가 다음 Fold로 이어짐으로서 성능 향상을 나타낸다.

  - Gradient Accumulation에서 Num_Accum으로 loss를 나누어주게 되는데, 왜 이렇게 하는가?
  - → 이유 모색 후 토의

  - Brightness & Contrast를 활용하여 배경을 아예 흰색으로 만들 수 있지 않을까?
  - → 일정 임계값 이하일 경우, 배경이 검은색이라면 얼굴이 날아갈 위험이 있다.

  - Focal Loss 직접 활용해 보았는가?
  - → Weight를 직접 조정할 수 있는데 이것이 Focal Loss의 방법과 유사한 것 같다.

  - 서버에서 깃헙으로 바로 업로드하는 방법이 있는가?
  - → 기존의 방식에서 조금 변화가 있어, 이제는 token을 입력해주면 서버에서 깃헙으로 업로드 할 수 있다.

- 코드 리뷰

  - 원진님, 우창님, 성욱님, 승찬님, 범수님
