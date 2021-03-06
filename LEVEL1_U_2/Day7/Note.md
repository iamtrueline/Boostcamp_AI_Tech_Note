# ๐ Note

### Optimization

- ์ฉ์ด ์ ์

  - ์ผ๋ฐํ(Generalization) : Training error์ Test error ์ฐจ์ด๊ฐ ์ ๋ค๋ฉด ์ผ๋ฐํ ์ฑ๋ฅ์ด ์ข๋ค๊ณ  ํ๋ค. ์ด๋ ํ์ต ๋ฐ์ดํฐ์์๋ง ์ ๋์ํ๋ ๊ฒ ์๋๋ผ ์ค์  ์คํ ๋ฐ์ดํฐ์์ ์ ๋์ํจ์ ์๋ฏธํ๋ค. ๋ค๋ง ์ผ๋ฐํ ์ฑ๋ฅ์ด ์ข๋ค๊ณ  ํด๋ ํ์ต ๋ฐ์ดํฐ ์์ฒด์ ์ฑ๋ฅ์ด ๋ฎ์ ์๋ ์๋ค.
  - Under-fitting vs Over-fitting : ํ์ต๋ฐ์ดํฐ๋ ์ ๋ง์ถ์ง๋ง ํ์คํธ๋ฐ์ดํฐ ์ ์ฉ์ ์ ์๋๋ ๊ฒฝ์ฐ Over-fitting, ํ์ต ์์ฒด๊ฐ ๋ถ์กฑํด์ ํ์ต๋ฐ์ดํฐ๋ ๋ชป ๋ง์ถ๋ ๊ฒฝ์ฐ Under-fitting.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img00.PNG" alt="Under-fitting vs Over-fitting ๊ทธ๋ํ ์์"></p>

-
  - Crossvalidation : ํ์ต ๋ฐ์ดํฐ์ ํ์ต์ ์ฐ์ด์ง ์์ ๊ฒ์ฆ ๋ฐ์ดํฐ๋ฅผ ๋ ๋ค ์ฌ์ฉํด์ ๊ฒ์ฆ. k-fold cross validation์ด ๊ฐ์ฅ ์ผ๋ฐ์ ์ด๋ค. ์ด๋ ๋ฐ์ดํฐ ์(ํ์ต + ๊ฒ์ฆ)์ k๊ฐ์ subset์ผ๋ก ๋๋๊ณ  k-1๋ฒ subset๊น์ง ํ์ต ํ ๋ง์ง๋ง subset์ผ๋ก ํ๊ฐํ๋ค. ์ด ๋ ๊ฐ Iteration๋ง๋ค test set์ ๋ค๋ฅด๊ฒ ํ ๋นํ์ฌ ์ด k๊ฐ์ '๋ฐ์ดํฐ ํด๋ ์ธํธ'๋ฅผ ๊ตฌ์ฑํ๋ฏ๋ก ๋ชจ๋ธ์ ํ์ต ๋ฐ ํ๋ จํ๋๋ฐ ์ด k๋ฒ์ Iteration์ด ํ์ํ ๊ฒ์ด ํน์ง. ๊ฐ ๋ฐ์ดํฐ ํด๋ ์ธํธ์ ๋ํด์ ๋์จ ๊ฒ์ฆ ๊ฒฐ๊ณผ๋ค์ ํ๊ท ๋ด์ด ์ต์ข์ ์ธ ๊ฒ์ฆ ๊ฒฐ๊ณผ๋ฅผ ๋์ถํ๋ ๊ฒ์ด ์ผ๋ฐ์ .
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img01.PNG" alt="Cross-validation ์์"></p>

-
  - Bias and Variance : Variance๊ฐ ๋ฎ๋ค๋ ๊ฑด ์ถ๋ ฅ์ด ์ผ๊ด์ ์ด๋ผ๋ ๊ฒ(๋ชฉํ์ ์ด ์๋๋ผ๋). Bias๊ฐ ๋ฎ๋ค๋ ๊ฑด ํ๊ท ์ ์ผ๋ก ๋ชฉํ์ ์ ์ ๊ทผํ ๊ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img02.PNG" alt="Bias and Variance"></p>

-
  - Bias and Variance Tradeoff : ํ์ต๋ฐ์ดํฐ์ ๋ธ์ด์ฆ๊ฐ ์๋ค๊ณ  ๊ฐ์ ํ์ ๋, cost๋ bias^2, variance, noise๋ฅผ ๊ฐ๊ฐ ๋ํ ๊ฐ์ผ๋ก ํ์ชฝ์ด ์ค์ด๋ค๋ฉด ํ ์ชฝ์ด ๋์ด๋๋ค. Bias์ Variance ๋ชจ๋ ์ค์ด๋ ๊ฑด ์ด๋ ต๋ค.
  - Bootstrapping : ๊ฒ์ฆ์ ํ๊ธฐ ์  Random sampling์ ์ ์ฉํ๋ ๋ฐฉ๋ฒ. ๋ฐ์ดํฐ ์ค์์ ์ค๋ณต์ ํ์ฉํ์ฌ m๊ฐ๋ฅผ ๋ฝ๊ณ , ๊ทธ๋ค์ ํ๊ท ์ ๊ตฌํ๊ธฐ๋ฅผ ์ฌ๋ฌ ๋ฒ ๋ฐ๋ณต.
  - Bagging : Bootstrapping AGGregatING. bootstrapping์ ํตํด Over-fitting์ ์ค์ผ ์ ์๋ค.
  - Boosting : ์ฌ๋ฌ ๋ชจ๋ธ์ ๋ง๋ค์ด ์ํ์ํ๊ฒ ํฉ์ณ์(not ๋๋ฆฝ์ ) ํ๋์ ๋ชจ๋ธ์ ๊ตฌ์ฑ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img03.PNG" alt="Bagging and Boosting"></p>

- ๊ฒฝ์ฌํ๊ฐ๋ฒ ๋ฐฐ์น ์ฌ์ด์ฆ ์ ํ๊ธฐ.

  - ๋ฐฐ์น ์ฌ์ด์ฆ๋ ์์ ๊ฒ ์ผ๋ฐ์ ์ผ๋ก ์ข๋ค. ์คํ์ ์ผ๋ก, ํฌ๋ฉด Sharp Minimum์ ๋๋ฌ, ์์ผ๋ฉด Flat Minimum์ ๋๋ฌ. Shart Minimum ์ ๋๋ฌํ๋ค๋ ๊ฑด ์ผ๋ฐํ ์ฑํ์ด ๋ฎ๋ค๋ ๊ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img04.PNG" alt="Flat Minimum, Sharp Minimum"></p>

- ๊ฒฝ์ฌํ๊ฐ๋ฒ ์ฉ์ด ์ ์

  - Momentum : ๊ธฐ์กด ๊ฒฝ์ฌํ๊ฐ๋ฒ ๊ทธ๋๋์ธํธ ๋ฐฉ์์ ๊ธฐ์กด ๋ฐฉํฅ์ฑ์ ๊ฐ์ง๊ณ  ์๋ ๋ฒ ํ๊ฐ(๋ชจ๋ฉํ)์ ์ถ๊ฐ. Gradient Descent๋ฅผ ํตํด ์ด๋ํ๋ ๊ณผ์ ์ ์ผ์ข์ โ๊ด์ฑโ์ ์ฃผ๋ ๊ฒ. ์ด ๋ชจ๋ฉํ๊ณผ ๊ธฐ์กด ๊ทธ๋๋์ธํธ๊ฐ ํฉ์ณ์ง ๊ทธ๋๋์ธํธ๋ ํ ๋ฒ ํ๋ฌ๊ฐ๋ ๋ฐฉํฅ์ฑ์ ์ ์งํ๊ธฐ ๋๋ฌธ์ ํ์ต๋ ฅ์ด ์ข์์ง.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img05.PNG" alt="Momentum ์ถ๊ฐ ์"></p>

-
  - Nesterov Accelerated Gradient(NAG) : ๊ธฐ์กด ๋ชจ๋ฉํ์ ํ์ฌ ๋ฐฉํฅ์ฑ์ ์ฌ์ฉํ๊ณ  Nesterov Accelerate์ ์งํ ๊ณ์ฐ๋ ๊ฐ์ ๋ฏธ๋ฆฌ ์ฌ์ฉ. ๋ฉ์ถฐ์ผ ํ  ์ ์ ํ ์์ ์์ ์ ๋์ ๊ฑฐ๋ ๋ฐ์ ํจ์ฌ ์ฉ์ด. Local Minimum์ ๋ ๋น ๋ฅธ ๋๋ฌ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img06.PNG" alt="NAG ์"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img07.PNG" alt="Momentum, NAG ๋น๊ต"></p>

-
  - Adagrad : ๋ณ์๋ค์ updateํ  ๋ ๊ฐ๊ฐ์ ๋ณ์๋ง๋ค step size๋ฅผ ๋ค๋ฅด๊ฒ ์ค์ ํด์ ์ด๋ํ๋ ๋ฐฉ์. step size = ๋ณํ๋. ํ๋ผ๋ฏธํฐ์ ๋ณํ๋์ G์ ์ ์ฅ. ๊ฐ ํ๋ผ๋ฏธํฐ๋ฅผ ๋ณด๋ฉฐ ๋ง์ ๋ณํ๊ฐ ์์์ ๊ฒฝ์ฐ ์ ๊ฒ ๋ณํ, ์ ์ ๋ณํ๊ฐ ์์์ ๊ฒฝ์ฐ ๋ง์ด ๋ณํ์ํค๋ ค๋ ์๋. ์ด ๋ G๋ ๊ทธ๋๋์ธํธ๋ค์ ์ ๊ณฑ์ ๋ํ ๊ฒ์ผ๋ก ๊ณ์ ์ปค์ง๋ค. ์์ ๋ฐ๋ฅด๋ฉด ๋ถ๋ชจ๊ฐ ์ปค์ง๋ W๋ ๊ณ์ ์์์ง๋ค(๋ฉ์ถค).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img08.PNG" alt="Adagrad ์"></p>

-
  - Adadelta : Adagrad์ ํ์ฅ. G๊ฐ ๊ณ์ํด์ ์ปค์ง๋ ๊ฒ์ ๋ง์๋ณด์. ์ ์ฒด ์๊ฐ์ด ์๋๋ผ ํน์  ํ์ ์คํฌํ๋์์ ํ๋ผ๋ฏธํฐ๋ง ๋ณด๋ ๊ฒ. Learning rate์ด ์๋ค. ์ฆ, ๋ฐ๊ฟ ์ ์๋ ๊ฐ์ด ์์ด์ ๋ง์ด ํ์ฉ๋์ง ์์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img09.PNG" alt="Adadelta ์"></p>

-
  - RMSprop : Adagrad์ ๋จ์ (G๊ฐ ์ปค์ง)์ ํด๊ฒฐํ๊ธฐ ์ํ ๋ ๋ค๋ฅธ ๋ฐฉ๋ฒ. Adagrad์์์ gradient์ ์ ๊ณฑ๊ฐ์ ๋ํด๋๊ฐ๋ฉด์ ๊ตฌํ Gt ๋ถ๋ถ์ ํฉ์ด ์๋๋ผ ์ง์ํ๊ท ์ผ๋ก ๋ฐ๊พธ์ด์ ๋์ฒดํ ๋ฐฉ๋ฒ. G๊ฐ ๋ฌดํ์  ์ปค์ง์ง๋ ์์ผ๋ฉด์ ์ต๊ทผ ๋ณํ๋์ ๋ณ์ ๊ฐ ์๋์ ์ธ ํฌ๊ธฐ ์ฐจ์ด๋ ์ ์ง.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img10.PNG" alt="RMSprop ์"></p>

-
  - Adam(Adaptive Moment Estimation) : RMSProp๊ณผ Momentum ๋ฐฉ์์ ํจ๊ณผ์ ์ผ๋ก ํฉ์น ์๊ณ ๋ฆฌ์ฆ. Momentum ๋ฐฉ์๊ณผ ์ ์ฌํ๊ฒ ์ง๊ธ๊น์ง ๊ณ์ฐํด์จ ๊ธฐ์ธ๊ธฐ์ ์ง์ํ๊ท ์ ์ ์ฅํ๋ฉฐ, RMSProp๊ณผ ์ ์ฌํ๊ฒ ๊ธฐ์ธ๊ธฐ์ ์ ๊ณฑ๊ฐ์ ์ง์ํ๊ท ์ ์ ์ฅ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img11.PNG" alt="Adam ์"></p>

- Regularization(์ ์นํ)

  - ํ์ต์ ๋ฐฉํด. ํ์ต ๋ฐ์ดํฐ ๋ฟ ์๋๋ผ ํ์คํธ ๋ฐ์ดํฐ์๋ ์ ์ ์ฉ๋๋๋ก ํ๋ ๊ฒ์ด ๋ชฉ์ .
  - Early Stopping : ์ผ๋ฐ์ ์ผ๋ก ์ง์์ ์ธ ํ์ต์์ ํ์ต ์๋ฌ๊ฐ ์ ์ด์ง๋ฉด ํ์คํธ ์๋ฌ๊ฐ ์ปค์ง๋ค. ์ด ์ฐจ์ด๊ฐ ๋ฒ์ด์ง๊ธฐ ์์ํ  ๋ ํ์ต์ ๋ฉ์ถฐ๋ฒ๋ฆฌ๋ ๊ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img12.PNG" alt="Early Stopping"></p>

-
  - Parameter Norm Penalty : ๋น์ฉํจ์์ ์ ๊ณฑ์ ๋ํ๊ฑฐ๋(L2) ์ ๋๊ฐ์ ๋ํด์(L1) ์จ์ดํธ์ ํฌ๊ธฐ์ ์ ํ์ ์ค๋ค.
  - Data Augmentation : ๋ฐ์ดํฐ๊ฐ ๋ง์ผ๋ฉด ์ผ๋ฐ์ ์ผ๋ก ์ฑ๋ฅ์ด ์ข๋ค. ๊ทธ๋ฌ๋ ๋ฐ์ดํฐ๋ ํ์ ์ ์ด๋ฏ๋ก ์ด๋ค ์์ผ๋ก๋  ๋๋ ค์ผ ํ๋ค. ์๋ฅผ ๋ค์ด ํน์  ์ด๋ฏธ์ง๋ฅผ ๋๋ฆฌ๊ณ  ๊ตฌ๊ธฐ๊ณ  ํ๋ ๋ฑ.
  - Noiserobustness : ์๋ ฅ ๋ฐ์ดํฐ์ ๋ธ์ด์ฆ๋ฅผ ๋ํ๋ค. Data Augmentation๊ณผ์ ์ฐจ์ด์ ? ๋จ์ํ ์๋ ฅ ๋ฟ ์๋๋ผ ์จ์ดํธ์๋ ๋ธ์ด์ฆ ๋ผ๊ธฐ.
  - Labelsmoothing : ํ์ต ๋ฐ์ดํฐ๋ฅผ ๋ ๊ฐ ๋ฝ์ ์๋๋ค. Division Boundary๋ฅผ ๋ถ๋๋ฝ๊ฒ ๋ง๋ค์ด์ค๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img13.PNG" alt="Labelsmoothing ์์"></p>

-
  - Dropout : ๋๋คํ๊ฒ ๋ช ๋ด๋ฐ์(ex. 50%) ์จ์ดํธ๋ฅผ 0์ผ๋ก ๋ฐ๊พผ๋ค. ์ผ๋ฐ์ ์ผ๋ก ์ฌ์ฉ ์ ์ฑ๋ฅ์ด ์ฌ๋ผ๊ฐ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img14.PNG" alt="Dropout"></p>

-
  - Batch Normalization : ํ๊ท ๊ณผ ๋ถ์ฐ์ ์กฐ์ ํ๋ ๊ณผ์ ์ด ๋ณ๋์ ๊ณผ์ ์ผ๋ก ๋ผ์ด์ง ๊ฒ์ด ์๋๋ผ, ์ ๊ฒฝ๋ง ์์ ํฌํจ๋์ด ํ์ต ์ ํ๊ท ๊ณผ ๋ถ์ฐ์ ์กฐ์ ํ๋ ๊ณผ์  ์ญ์ ๊ฐ์ด ์กฐ์ . ์ผ๋ฐ์ ์ผ๋ก  ์ฑ๋ฅ ํฅ์์ ๋์. ์ด์ ํ์์ผ๋ก ํ ๋ ์ด์ด๋ง, ํน์  ๊ทธ๋ฃน๋ง Normalization ํ๋ ํํ๊ฐ ์๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img15.PNG" alt="Batch Normalization ์์"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day07_img16.PNG" alt="Batch Normalization ํ์"></p>

# โ๏ธ Doodle

- ์ ๊ท ์์ ์ธ ํ์ ๊ฐ์ ํด๋์ค๊ฐ ๋ง์๋ ๋ . ๋๋ฉ์ธ ๊ฒฐ์ ์ ๋์ ๋ฐ์ ์ ์๋ ์ธํฐ๋ทฐ์ ์๊ฐํ์ ๊ดํ ๋ค๋ฅธ ๊ฐ๋ก ์ด ์ฃผ์ ์๋ค. ๋๋ฉ์ธ์ ๋ด๊ฐ ๋ ์ํ๋ ๊ฑธ ๊ฐ๋ ๊ฒ ์ ๋ต์ด๋ผ๊ณ  ํ๋ค. ์ ๋ฐฐ์ธ ์ ์๋ ํ์์์ ์์ ๊ฐ์๋ฅผ ๋ญ๋ก ํ ์ง ์ ํ๋ ์ผ์ ์คํ๋ ค ์ด๋ ต๋ค. ์ผ๋จ์ ์ค๋ฌธ๋๋ก NLP ๊ณ . ๋ ๊ทธ๊ฒ ๋ ๋ง์์ ๋ค์ด. ์ ํ ๊ณผ์ ๋ก ์ฃผ์ด์ง Vision Transformer, Adversarial Auto-Encoder ๋ ๊ฐ์์ ๋์ ์์ด ์ง๊ธฐ ํ๋ค๋ค. ํ์์ด ์์ด ๋์์ ๋ฐ์ ์ ์๋ ๊ฒ ๋คํ. ํ์ง๋ง ์์ง ์๋ฒฝํ ์ดํด๋ ๋ถ๊ฐ. ์ฝ๋ ๋ฏ๋ ๊ฒ๋ ์๊ฐ์ด ๋ง์ด ์์๋๋ ๋ง์ด ๋ ์ด์ฌํ ํด์ผ ํ  ๊ฒ. ์ค๋์ ๋์ ๋ผํ์๋ก.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Raffaello_1509_The_School_of_Athens_.jpg"></p>
<p align="center">Raffaello, &ltThe School of Athens&gt, 1509-1511. Fresco, 500x770cm.</p>

- Day 7 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day6/Note.md "Day6 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day8/Note.md "Day8 Note")
