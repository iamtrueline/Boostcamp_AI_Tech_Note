# 📙 Note

### 모델 불러오기

- model.save()

  - 학습의 결과를 저장하기 위한 함수. 모델 형태(architecture)와 파라미터를 저장한다.
  - 만들어진 모델을 외부 연구자와 공유하여 학습 재연성 향상.

- checkpoints

  - 학습의 중간 결과를 저장하여 최선의 결과를 선택.
  - earlystopping 기법 사용시 이전 학습의 결과물을 저장.
  - loss와 metric 값을 지속적으로 확인 저장.
  - 일반적으로 epoch, loss, metric을 함께 저장한다.
  - colab에서 지속적인 학습을 위해 필요.

- Transfer learning

  - 다른 데이터셋으로 만든 모델을 현재 데이터에 적용.
  - '일반적으로' 대용량 데이터셋으로 만들어진 모델의 성능이 높고 현재의 DL에서는 가장 일반적인 학습 기법.

- Freezing

  - pretrained model을 활용시 모델의 일부분을 고정.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img00.PNG" alt="pretrained model"></p>

---

### Monitoring tools for PyTorch

- Tensorboard

  - TensorFlow의 프로젝트로 만들어진 시각화 도구.
  - 학습 그래프, metric, 학습 결과의 시각화 지원.
  - PyTorch도 연결 가능 → DL 시각화 핵심 도구.
  - scalar : metric 등 상수 값의 연속(epoch)을 표시.
  - graph : 모델의 computational graph 표시.
  - histogram : weight 등 값의 분포를 표현.
  - Image : 예측값과 실제 값을 비교 표시.
  - mesh : 3d 형태의 데이터를 표현하는 도구.

- weight & biases

  - 머신러닝 실험을 원활히 지원하기 위한 상용도구.
  - 협업, code versioning, 실험 결과 기록 등 제공.
  - MLOps의 대표적인 툴로 저변 확대 중.

---

### 기본 차트의 사용 2-2 ~ 2-3강

- Line Plot

  - 연속적으로 변화하는 값을 순서대로 점으로 나타내고, 이를 선으로 연결한 그래프.
  - 꺾은선 그래프, 선 그래프, line chart, line graph 등의 이름으로 사용됨.
  - 시간/순서에 대한 변화에 적합하여 추세를 살피기 위해 사용. 시계열 분석에 특화.
  - .plot()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img01.PNG" alt="Line plot"></p>

-
  - 사용시 가독성을 위해 5개 이하의 선을 사용하자. 많으면 파악 난도가 올라감.
  - 시시각각 변동하는 데이터는 Noise로 인해 패턴 및 추세 파악이 어려우므로 smoothing사용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img02.PNG" alt="smoothing"></p>

- 정확한 Line Plot

  - 추세를 보기 위한 목적이므로 Bar plot과 다르게 꼭 축을 0에 초점을 둘 필요는 없다.
  - 너무 구체적인 line plot보다는 생략된 line plot을 사용하기. 디테일한 정보는 표로 제공.
  - 생략되지 않는 선에서 범위를 조정하여 변화율 관찰. (.set_ylim())
  - 규칙적인 간격의 데이터가 아니라면 각 관측 값에 점으로 표시하여 오해를 줄이자.
  - 보간 : 점과 점 사이에 데이터가 없기에 이를 잇는 방법. 데이터의 error나 noise가 포함되어 있는 경우, 데이터의 이해를 돕는 방법. 그러나 없는 데이터를 있다고 생각하게 할 수 있으며 작은 차이를 없앨 수 있으므로 일반적인 분석에서는 지양.
  - 이중 축 : 한 plot에 대해 2개의 축. 2개의 plot을 그리는 것이 이중 축 사용보다 낫다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img03.PNG" alt="이중 축"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img04.PNG" alt="이중 축->두 개 플롯"></p>

-
  - ETC : 라인 끝 단에 레이블을 추가하면 식별에 도움 (범례 대신). Min/Max 정보(또는 원하는 포인트)는 추가해주면 도움이 될 수 있음. (annatation) 보다 연한 색을 사용하여 uncertainty 표현 가능 (신뢰구간, 분산 등).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img05.PNG" alt="라인 끝 단에 레이블"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img06.PNG" alt="Min/Max 정보"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img07.PNG" alt="uncertainty 표현"></p>

- Scatter Plot

  - 점을 사용하여 두 feature간의 관계를 알기 위해 사용하는 그래프. 산점도. 점에서 다양한 variation 사용 가능(색, 모양, 크기).
  - 직교 좌표계에서 x축/y축에 feature 값을 매핑해서 사용.
  - .scatter()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img08.PNG" alt="Scatter Plot"></p>

-
  - Scatter plot의 목적 : 상관 관계 확인(양, 음, 없음), 군집, 값 사이 간극, 이상치 측정.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img09.PNG" alt="Scatter plot 관찰"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img10.PNG" alt="Scatter plot 관찰"></p>

- 정확한 Scatter Plot

  - 점이 많아질수록 점의 분포를 파악하기 힘들다 -> 투명도 조정, 지터링(jittering), 2차원 히스토그램, Contour plot (등고선)활용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img11.PNG" alt="Scatter plot 조정"></p>

-
  - 색 : 연속은 gradient, 이산은 개별 색상으로.
  - 마커 : 거의 구별하기 힘들다 + 크기가 고르지 않음.
  - 크기 : 버블 차트 (bubble chart). 관계보다는 각 점간 비율에 초점. SWOT 분석 등에 활용.
  - 인과 관계 (causal relation)과 상관 관계 (correlation)는 다르다. 인과 관계는 항상 사전 정보와 함께 가정으로 제시.
  - 추세선을 사용하면 scatter의 패턴을 유추할 수 있음. 단, 2개 이상이 되면 가독성이 떨어지므로 주의.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img12.PNG" alt="추세선"></p>

-
  - Grid는 지양. 사용한다면 최소한으로. 범주형이 포함된 관계에서는 heatmap 또는 bubble chart를 추천.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img13.PNG" alt="Grid&범주"></p>


# ✏️ Doodle

- 정리보다 과제가 선수. 그래서 내 입말이 부족하다. 과제는 일단 해결이 우선이라는 식으로 짜 놓아서 다시 한번 들춰야 할 것 같다. 문제는 다음주에 대회라는 거지. 오늘의 끝은 이미 지났지만, 그래도! 오늘의 끝은 프리다 칼로.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Frida_Kahlo_1951_Still_Life_with_Parrot_and_Flag.jpg"></p>
<p align="center">Frida Kahlo, &ltStill Life with Parrot and Flag&gt, 1951. Oil on masonite, 28x40cm.</p>

- Day 13 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day12/Note.md "Day12 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day14/Note.md "Day14 Note")
