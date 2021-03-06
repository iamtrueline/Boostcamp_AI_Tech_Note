# ๐ Note

### Modern CNN - 1x1 convolution์ ์ค์์ฑ

- ILSVRC

  - ImageNet Large-Scale Visual Recogmnition Challenge
  - Classification / Detection / Localization / Segmentation
  - ๋ฐฑ๋ง ๊ฐ๊ฐ ๋๋ ์ด๋ฏธ์ง, ์ฒ์ฌ ๊ฐ์ ๋ค๋ฅธ ์นดํ๊ณ ๋ฆฌ, ํธ๋ ์ด๋ ์ธํธ : 456,567๊ฐ ์ด๋ฏธ์ง.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img00.PNG" alt="์ฐ๋๋ณ Error Rate"></p>

- AlexNet (2011๋๋ ์ฐ์น)

  - ์ฒ์ ํ์ฉ ๋น์์ GPU๊ฐ ๋ถ์กฑ, ์ต๋ํ ๋ง์ ํ๋ผ๋ฏธํฐ๋ฅผ ๋ฃ๊ณ  ์ถ์ด์ ๋คํธ์ํฌ๋ฅผ ๋๊ฐ๋ก ๋๋.
  - 5 Convolutional layers, 3 Dense layers
  - Rectified Linear Unit(ReLU) activation : Preserves properties of linear models(0 ๋ฐ์ผ๋ก 0, ์ด์์ผ๋ก  ์์น) / Easy to optimize with gradient descent / Good generalization / Overcome the vanishing gradient problem
  - GPIimp lementation (2GPUs)
  - Local response normalization, Overlapping pooling
  - Data augmentation
  - Dropout (๋ช ๊ฐ ๋ด๋ฐ์ 0์ผ๋ก)
  - ํ์ฌ ๊ธฐ์ค์ผ๋ก  ๋น์ฐํ ์ ์ฉ๋ค์ด๋, 2011๋๋ ๊ธฐ์ค์ผ๋ก  ํ๊ธฐ์ .
  - 8-layers, 60M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img01.PNG" alt="AlexNet ๊ตฌ์กฐ"></p>

- VGGNet (2014๋๋ ์ค์ฐ์น)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img02.PNG" alt="VGGNet ๊ตฌ์กฐ"></p>

-
  - 3*3 convolution filter๋ง ์ฌ์ฉ. ์? 3*3์ ๋๋ฒ ํ๋ ๊ฒ(18)๊ณผ 5*5๋ฅผ ํ๋ฒ ํ๋๊ฒ(25)๋ Receptive field ์ธก๋ฉด์์  ๋๊ฐ์ง๋ง ๊ณ์ฐ๋์ด ์ฝ 1.5๋ฐฐ ์ฐจ์ด ๋จ(3*3์ด ๊ณ์ฐ์  ์ ๋ฆฌ).
  - ์ดํ ๋ค๋ฅธ ๊ฒ๋ค๋ ๋น์ทํ ์ด์ ๋ก 7*7์ ๋ฒ์ด๋์ง ์์. 1์ ๋ธ์๋ฏธ. 3 ์ ์ . 5์ 7๋ ์ฌ์ฉ ๊ฐ๋ฅ. ์ง์๋ ์ ์์ฐ๋์? -> Anti-Aliasing.
  - 19-layers, 110M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img03.PNG" alt="3*3 convolution vs 5*5 convolution ๊ตฌ์กฐ"></p>

- GoogLeNet (2014๋๋ ์ฐ์น)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img04.PNG" alt="GoogLeNet ๊ตฌ์กฐ"></p>

-
  - Inception blocks : Convolution filter ์ ์ 1*1 ํํฐ๋ฅผ ๊ฑฐ์นจ. ํ๋ผ๋ฏธํฐ๋ฅผ ์ค์ด๋ ์ญํ . ์ด๋ ์ฑ๋ ๋ฐฉํฅ์ผ๋ก ์ฐจ์์ ์ค์ด๋ ์ญํ ์ ํ๋ค.
  - 1*1 ํํฐ์ ์ด์  : ํ๋ผ๋ฏธํฐ๊ฐ ์ฝ 30% ์ค์ด๋ ๋ค.
  - 22-layers, 4M parameters.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img05.PNG" alt="ํํฐ ๊ตฌ์กฐ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img06.PNG" alt="1*1 ํํฐ ๊ณ์ฐ ๋น๊ต"></p>

- ResNet (2015๋๋ ์ฐ์น, ์ต์ด๋ก ์ฌ๋์ ์ฑ๋ฅ์ ๋์)

  - ํธ๋ ์ด๋ ์๋ฌ๊ฐ ์์์๋ ๋ถ๊ตฌํ๊ณ  ์ค์  ํ์คํธ ์๋ฌ๊ฐ ๊ทธ๋งํผ ์ค์ด๋ค์ง ์์(not Overfitting). = ๋คํธ์ํฌ๊ฐ ์ปค์ง์ ๋ฐ๋ผ ํ์ต์ด ๋ถ๊ฐ๋ฅ. ๊ทธ๋์ Identity map(skip connection)์ ์ ์ฉ.
  - Identity map : x๊ฐ์ ์ฐจ์ด๋ง ํ์ต. ์ด๋ฅผ ์ด์ฉํ๋ฉด 18-layer์ ์ฑ๋ฅ์ด 34-layer๋ณด๋ค ๋์๋ ๋ฌธ์ ๋ฅผ ํด๊ฒฐ ๊ฐ๋ฅ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img07.PNG" alt="Identity map"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img08.PNG" alt="18 and 34-layer ๋น๊ต"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img09.PNG" alt="์ ์ฉ ๋ฐฉ๋ฒ"></p>

- DenseNet

  - ๊ฐ์ ๋ํ์ง ๋ง๊ณ  concatenationํ์.
  - ์ด ๋, ์ฑ๋์ด ๋ฌดํ์  ๋์ด๋๊ฒ ๋จ. ๊ทธ๋์ ์ค๊ฐ์ ํ ๋ฒ ์ฉ 1*1 convolution์ผ๋ก ์ค์ฌ๋ฒ๋ฆฌ๊ธฐ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img10.PNG" alt="ResNet, DenseNet ๋น๊ต"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img11.PNG" alt="DenseNet ๊ตฌ์กฐ"></p>

- Summary
  - VGG : repeated 3*3 blocks
  - GoogLeNet : 1*1 convolution
  - ResNet : skip-connection
  - DenseNet : concatenation

---

### Computer Vision Applications

- Semantic Segmentation

  - ๊ฐ ์ด๋ฏธ์ง๋ฅผ ํฝ์๋ณ๋ก ๋ถ๋ฅ & ๋ผ๋ฒจ๋ง.
  - ์์จ์ฃผํ ๋ฑ์ ํ์ฉ.

- FCN(Fully Convolutional Network)

  - ๊ธฐ๋ณธ CNN์์ dense layer๋ฅผ ์์ ๊ณ  convolution์ผ๋ก ๋์ฒดํ๊ธฐ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img12.PNG" alt="ordinary CNN"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img13.PNG" alt="fully convolutional network"></p>

-
  - ๊ฒฐ๊ตญ ํ๋ผ๋ฏธํฐ ์๋ ๊ฐ๋ค. ์ด ์ ์ฐจ๋ช์ Convolutionalization.
  - Why? fully convolution : input image ์ฌ์ด์ฆ์ ์๊ด์์ด ์ ์ฉ ๊ฐ๋ฅ.
  - ์ค์ด๋  output์ ๋ค์ ๋๋ฆฌ๋ ๋ฐฉ๋ฒ : Deconvolution(conv transpose). ์ค์ ๋ก ์ญ์ ์๋๋ค. ๋ฎ์ ํ์ง์ ๋์ ํ์ง๋ก ๋ณต๊ตฌํ  ์ ์๋ฏ์ด(๋ณต๊ตฌ๋ผ๋ ์ด๋ฆ์ ์ถ์ธก ๋ฐ ์์ฑ์ ๊ฐ๋ฅํ ๊ฒ).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img14.PNG" alt="Deconvolution"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img15.PNG" alt="Deconvolution"></p>

- Detection

  - ์ด๋ฏธ์ง ์์์ Region์ ์ถ์ถ(์ฐพ๊ธฐ). ์ด๋ ๋ฌผ์ฒด๊ฐ ์ด๋์ ์๋์?

- R-CNN

  - Input image -> 2,000๊ฐ์ region์ ์ฐพ๊ธฐ -> ๋ชจ๋ ๊ฐ์ ํฌ๊ธฐ๋ก ๋ง์ถ๊ธฐ. -> ๋ถ๋ฅ with linear SVMs.
  - ๋จ์. ๋น๊ต์  ๋ถ์ ํ.

- SPPNet

  - R-CNN์ 2,000๊ฐ๋ฅผ ๋ค ๋๋ฆฐ๋ค. ํ๋๋๊น CNN์ ํ ๋ฒ๋ง ๋๋ฆฌ์ = SPPNet.
  - ๋ฐ์ด๋ฉ์ ๊ตฌํ ์ด๋ฏธ์ง ์ ์ฒด์ ๋ํ convolutional feature map์ ํ ๋ฒ ๋ง๋ค๊ณ , ๋ฐ์ด๋์ ํด๋นํ๋ feature๋ง ๊ฐ์ ธ์ค๋ ๊ฒ.

- Fast R-CNN

  - ๋ฐ์ด๋ฉ์ ๊ตฌํ ์ด๋ฏธ์ง ์ ์ฒด์ ๋ํ convolutional feature map์ ํ ๋ฒ ๋ง๋ค๊ณ , ROI pooling์ ํตํด feature๋ฅผ ๋ฝ์ ํ class์ bounding-box regressor๋ฅผ ์ถ์ถ.
  - SPPNet๊ณผ ์ฐจ์ด : ๋ง์ง๋ง์ ๋ด๋ด ๋คํธ์ํฌ๋ฅผ ์ฌ์ฉํ๋ค๋ ์ (ROI pooling).

- Faster R-CNN

  - RPN(Region Proposal Network) + Fast R-CNN
  - RPN : ์ด๋ฏธ์ง ๋ด ํน์  ์์ญ์ ๋ฌผ์ฒด๊ฐ ์๋์ง ์๋์ง ํ๋จ. anchor box = ๋ฏธ๋ฆฌ ์์ธก๋ ์ฌ์ด์ฆ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img16.PNG" alt="RPN ๋ฐ์ด๋ฉ ํ๋จ"></p>

- YOLO (v1)

  - Faster R-CNN๋ณด๋ค ํจ์ฌ ๋น ๋ฅธ ๋ฌผ์ฒด ์ธ์ ์๊ณ ๋ฆฌ์ฆ.
  - ์ด๋ฏธ์ง ํ ์ฅ์์ ๋ฐ๋ก ์์ํ. ๋ฐ์ด๋ฉ ๋ฐ์ค ๋ถ๋ฅ ๊ณผ์  ์๋ต.
  - Input image -> divide SxS grid. (๋ฌผ์ฒด๊ฐ grid ์์ ๋ค์ด๊ฐ๋ฉด detection๋ ํจ๊ป) -> B๊ฐ(ex. 5)์ ๋ฐ์ด๋ฉ ๋ฐ์ค ์์ธก. ๋ฐ ์ค์  ๋ฌผ์ฒด๊ฐ ์๋์ง ํ๋จ + ๋ฌผ์ฒด class(C) ์์ธก -> tensor = SxS(B^5+C) size.
  - ๋ฐ์ด๋ฉ ๋ฐ์ค ์ฐพ๊ธฐ์ ํด๋์ค ์์ธก์ด ํจ๊ป ์ด๋ฃจ์ด์ ธ์ ์๋ ํฅ์.

---

### Sequential Models - RNN(Recurrent Neural Networks)

- Sequential Model

  - ์ผ์ ์ ๋๋ถ๋ถ์ ๋ฐ์ดํฐ๊ฐ ์ํ์ ๋ฐ์ดํฐ.
  - ์ฒ๋ฆฌ์ ์ด๋ ค์ : ์ํ๋ ์ ๋ณด๋ ํน์  ๋ผ๋ฒจ ํ๋์ผ ๊ฒฝ์ฐ๊ฐ ๋ง์๋ฐ, ๊ทธ๋ฅผ ์ํด ์ผ๋ง๋ ๋ง์ ๊ธธ์ด์ ๋ฐ์ดํฐ๊ฐ ํ์ํ์ง ์ฝ๊ฒ ์ ์ ์์. ๋ฐ๋ผ์, ์ธํ ๊ธธ์ด์ ์๊ด์์ด ๋์ํ๋ ๋ชจ๋ธ์ด ํ์.
  - ๊ฐ์ฅ ๊ฐ๋จํ ์ฒ๋ฆฌ๋ ์ ํด์ง ๊ตฌ๊ฐ์ ๊ณผ๊ฑฐ ์ ๋ณด๋ง ์ฐธ๊ณ ํ๋ ๊ฒ. (ex. ๋ค์ ๋จ์ด ์์ธก์ ๋ฐ๋ก ์ง์  2๊ฐ ๋จ์ด๋ง ์ฌ์ฉ)
  - Markov model : ๋์ ํ์ฌ๋ ๋ฐ๋ก ์ง์ ์ ๊ณผ๊ฑฐ์๋ง dependent๋ผ๋ ๊ฐ์ .
  - Latent autoregressive model : ๋ฐ๋ก ์ง์ ์ด ์๋ ์ ์ฒด ๊ณผ๊ฑฐ์ ์ ๋ณด๋ฅผ ์์ฝํ ํ๋  state๋ฅผ ์ฌ์ฉ.

- RNN

  - ์๋ ฅ๊ณผ ์ถ๋ ฅ์ ์ํ์ค ๋จ์๋ก ์ฒ๋ฆฌํ๋ ๋ชจ๋ธ. ์๋์ธต(ํ๋  state)์ ๋ธ๋์์ ํ์ฑํ ํจ์๋ฅผ ํตํด ๋์จ ๊ฒฐ๊ณผ๊ฐ์ ์ถ๋ ฅ์ธต ๋ฐฉํฅ์ผ๋ก๋ ๋ณด๋ด๋ฉด์, ๋ค์ ์๋์ธต ๋ธ๋์ ๋ค์ ๊ณ์ฐ์ ์๋ ฅ์ผ๋ก ๋ณด๋ธ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img17.PNG" alt="RNN ๊ตฌ์กฐ"></p>

-
  - ๋ค๋ง, ์ด ๊ฒฝ์ฐ Short-term dependencies๋ผ๋ ๋จ์ ์ด ์กด์ฌ. ๋จผ ๊ณผ๊ฑฐ์ ์ ๋ณด ๊ณ ๋ ค๊ฐ ์ด๋ ค์. ๋ฉ๋ฆฌ ์๋ ๊ณผ๊ฑฐ๋ผ๊ณ  ๊ฐ์น๊ฐ ์ ์ ๊ฒ์ ์๋๋ฏ๋ก ์ด๋ฅผ ๋ณด์ํ๋ ์ผ์ด ์ค์ํ๋ค.
  - ๊ฐ์ค์น๋ ๊ณผ๊ฑฐ์ ์ ๋ณด๋ฅผ ๊ณ์ํด์ ์์ผ๋ฉฐ ๊ณฑ. ํ์ฑํจ์๊ฐ Sigmoid์ผ ๊ฒฝ์ฐ, ๊ฐ์๋ก ๊ฐ์ค์น๊ฐ ๊ณ์ ์ค์ด๋ค์ด ์๋ฏธ๊ฐ ์ฌ๋ผ์ง๋ค. ๋ฐ๋๋ก ReLU๋ผ๋ฉด, ๊ฐ์๋ก ๊ฐ์ค์น๊ฐ ๊ธ์์ผ๋ก ์ปค์ ธ ํ์ต์ด ๋ถ๊ฐ๋ฅ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img18.PNG" alt="RNN ์"></p>

- LSTM(Long Short Term Memory)

 - ๊ธฐ์กด RNN๊ณผ LSTM ๋น๊ต.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img19.PNG" alt="RNN ๊ตฌ์กฐ ์์ฝ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img20.PNG" alt="LSTM ๊ตฌ์กฐ ์์ฝ"></p>

-
  - LSTM ์์ธ
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img21.PNG" alt="LSTM ์์ธ ๊ตฌ์กฐ"></p>

-
  - Forget Gate : ์ด๋ค ์ ๋ณด๋ฅผ ๋ฒ๋ฆด๊น?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img22.PNG" alt="Forget Gate"></p>

-
  - Input Gate : ํ์ฌ ๋ค์ด์จ ์ ๋ณด ์ค ์ด๋ค ์ ๋ณด๋ฅผ ์ ์ฅํ ๊น?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img23.PNG" alt="Input Gate"></p>

-
  - Update cell : ์ฒ๋ฆฌ๋ ์ ๋ณด๋ฅผ ์๋ฐ์ดํธ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img24.PNG" alt="Update cell"></p>

-
  - Output Gate : ํ์ฌ ๊ฒฐ๊ณผ๋ฅผ ์์ํ, ๋ค์ ํ๋ ์คํ์ดํธ๋ก ํ์ฉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img25.PNG" alt="Output Gate"></p>

- GRU(Gated Recurrent Unit)

  - Gate๊ฐ ๋ ๊ฐ. reset and update.
  - cell state๊ฐ ์๋ค. ์ค์ง hidden state ๋ฟ. hidden state๊ฐ ๊ณง output.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day09_img26.PNG" alt="GRU ๊ตฌ์กฐ"></p>

-
  - ์ผ๋ฐ์ ์ผ๋ก LSTM๋ณด๋ค GRU ์ฑ๋ฅ์ด ์ข์ ๊ฒ์ ๋ณผ ์ ์์.

# โ๏ธ Doodle

- ์ด์ ์ ์ด์ ๊นํ๋ธ ๊ฐ์. ์ ์ฉํ๊ณ  ์ค๋ ๊ฑธ๋ฆฐ๋ค. ์ด์ ์น ๋ถ๋๊ณผ ๋๋ถ์ด ์ค๋ ๊ฐ์ ๋์ด๋๊ฐ ์์ด์ ์๋ฒฝํ ์ํ๊ฐ ์ด๋ ต๋ค. ์งง์ ์๊ฐ์ ์ต๋ํ ๊ฐ๊ฒฐํ๊ณ  ์ ํํ ์ ๋ณด ์ ๋ฌ์ ํด์ฃผ์๋ ค๋ ๊ฑด ๋๊ปด์ง๋ค. ๊ทธ๋ ์ง๋ง ๋ด ์ชฝ์ด ์ฐ๋ฑ์์ด ์๋๋ผ์ ๊ธธ์ด๋ ์ข์ผ๋ ๋ ์ ํํ ์ค๋ช์ด ํ์. ๊ตฌํ๊ณผ ํจ๊ป ๋ณด๊ณ  ์ถ์๋ฐ ๊ณผ์ ์๋ ์ฝ๊ฐ ๊ฑฐ๋ฆฌ๊ฐ ์๋ ๊ฒ ์์ฝ๋ค. ์ง์  ์ฝ๋๋ฅผ ์ฐพ์๋ณด๋ ๊ฒ ๋ต. ์ค๋์ ๋์ ๋งํฐ์ค.

<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Henri_Matisse_1910_Dance.jpg"></p>
<p align="center">Henri Matisse, &ltDance&gt, 1910. Oil on canvas, 260x391cm.</p>

- Day 9 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day8/Note.md "Day8 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day10/Note.md "Day10 Note")
