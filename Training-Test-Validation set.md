# Training-Test-Validation set

- Original set에서 모델의 학습 중 이용하는 건 Training set. 학습 완료 후 마지막 성능 측정을 위한 데이터가 Test set.
- 학습 중 성능을 더 정밀하게 측정하기 위해 Training set을 다시 두 파트 - Training, Validation set으로 나눈다. 마찬가지로 학습에 사용되는 건 Training, 성능 측정에 사용되는 건 Validation.
- Test set과 Validation set의 차이는 전자는 마지막 한 번만 수행, 후자는 학습 중 다회 모델 성능 측정에 사용된다는 것.
- 일반적으로 Validation set 측정 결과가 높은 모델을 최종 모델로 채택하며, 데이터가 겹치지 않으므로 최종 Test set 측정 결과와 오차가 있을 수 있다.
- Original set에서 셋을 나누는 일반적 비율은 Training : Test : Validation = 6 : 2 : 2. 사용자 임의로 조정 가능.
