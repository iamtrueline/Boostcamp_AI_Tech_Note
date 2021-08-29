# 📙 Note

### Convolution은 무엇인가?

- CNN(Convolution Neural Networks)

  - Continuous convolution
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img00.PNG" alt=""></p>

-
  - Discrete convolution
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img01.PNG" alt=""></p>

-
  - 2D image convolution
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img02.PNG" alt=""></p>

-
  - 필터를 이미지에 적용하면 크기는 이미지 - 필터 + 1(Stride 1, None Padding 조건 있음). 이 때, 필터는 Stack-Up 하여 최종 결과의 크기를 쌓을 수도 있다. (ex. 32*32*3 이미지를 5*5*3필터 적용 후 28*28*4 로 출력 = 필터는 4개)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img03.PNG" alt="필터 적용 예시"></p>

-
  - CNN은 Convolution layer, pooling layer, fully connected layer의 조합.
  - Convolution, pooling layer : feature extraction
  - Fully connected layer : decision making (분류 등)
  - Stride : 얼마나 촘촘하게 필터(커널)를 찍을거야? 기본 : 1. 만약 2라면 이미지를 두 칸씩 떼서 찍는다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img04.PNG" alt="Stride"></p>

-
  - Padding : 덧대는 값. 가에 있는 값까지 포함해서 찍으면 아웃풋의 차원도 똑같아진다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img05.PNG" alt="Padding"></p>

- 1*1 Convolution

  - 차원 축소.
  - 깊이는 깊게, 파라미터는 줄이기.
  - CNN의 뒷 단, Fully convolution시 차원이 높으면 비용이 너무 높게 산출됨. 차원 축소는 비용을 줄이고 성능을 높이는 방법.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img06.PNG" alt="CNN 전체"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img07.PNG" alt="Convolution"></p>

# ✏️ Doodle

- 내용이 아주 깊진 않지만 완벽하게 소화하려면 시간이 필요하다. 많이 들어봤던 연사, 이고잉님의 깃허브 강의도 함께 있던 날. 충분한 소화를 했는지 모르지만 노력해야지. 몸이 너무 안 좋아 노트 기록은 잠시 축소. 내일 힘내. 오늘의 끝은 보티첼리.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Sandro_Botticelli_1484_The_Birth_of_Venus.jpg"></p>
<p align="center">Sandro Botticelli, &ltThe Birth of Venus&gt, 1484-1486. Tempera on canvas, 172.5x278.9cm.</p>

- Day 8 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day7/Note.md "Day7 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day9/Note.md "Day9 Note")
