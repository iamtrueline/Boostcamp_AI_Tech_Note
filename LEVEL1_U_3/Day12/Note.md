# 📙 Note

### AutoGrad & Optimizer

- Module

  - torch.nn.Module : 딥러닝을 구성하는 Layer의 base class, Input, Output, Forward, Backward 정의, 학습의 대상이 되는 parameter(tensor) 정의.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day12_img00.PNG" alt="Forwardpass and Backwardpass"></p>

- Parameter

  - nn.Parameter : Tensor 객체의 상속 객체, nn.Module 내에 attribute가 될 때는 required_grad=True로 지정되어 학습 대상이 되는 Tensor(AutoGrad).
  - 우리가 직접 지정할 일은 잘 없고 대부분의 layer에는 weights 값들이 지정되어 있다. 웬만하면 텐서로.

- Backward

  - Layer에 있는 Parameter들의 미분을 수행.
  - Forward의 결과값 (model의 output=예측치)과 실제값 간의 차이(loss) 에 대해 미분을 수행하고 해당 값으로 파라미터 업데이트.
  - Backward from the scratch : 실제 backward는 Module 단계에서 직접 지정 가능. Module에서 backward와 optimize 오버라이딩, 사용자가 직접 미분 수식을 써야 하는 부담(쓸 일은 없으나 순서는 이해해야한다). 보통 레이어가 많으니까.

### Dataset & Dataloader

- 모델에 데이터를 넣기
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day12_img01.PNG" alt="Data -> Model"></p>

- Dataset

  - 데이터 입력 형태를 정의하는 클래스. 데이터를 입력하는 방식의 표준화.
  - Image, Text, Audio 등에 따라 함수 입력 정의가 다르다.
  - 모든 것을 데이터 생성 시점에 처리할 필요는 없다. 예를 들어 image의 Tensor 변화는 학습에 필요한 시점에 변환.
  - 데이터 셋에 대한 표준화된 처리방법이 제공되어야 지속 사용이 용이하다.
  - 표준화된 라이브러리 : HuggingFace 등.

- DataLoader

  - Data의 Batch를 생성해주는 클래스.
  - 학습직전(GPU feed전) 데이터의 변환을 책임.
  - Tensor로 변환 + Batch 처리가 메인 업무.

# ✏️ Doodle

- 과제 해결이 오래 걸린다. 깨달은 점은, 나 파이썬 모르네? 파이토치 문서량에 압도돼서 하나하나 찾아볼 순 없지만, 필수 과제만큼은 소화해야 하는데. 오늘 본 강의에 충실하지 않아서 나중에 다시 한번 정리해야 한다. 코드 중심 강의여서 따로 적어놓는 게 나을 듯. 오늘의 끝은 요하네스 페르메이르.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Johannes_Vermeer_1665_Girl_with_a_Pearl_Earring.jpg"></p>
<p align="center">	Johannes Vermeer, &ltGirl with a Pearl Earring&gt, 1665. Oil on canvas, 44.5x39cm.</p>

- Day 12 마침.
