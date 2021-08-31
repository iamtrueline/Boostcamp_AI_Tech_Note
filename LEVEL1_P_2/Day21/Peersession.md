### 🔍 피어세션

- cutmix와 label smoothing : 현재는 label이 scalar로 return되지만, 이를 벡터로 바꿔야한다. (loss 함수도 수정필요)

### 🔍 개인 코드 리뷰

- 승찬

  - class imbalance문제는 class간 전체적인 비율을 고려해서 상위 4개만 유지, 나머지는 복제하면서 oversampling하여 해결했다.
  - facenet을 이용하여 미리 crop한 이미지를 저장하여 학습시켰다.

- 성욱

  - augmentation하면서 oversampling을 구현했다.
  - dataset get_item에서 train set과 valid set의 구분방법?
  - index로 구분이 가능하다. -> 하지만 k fold 이전에 aug하고싶다 -> init에서 aug를 이미 했기때문에 문제가됨
  - k fold를 구현하여 fold마다 모델을 다르게 적용해서 마지막에 평균으로 취합했다.

- 우창

  - efficient-b7을 pretrained model로 사용했다.
  - 하지만 batch-size가 4로 작아져서 학습이 오래걸렸다.

- 범수

  - MyModel에서 pretrained model로 resnext사용, 이후 3개의 classifier를 구현했다.
  - bbox를 cvlib을 이용해 찾아내 약간의 random하게 crop을 했다.
  - train dataset도 bbox를 이용해 crop하여 진행했다.

- 원진
  - pretrained model로 efficient 모델을 사용, 이후 3개의 classifier를 구현했다.
  - loss에서 label smoothing이 적용된 custom focal loss구현했다.
