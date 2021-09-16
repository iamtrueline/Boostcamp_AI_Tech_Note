# 📙 Note

### Model 1

- Pytorch에서 모델 부르기

  - 모델 : object나 system 정보의 표현.
  - Why Pythorch? Low-level,Pythonic, Flexibility. 유연하게 응용이 쉽다. 그리고 오픈소스 풍년.
  - Pytorch 모델의 모든 레이어는 nn.Module 클래스를 따른다.
  - modules : __init__에서 정의한 또 다른 nn.Modules.
  - nn.Module을 상속받은 모든 클래스의 공통된 특징 : forward()->모델(모듈)이 호출 되었을 때 실행 되는 함수. 모델의 forward()를 한번만 실행한 것으로 그 모델의 forward에 정의된 모듈 각각의 forward()가 실행.
  - 파라미터 : 모델에 정의되어 있는 modules이 가지고 있는 계산에 쓰일 Parameter. 각 모델 파라미터 들은 data, grad, requires_grad 변수 등을 가지고 있다.
  - Pythorch의 특징(Pythonic)을 잘 알고 있다면 응용과 에러 핸들링이 쉽다.

---

### Model 2

- Pretrained Model

  - 세상은 넓고 컴퓨터 비전은 충분히 똑똑해졌다.
  - 획기적인 알고리즘 개발과, 검증을 위해 높은 품질의 데이터 셋은 필수적.
  - ImageNet(대용량 데이터셋)이 만들어 진후 트레이닝 모델의 성능도 빠르게 상승. 데이터가 많으면 배울 것도 많다 = 똑똑해지는 모델.
  - 모델 일반화를 위해 매번 수 많은 이미지를 학습시키는 것은 까다롭고 비효율적. 그렇다면 이 어느정도 충분히 '똑똑해진' 모델을 쓰면 어떨까?
  - 좋은 품질, 대용량의 데이터로 미리 학습한 모델 -> 이 모델을 바탕으로 내 목적에 맞게 다듬어서 사용.
  - torchvision.models로 목적에 맞는 모델 다운 가능.

- Transfer Learning

  - CNNbase모델 구조 : Input+CNNBackbone+Classifier→Output
  - 내 데이터, 모델과 이미 존재하는 Pretraining 모델의 유사성을 비교 분석하여 모델 선택 및 응용 -> 우리 모델과 목적 및 학습 데이터가 얼마나 유사할까?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day17_img00.PNG" alt="비교 example"></p>

-
  - 학습 데이터가 충분한 경우 : 유사성이 높다면(ex.클래스만 다른 경우) Backbone 업데이트는 필요 없다. 유사성이 낮더라도 기존 Backbone을 가지고 같이 학습하는 경우 성능이 좋다는 것이 실험으로 증명됨.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day17_img01.PNG" alt="학습 데이터가 충분한 case"></p>

-
  - 학습 데이터가 충분하지 않은 경우 : 유사성이 높다면 마찬가지로 Backbone을 건드리지 않고 트레이닝이 가능. 유사성이 낮다면 이용 어려움. 납득 안되는 결과가 나올 확률이 높다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day17_img02.PNG" alt="학습 데이터가 충분하지 않은 case"></p>

---

### 통계와 차트 4-1강

- Seaborn 기초

  - 기본적인 분류 : Categorical API, Distribution API, Relational API, Regression API, Matrix API.
  - 실습 코드로 학습 진행.

# ✏️ Doodle

- 온종일 붙들고 모델 학습 코드를 짰는데 에러만 뱉어서 사용할 수 없다. 코드에 양심이 있다면 내가 들인 시간만큼의 성의는 보여주겠지? 안타깝게도 코드는 양심이 없다. 이 와중에 대회 제출이 필수로 바뀌어서 기본 제공되는 베이스로 돌린 값을 올렸다. 모르는 사람들이 올린 좋은 기록들엔 큰 감흥이 없지만, 얼굴을 아는 팀원들이 올리는 기록엔 눈이 간다. 내가 완성은 할 수 있을까? 회의록(會議錄)이 아니라 회의록(懷疑錄)을 적어야 할 것 같은데. 시간 분배를 잘못해서 강의는 저녁에 몰아 들었다. 강의를 듣고 뒤늦게나마 이미 있는 좋은 모델을 활용해보려고 한다. 안되는 걸 붙들고 있기엔 시간이 너무 짧다. 자, 꼭 복기하고 자기. 오늘의 끝은 칸딘스키.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Wassily_Kandinsky_1913_Composition_7.jpg"></p>
<p align="center">Wassily Kandinsky, &ltComposition 7&gt, 1913. Oil on canvas, 200.6x302.2cm.</p>

- Day 17 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day16/Note.md "Day16 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day18/Note.md "Day18 Note")
