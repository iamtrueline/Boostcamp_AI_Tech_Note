# 📙 Note

### Ensemble

- Ensemble(앙상블)

  - 싱글 모델보다 더 나은 성능을 위해 서로 다른 여러 학습 모델을 사용하는 것.
  - Boosting : 복원추출하면서 잘못 분류한 데이터에 대해 가중치를 주어 샘플링 확률을 높이는 방법. 이상치에 약할 수 있고(오버피팅 가능성도 유) 직렬 모델이라 속도가 느리다. 다만 속도는 병렬화 시킨 형태 존재해서 효율 높임. Bias가 큰 모형에 적합.
  - Bagging(Bootstrap aggregating) : 복원추출을 통해 각각 다른데이터로 병렬 학습 후 Aggregating을 통해 결과 도출. 데이터의 수가 적은 경우에도 오버피팅을 줄이면서 좋은 성능을 낼 수 있다. 일반적인 Soft Vote(Regression), Hard Vote(Classification) 방식 차용. Bias가 작고 Variance가 큰 모형에 적합.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day19_img00.PNG" alt="Voting"></p>

-
  - Cross Validation : 훈련 셋과 검증 셋 분리는 필수. 다만 검증 셋을 학습에 활용하고 싶다 -> K-Fold Cross Validation. 가능한 경우를 모두 고려 + Split시에 Class분포 까지 고려. 일정한 셋을 가져가는 게 중요. 80-20이 일반적.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day19_img01.PNG" alt="K-Fold"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day19_img02.PNG" alt="K-Fold"></p>

-
  - TTA(Test Time Augmentation) : 테스트 중에 Augmentation. 테스트 이미지를 Augmentation후 모델 추론, 출력된 여러가지 결과를 앙상블. 다양한 환경에 대한 대응이 좋아진다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day19_img03.PNG" alt="TTA"></p>

-
  - 항상 앙상블을 돌려야 하나? : 당연히 효과가 있으므로 시도 유익 높음. 다만 시간이 필요하고, 이는 성능과 효율을 잴 때 뺄 수 없는 고려사항. 딥러닝은 무거우니까.

- Hyperparameter Optimization

  - 시스템의 매커니즘에 영향을 주는 주요한 파라미터. ex)Hidden Layer 갯수, 학습률, 배치 사이즈, Dropout 등.
  - 개개 파라미터가 변경될 때마다 학습을 한다면 효율이 떨어진다. 그래서 일반적인 딥러닝에선 잘 쓰지 않는 기법.
  - Optuna : 파라미터 범위를 주고 그 범위 안에서 trials만큼 시행.

### Experiment Toolkits & Tips

- Tensorboard

  - 학습 과정과 로그를 기록하고 트래킹하기 좋은 툴. 파이토치에서도 사용 가능. 실시간과 이전 학습 모두 관찰 가능.

- wandb

  - 딥러닝 로그의 깃허브. 깃허브가 코드 저장이라면 wandb는 프로젝트별 로그 저장. 페이지에서 바로 로그 확인 가능.

- Jupyter Notebook

  - 코드를 아주 빠르게 Cell단위로 실행해볼 수 있는 것이 장점인 툴. 딥러닝을 처음 만난다면 이걸 하자. 데이터 로드를 매번 할 필요를 없기 때문에 EDA를 할 때 사용하면 매우 편리. 다만 학습 진행 도중 노트북 창이 꺼지면 이전으로 돌아갈 수 없다는 단점이 있음.

- PythonIDLE 

  - 구현은 한번만, 사용은 언제든, 간편한 코드 재사용에 적합한 툴. 디버깅 툴에 익숙해지면 활용도가 높다. 자유로운 실험 핸들링 가능.

- Tips

  - 분석 코드보다는 필자의 생각이 담긴 설명글을 유심히 보기.
  - 코드를 이해할 땐 디테일하게.
  - 공유를 주저 말라. 내 인사이트가 넓어지는 지름길.
  - 여유가 잇다면 최신 논문을 훑을 뿐 아니라 그 코드까지 관찰하기. 한 번에 이해하지 못해도 괜찮다.

### 통계와 차트 4-3강

- Seaborn 심화

  - 실습 코드로 학습 진행.

# ✏️ Doodle

- 또 한 주의 마무리. 한참 배울 땐 하루가 가는 것보다 쌓인다는 느낌이 든다. 오늘 하루도 쌓였는지는 미지수지만 분명한 건 저번 주의 나보단 더 자랐다는 것. 나이만 늘진 않았을 거야. 강의에선 모델 완성 후 성능을 높이기 위한 '굳히기'에 대해 말했다. 아직 내 코드는 굳히기는커녕 말랑한 상태로도 완성되지 않았지만, 다음 주에 대회가 마무리되기 때문에 좋은 성능을 내는 모델을 받아 학습을 진행하는 것이 맞겠다. 주인공은 가장 성능이 좋게 나온 팀원분의 모델이 될 것. 학습 템포가 조금 빠르다는 느낌이 드는데, 훌륭한 팀원 덕을 많이 보고 있다. 한 주 동안 더 밀도 높은 시간을 보내지 못했음에 반성. 매일을 마무리하는 그림은 그 주의 첫날에 미리 골라놓는데, 이번 주 그림은 어쩜 이리 내 상태에 꼭 맞는지 모르겠다. 잘 골랐네. 오늘의 끝은 틴토레토.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Tintoretto_1598_Penitent_Magdalene.jpg"></p>
<p align="center">Tintoretto, &ltPenitent Magdalene&gt, 1598-1602. Oil on canvas, 114.5x92cm.</p>

- Day 19 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day18/Note.md "Day18 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_2/Day20/Note.md "Day20 Note")
