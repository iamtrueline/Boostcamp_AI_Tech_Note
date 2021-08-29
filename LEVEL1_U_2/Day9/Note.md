# 📙 Note

### Modern CNN - 1x1 convolution의 중요성

- ILSVRC

  - ImageNet Large-Scale Visual Recogmnition Challenge
  - Classification / Detection / Localization / Segmentation
  - 백만 개가 넘는 이미지, 천여 개의 다른 카테고리, 트레이닝 세트 : 456,567개 이미지.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img00.PNG" alt="연도별 Error Rate"></p>

- AlexNet (2011년도 우승)

  - 처음 활용 당시에 GPU가 부족, 최대한 많은 파라미터를 넣고 싶어서 네트워크를 두개로 나눔.
  - 5 Convolutional layers, 3 Dense layers
  - Rectified Linear Unit(ReLU) activation : Preserves properties of linear models(0 밑으로 0, 이상으론 상승) / Easy to optimize with gradient descent / Good generalization / Overcome the vanishing gradient problem
  - GPIimp lementation (2GPUs)
  - Local response normalization, Overlapping pooling
  - Data augmentation
  - Dropout (몇 개 뉴런을 0으로)
  - 현재 기준으론 당연한 적용들이나, 2011년도 기준으론 획기적.
  - 8-layers, 60M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img01.PNG" alt="AlexNet 구조"></p>

- VGGNet (2014년도 준우승)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img02.PNG" alt="VGGNet 구조"></p>

-
  - 3*3 convolution filter만 사용. 왜? 3*3을 두번 하는 것(18)과 5*5를 한번 하는것(25)는 Receptive field 측면에선 똑같지만 계산량이 약 1.5배 차이 남(3*3이 계산적 유리).
  - 이후 다른 것들도 비슷한 이유로 7*7을 벗어나지 않음. 1은 노의미. 3 적절. 5와 7도 사용 가능. 짝수는 왜 안쓰나요? -> Anti-Aliasing.
  - 19-layers, 110M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img03.PNG" alt="3*3 convolution vs 5*5 convolution 구조"></p>

- GoogLeNet (2014년도 우승)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img04.PNG" alt="GoogLeNet 구조"></p>

-
  - Inception blocks : Convolution filter 전에 1*1 필터를 거침. 파라미터를 줄이는 역할. 이는 채널 방향으로 차원을 줄이는 역할을 한다.
  - 1*1 필터의 이점 : 파라미터가 약 30% 줄어든다.
  - 22-layers, 4M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img05.PNG" alt="필터 구조"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img06.PNG" alt="1*1 필터 계산 비교"></p>

- ResNet (2015년도 우승, 최초로 사람의 성능을 넘음)

  - 트레이닝 에러가 작음에도 불구하고 실제 테스트 에러가 그만큼 줄어들지 않음(not Overfitting). = 네트워크가 커짐에 따라 학습이 불가능. 그래서 Identity map(skip connection)을 적용.
  - Identity map : x값의 차이만 학습. 이를 이용하면 18-layer의 성능이 34-layer보다 나았던 문제를 해결 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img07.PNG" alt="Identity map"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img08.PNG" alt="18 and 34-layer 비교"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img09.PNG" alt="적용 방법"></p>

- DenseNet

  - 값을 더하지 말고 concatenation하자.
  - 이 때, 채널이 무한정 늘어나게 됨. 그래서 중간에 한 번 씩 1*1 convolution으로 줄여버리기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img10.PNG" alt="ResNet, DenseNet 비교"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img11.PNG" alt="DenseNet 구조"></p>

- Summary
  - VGG : repeated 3*3 blocks
  - GoogLeNet : 1*1 convolution
  - ResNet : skip-connection
  - DenseNet : concatenation

### Computer Vision Applications

- Semantic Segmentation

  - 각 이미지를 픽셀별로 분류 & 라벨링.
  - 자율주행 등에 활용.

- FCN(Fully Convolutional Network)

  - 기본 CNN에서 dense layer를 없애고 convolution으로 대체하기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img12.PNG" alt="ordinary CNN"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img13.PNG" alt="fully convolutional network"></p>

-
  - 결국 파라미터 수는 같다. 이 절차명은 Convolutionalization.
  - Why? fully convolution : input image 사이즈에 상관없이 적용 가능.
  - 줄어든 output을 다시 늘리는 방법 : Deconvolution(conv transpose). 실제로 역은 아니다. 낮은 화질을 높은 화질로 복구할 수 없듯이(복구라는 이름의 추측 및 생성은 가능한 것).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img14.PNG" alt="Deconvolution"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img15.PNG" alt="Deconvolution"></p>

- Detection

  - 이미지 안에서 Region을 추출(찾기). 어느 물체가 어디에 있나요?

- R-CNN

  - Input image -> 2,000개의 region을 찾기 -> 모두 같은 크기로 맞추기. -> 분류 with linear SVMs.
  - 단순. 비교적 부정확.

- SPPNet

  - R-CNN은 2,000개를 다 돌린다. 힘드니까 CNN은 한 번만 돌리자 = SPPNet.
  - 바운딩을 구한 이미지 전체에 대한 convolutional feature map을 한 번 만들고, 바운드에 해당하는 feature만 가져오는 것.

- Fast R-CNN

  - 바운딩을 구한 이미지 전체에 대한 convolutional feature map을 한 번 만들고, ROI pooling을 통해 feature를 뽑은 후 class와 bounding-box regressor를 추출.
  - SPPNet과 차이 : 마지막에 뉴럴 네트워크를 사용했다는 점(ROI pooling).

- Faster R-CNN

  - RPN(Region Proposal Network) + Fast R-CNN
  - RPN : 이미지 내 특정 영역에 물체가 있는지 없는지 판단. anchor box = 미리 예측된 사이즈.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img16.PNG" alt="RPN 바운딩 판단"></p>

- YOLO (v1)

  - Faster R-CNN보다 훨씬 빠른 물체 인식 알고리즘.
  - 이미지 한 장에서 바로 아웃풋. 바운딩 박스 분류 과정 생략.
  - Input image -> divide SxS grid. (물체가 grid 안에 들어가면 detection도 함께) -> B개(ex. 5)의 바운딩 박스 예측. 및 실제 물체가 있는지 판단 + 물체 class(C) 예측 -> tensor = SxS(B^5+C) size.
  - 바운딩 박스 찾기와 클래스 예측이 함께 이루어져서 속도 향상.

### Sequential Models - RNN(Recurrent Neural Networks)

- Sequential Model

  - 일상 속 대부분의 데이터가 시퀀셜 데이터.
  - 처리의 어려움 : 원하는 정보는 특정 라벨 하나일 경우가 많은데, 그를 위해 얼마나 많은 길이의 데이터가 필요한지 쉽게 알 수 없음. 따라서, 인풋 길이에 상관없이 동작하는 모델이 필요.
  - 가장 간단한 처리는 정해진 구간의 과거 정보만 참고하는 것. (ex. 다음 단어 예측에 바로 직전 2개 단어만 사용)
  - Markov model : 나의 현재는 바로 직전의 과거에만 dependent라는 가정.
  - Latent autoregressive model : 바로 직전이 아닌 전체 과거의 정보를 요약한 히든 state를 사용.

- RNN

  - 입력과 출력을 시퀀스 단위로 처리하는 모델. 은닉층(히든 state)의 노드에서 활성화 함수를 통해 나온 결과값을 출력층 방향으로도 보내면서, 다시 은닉층 노드의 다음 계산의 입력으로 보낸다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img17.PNG" alt="RNN 구조"></p>

-
  - 다만, 이 경우 Short-term dependencies라는 단점이 존재. 먼 과거의 정보 고려가 어려움. 멀리 있는 과거라고 가치가 적은 것은 아니므로 이를 보완하는 일이 중요하다.
  - 가중치는 과거의 정보를 계속해서 쌓으며 곱. 활성함수가 Sigmoid일 경우, 갈수록 가중치가 계속 줄어들어 의미가 사라진다. 반대로 ReLU라면, 갈수록 가중치가 급속으로 커져 학습이 불가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img18.PNG" alt="RNN 식"></p>

- LSTM(Long Short Term Memory)

 - 기존 RNN과 LSTM 비교.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img19.PNG" alt="RNN 구조 요약"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img20.PNG" alt="LSTM 구조 요약"></p>

-
  - LSTM 상세
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img21.PNG" alt="LSTM 상세 구조"></p>

-
  - Forget Gate : 어떤 정보를 버릴까?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img22.PNG" alt="Forget Gate"></p>

-
  - Input Gate : 현재 들어온 정보 중 어떤 정보를 저장할까?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img23.PNG" alt="Input Gate"></p>

-
  - Update cell : 처리된 정보를 업데이트.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img24.PNG" alt="Update cell"></p>

-
  - Output Gate : 현재 결과를 아웃풋, 다음 히든스테이트로 활용.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img25.PNG" alt="Output Gate"></p>

- GRU(Gated Recurrent Unit)

  - Gate가 두 개. reset and update.
  - cell state가 없다. 오직 hidden state 뿐. hidden state가 곧 output.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img26.PNG" alt="GRU 구조"></p>

-
  - 일반적으로 LSTM보다 GRU 성능이 좋은 것을 볼 수 있음.

# ✏️ Doodle

- 어제에 이은 깃허브 강의. 유용하고 오래 걸린다. 어제치 분량과 더불어 오늘 강의 난이도가 있어서 완벽한 소화가 어렵다. 짧은 시간에 최대한 간결하고 정확한 정보 전달을 해주시려는 건 느껴진다. 그렇지만 내 쪽이 우등생이 아니라서 길어도 좋으니 더 정확한 설명이 필요. 구현과 함께 보고 싶은데 과제와는 약간 거리가 있는 게 아쉽다. 직접 코드를 찾아보는 게 답. 오늘의 끝은 마티스.

<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Henri_Matisse_1910_Dance.jpg"></p>
<p align="center">Henri Matisse, &ltDance&gt, 1910. Oil on canvas, 260x391cm.</p>

- Day 9 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day8/Note.md "Day8 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day10/Note.md "Day10 Note")
