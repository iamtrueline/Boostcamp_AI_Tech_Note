# 📙 Note

### Training & Inference 1

- Loss

  - 오차 역전파 -> Loss 함수 = Cost 함수 = Error 함수
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img00.PNG" alt="오차 역전파"></p>

-
  - 이전에 학습했던 역전파와 동일.
  - Loss율 계산에 따라 학습도 달라진다.
  - nn패키지 내 _Loss도 nn.Module Family = foward() 상속.
  - loss.backward() : 함수 실행 시 연결된 chain을 통해 모델 파라미터의 grad 값이 업데이트. 막고 싶다면 required_grad=false.
  - Focal Loss : ClassImbalance 문제가 있는 경우, 맞춘 확률이 높은 Class는 낮은 loss, 맞춘 확률이 낮은 Class는 높은 loss를 부여.
  - Label Smoothing Loss : Class targetlabel을 Onehot이 아닌 Smooth한 형태로 표현.

- Optimizer

  - 어느 방향으로 얼마나 빨리 움직일까?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img01.PNG" alt="학습률"></p>

-
  - LR(Learning Rate) scheduler : 학습률을 동적으로 조절하는 장치. 학습률이 고정되면 완벽한 학습과 거리가 있을 수 있다. 학습 시에 학습률을 동적으로 조절하면 더 정확히 수렴할 것.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img02.PNG" alt="학습률 변동가부에 따른 예시 그래프"></p>

-
  - StepLR : 가장 만들기 쉬운 LR scheduler. 특정 Step마다 학습률이 감소.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img03.PNG" alt="StepLR"></p>

-
  - CosineAnnealingLR : Cosine 함수 형태처럼 LR을 급격히 변경.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img04.PNG" alt="CosineAnnealingLR"></p>

-
  - ReduceLROnPlateau : 가장 일반적으로 쓰이는 scheduler. 더 이상 성능 향상이 없을 때 LR 감소.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img05.PNG" alt="ReduceLROnPlateau"></p>

- Metric

  - 학습에 직접적으로 사용되는 것은 아니지만 학습된 모델을 객관적으로 평가할 수 있는 지표가 필요. Classification, Regression, Ranking 등.
  - Classification : Accuracy, F1-score, precision, recall, ROC&AUC
  - Regression : MAE, MSE
  - Ranking : MRR, NDCG, MAP
  - 현업에서는 Metric이 미리 설정되어있지 않다. 그러므로 데이터 상태에 따라 적절한 Metric을 선택하는 것이 필요. ex) Class 별로 밸런스가 적절히 분포? -> Accuracy, Class별 밸런스가 좋지 않아서 각 클래스 별로 성능을 잘 낼 수 있는지 확인 필요? -> F1-Score 등.

---

### Training & Inference 2

- Training

  - 트레이닝을 위해 필요한 준비물.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img06.PNG" alt="트레이닝을 위해 필요한 준비물"></p>

-
  - 트레이닝 프로세스는?
  - model.train() -> optimzer.zero_grad() -> loss=criterion(outputs,labels) -> loss를 마지막으로 chain생성 -> loss의 grad_fn chain→ loss.backward() -> optimizer.step()

- Inference

  - Inference 프로세스는?
  - model.eval() -> withtorch.no_grad()
  - 추론 과정에 Validation set가 들어간다면 검증 과정.
  - 모든 절차가 끝나면 Submission 스펙에 맞추어 파일 변환 후 제출.

- Pytorch Lightning

  - 생산성을 위한 패키지.
  - 위에서 거친 단계를 하나의 정의와 일반적인 데이터로 끝낸다.
  - 배우는 단계를 지나 프로세스를 쉽고 빠르게 이해할 수 있다면 사용하기.

# ✏️ Doodle

- 팀원 코드 리뷰를 통해 성능이 잘 나오는 모델, 혹은 잘 나오기 위해 여러 시도를 한 모델을 본 날. 여기서 가장 많이 배운 건 코드 공유가 스스럼없다는 점이다. 내 코드는 나 혼자 볼 땐 소중하지만 다른 사람들 앞엔 데리고 나오기 싫은데. 열의 넘치는 좋은 사람들 사이에선 확실히 더 많이 배울 수밖에 없다. 내가 그걸 잘 담을 수 있는 그릇이 되길 바람. Resnet50 모델을 가져와 돌려보았고, 결과는 나왔지만 데이터 처리가 엉망이었는지 성능은 낮다. 심지어 제출 파일 처리를 잘못해서 submit fail도 여러 번 떴다. 나이 예측률이 가장 낮은데, 이건 내 눈으로 봐도 어려우니 봐준다. 그래도 머리가 없다고 무조건 아기라고 단정 짓는 건 너무 게으르다. 모델뿐 아니라 데이터도 그대로 끌어오는 게 좋을까? 오늘부터 대회에 팀으로 병합되어서 제출 횟수 제한이 더 적어진다. 마음대로 낼 수 없을 것이기 때문에 로컬에서 정확도를 측정하고 있다. 학습 정확도가 높게 나와도 시험 결과는 20~30% 언저리에 머무르고 있다. 아마 실제 제출 시엔 오차 때문에 더 낮은 기록을 할 것. 왜지? 아직은 모르겠다. 이젠 꿈에서도 모델을 돌리고 있다. 잠시 쉬고, 마시고, 자자. 오늘의 끝은 카라바조.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Caravaggio_Merisi_1595_The_adolescent_Bacchus.jpg"></p>
<p align="center">Caravaggio Merisi, &ltThe adolescent Bacchus&gt, 1595-1597. Oil on canvas, 95x85cm.</p>

- Day 18 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day17/Note.md "Day17 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day19/Note.md "Day19 Note")
