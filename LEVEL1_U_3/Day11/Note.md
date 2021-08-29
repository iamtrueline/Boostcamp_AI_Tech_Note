# 📙 Note

### Introduction to PyTorch

- 프레임워크

  - 이제 구현을 0부터 시작할 필요는 없다.
  - 자료도 많고 관리도 잘 되고 사실상 표준으로 쓰는 많은 프레임워크들 like 텐서플로, 파이토치.
  - PyTorch : Dynamic Computation Graph
  - TensorFlow : Define and run
  - Computational Graph : 연산의 과정을 그래프로 표현한 것. 텐서플로는 그래프를 먼저 정의하고 실행 시점에 feed, 파이토치는 실행을 하면서 그래프를 생성.
  - 파이토치의 강점 : Define by Run = 즉시 확인 가능->pythonic code. GPU support, Good API and community, 사용 용이. Numpy + AutoGrad + Function. Numpy 구조를 가지는 Tensor 객체로 어레이 표현. 자동 미분 지원, DL 연산 지원, 다양한 형태의 DL을 지원하는 함수와 모델 지원.

### PyTorch Basics

- PyTorch?

  - numpy + AutoGrad
  - Tensor : 다차원 어레이를 표현하는 PyTorch 클래스. 사실상 numpy의 ndarray와 동일(TF의 Tensor와도 동일). 생성 함수도 거의 동일. list나 ndarry 사용 가능. 기본적으로 가질 수 있는 데이터 타입이 numpy와 동일하며 사용법도 그대로 적용됨.
  - 파이토치의 Tensor는 GPU에 올려서 사용 가능.
  - view : reshape처럼 tensor의 shape을 변환.
  - squeeze : 차원의 개수가 1인 차원을 삭제 (압축)
  - unsqueeze : 차원의 개수가 1인 차원을 추가.
  - 기본적인 연산은 numpy와 동일.
  - mm은 자동 broadcastion no, matmul은 yes.
  - nn.functional 모듈을 통해 다양한 수식 변환 지원.
  - 자동 미분 지원. backward()

### PyTorch 프로젝트 구조 이해하기

- Overview

  - 초기 단계에서는 대화식 개발 과정이 유리. 학습과정과 디버깅 등 지속적인 확인이 필요.
  - 배포 및 공유 단계에서는 노트북 공유가 어려움. 쉬운 재현이 어렵고 실행 순서가 꼬임.
  - DL 코드도 하나의 프로그램으로, 개발 용이성 확보와 유지보수 향상 필요.
  - 주피터로는 유지보수 향상에 한계가 있음.
  - 다양한 프로젝트 템플릿이 있으므로 사용자 필요에 따라 수정하여 사용.

### 기본 차트의 사용 2-1강

- Bar Plot

  - 직사각형 막대를 사용하여 데이터의 값을 표현하는 차트/그래프. = 막대 그래프, bar chart, bar graph.
  - 범주(category)에 따른 수치 값을 비교하기에 적합한 방법. 개별 비교와 그룹 비교 모두에 적합하다.
  - .bar() = 수직, .barh() = 수평. 수직(vertical)은 x축에 범주, y축에 값을 표기하고 수평(horizontal)은 y축에 범주, x축에 값을 표기한다. 전자가 디폴트, 후자는 범주가 많을 때 적합.
  - 그룹이 5개~7개 이하일 때 효과적이며, 그룹이 이보다 많다면 비중이 작은 그룹은 ETC 처리.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img00.PNG" alt="Bar Plot"></p>

-
  - Bar Plot에서는 범주에 대해 각 값을 표현 -> 즉 1개의 feature에 대해서만 보여주므로 여러 그룹을 보여주기 위해서는 여러가지 방법이 필요. 이에, 플롯을 여러개 그리거나 한 개의 플롯에 동시에 나타내는 방법등을 쓸 수 있다.

- Multiple Bar Plot

  - 플롯을 여러 개 그리기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img01.PNG" alt="Multiple Bar Plot"></p>

- Stacked Bar Plot

  - 2개 이상의 그룹을 쌓아서(stack) 표현. 맨 밑의 bar 파악은 쉽지만 그 외는 어렵다.
  - .bar()에서는 bottom 파라미터를 사용, barh()에서는 left 파라미터를 사용.
  - 응용하여 전체에서 비율을 나타내는 Percentage Stacked Bar Chart가 있음.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img02.PNG" alt="Stacked Bar Plot"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img03.PNG" alt="Overlapped Bar Plot"></p>

- Grouped Bar Plot

  - 그룹별 범주에 따른 bar를 이웃되게 배치하는 방법. 
  - Matplotlib으로는 비교적 구현이 까다로우나, 방법은 .set_xticks(), .set_xticklabels()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img04.PNG" alt="Grouped Bar Plot"></p>

- 정확한 Bar Plot

  - Principle of Proportion Ink : 실제 값과 그에 표현되는 그래픽으로 표현되는 잉크양은 비례. 이는 대부분 시각화에서 적용되는 룰.
  - 반드시 x축의 시작은 0(zero).
  - 더 정확한 정보를 전달하기 위해서는 정렬이 필수. 데이터 종류에 따라, 시계열 = 시간순, 수치형 = 크기순, 순서형 = 범주순서, 명목형 = 범주의 값으로 정렬.
  - 여백과 공간 조절 등으로 가독성 높이기.
  - 정확하고 단순하게. 무의미한 3D는 필요 없다. 직사각형이 아닌 다른 형태의 bar는 지양.
  - 오차 막대를 추가하여 Uncertainty 정보를 추가 가능.
  - Bar 사이 Gap이 0이라면 -> 히스토그램(Histogram).
  - Text 정보(제목, 라벨)를 다양하게 활용하기.

### Generative Models 2

- Variational Auto-encoder(VAE)

  - Variational inference(변분추론)의 목적은 Posterior distribution(사후분포)를 찾는 것.
  - 그러나 일반적으로는 Posterior distribution(p(z|x))을 구하기 어려움. 그래서 최대한 근사한 값, Variational distribution(q(x))을 쓴다. 
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img05.PNG" alt="Variational inference"></p>

-
  - 문제는, 모르는 값을 근사할 수 있는가? So, ELBO(Evidence Lower BOund)를 계산.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img06.PNG" alt="ELBO"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img07.PNG" alt="ELBO"></p>

-
  - Reconstruction Term : 이상적인 샘플링 함수로부터 얼마나 잘 복원을 했는가?
  - Regularlization Term : 이상적인 샘플링 함수가 최대한 prior와 같도록 만들기. 여러 샘플 중에서 prior와 유사한 값을 샘플링하도록 조건 부여.
  - Key limitation : intractable 모델. 얼마나 근사한지 알기 힘듦. KL divergence가 미분 가능해야하므로 보통 모든 아웃풋이 independent한 isotropic Gaussian을 사용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img08.PNG" alt="KL divergence"></p>

- Adversarial Auto-encoder(AAE)

  - 가우시안을 활용하고싶지 않으면? latent distribution을 맞추기 위해 GAN을 활용하는 AAE사용.
  - 성능도 일반적으로 VAE보다 낫다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img09.PNG" alt="KL divergence"></p>

- GAN

  - 흐름은? 한쪽(discriminator)은 최대로, 한쪽(generator)은 최저로 낮추기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img10.PNG" alt="GAN"></p>

-
  - GAN과 VAE 차이
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img11.PNG" alt="GAN and VAE"></p>

- GAN 관련 논문들 참조

  - DCGAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img12.PNG" alt="DCGAN"></p>

-
  - Info-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img13.PNG" alt="Info-GAN"></p>

-
  - Text2Image
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img14.PNG" alt="Text2Image"></p>

-
  - Puzzle-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img15.PNG" alt="Puzzle-GAN"></p>

-
  - CycleGAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img16.PNG" alt="CycleGAN"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img17.PNG" alt="CycleGAN"></p>

-
  - Star-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img18.PNG" alt="Star-GAN"></p>

-
  - Progressive-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img19.PNG" alt="Progressive-GAN"></p>

# ✏️ Doodle

- 긴 휴일 끝. 긴 논문 안 끝. 뒤돌면 잊는데 복습을 하지 않는 건 말도 안 된다. 그리고 난 어불성설의 아이콘이지. 지난주에 이해가 낮아 전부 기록하지 못했던 Generative Model을 다시 기록하고, 새 과제를 시작했다. 왜 파이토치를 배우는 순서가 뒤였는지 의아했는데 난이도를 보니 이해된다. 말투가 친절해서 내용도 친절할 거라 생각했는데 아니었어. 사람이든 과제든 겉모습만 보고 판단하지 말라는 멘토들의 교훈이라고 생각한다. 오늘의 끝은 렘브란트.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Rembrandt_1642_The_Night_Watch.jpg"></p>
<p align="center">	Rembrandt van Rijn, &ltThe Night Watch&gt, 1642. Oil on canvas, 363x437cm.</p>

- Day 11 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day10/Note.md "Day10 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day12/Note.md "Day12 Note")
