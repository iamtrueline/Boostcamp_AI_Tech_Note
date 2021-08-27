# 📙 Note

### Dataset

- Pre-processing

  - 주어진 바닐라 데이터를 모델이 학습할 수 있는 형태로 만들기.
  - 보통 경진대회용 데이터는 품질이 좋다. 대회 효율 != 실제 효율.
  - Bounding box : 필요 이상의 정보라면 감하자.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img00.PNG" alt="Bounding box"></p>

-
  - Resize : 효율적인 계산을 위해 사이즈 변경.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img01.PNG" alt="Resize"></p>

-
  - 전처리는 데이터 형식과 목적에 따라 여러 형태가 존재. 고민과 연구가 답.

- Generalization

  - Bias & Variance : 학습이 너무 안되면 문제. 너무 맞춤이어도 문제. -> ealry stopping이 이럴 때 쓰인다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img02.PNG" alt="Bias & Variance"></p>

-
  - Train / Validation : 훈련 셋 중 일부를 검증 셋으로 활용하기(cf.K-fold). 테스트 셋은 건드리지 않는다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img03.PNG" alt="Train / Validation"></p>

-
  - Data Augmentation : 주어진 데이터의 케이스 다양화. 밤과 낮, 각도, 주변 환경 등을 반영한 데이터. 문제가 만들어진 배경과 모델을 분석하여 도출하기. 범주내에서 최대한 다양하게, 돌리기, 자르기, 왜곡, 화밸 등.
  - torchvision.transforms : 유용.
  - 모든 과제와 모든 데이터에 무조건 통하는 양약은 없다.

### Data Generation

- Data Feeding

  - 모델에 적합한 dataset을 알맞게 넣기. -> 효율 증대.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img04.PNG" alt="Data Feeding"></p>

- Dataset & DataLoader

  - Dataset : VanillaData를 Dataset으로 변환.
  - DataLoader : Dataset을 효율적으로 사용할 수 있도록 관련 기능 추가. 배치 사이즈, num workers, 채널 등.
  - Dataset과 DataLoader는 분리되는 것이 좋다. 재활용(사용)성을 높이기 위해. Dataset는 Vanilla데이터를 원하는 형태로 출력해주는 클래스. DataLoader는 Dataset의 효율을 올리는 게 목적인 유틸.

### 통계와 차트 4-1강

- Seaborn 소개

  - Seaborn : Matplotlib 기반 통계 시각화 라이브러리. Matplotlib 기반이라 Matplotlib으로 커스텀 가능하며, 쉬운 문법과 깔끔한 디자인이 특징.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img05.PNG" alt="Seaborn example"></p>

-
  - 불러올 땐 으레 sns로(import seaborn as sns).
  - 시각화의 목적과 방법에 따라 API를 분류하여 제공 -> Categorical API, Distribution API, Relational API, Regression API, Multiples API, Theme API 등.

# ✏️ Doodle

- 강의는 간단, 실습은 노간단. 기본적으로 들어본 내용들이지만 새로 구성하는 건 또 다른 일이라는 게 와닿는다. 대회용으로 주어진 데이터가 정갈하다고 생각했는데(물론 비교적 정갈하지만) 생각보다 노이즈가 많다. 분석은 재밌어도 내 코드가 오류만 뱉으면 슬프지. 사실 얘는 언제나 그랬어. 캡스톤을 다시 하는 마음으로 진행하기. 팀원들이 모두 앞서 나가서 정말 다급하고 도움된다. 스페셜 미션의 베이스 코드가 열렸는데, 난 EDA 봉투를 뜯고 냄새만 맡은 격이었다. 시간은 쏟았는데 형태로 남은 게 별로 없는 하루. 그림 그리러 가고 싶다. 오늘의 끝은 세잔.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Paul_Cezanne_1905_Still_Life_with_Apples_and_Peaches.jpg"></p>
<p align="center">Paul Cezanne, &ltStill Life with Apples and Peaches&gt, 1905. Oil on canvas, 81x100.5cm.</p>

- Day 16 마침.
