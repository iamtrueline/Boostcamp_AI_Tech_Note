# ๐ Note

### ๋ชจ๋ธ ๋ถ๋ฌ์ค๊ธฐ

- model.save()

  - ํ์ต์ ๊ฒฐ๊ณผ๋ฅผ ์ ์ฅํ๊ธฐ ์ํ ํจ์. ๋ชจ๋ธ ํํ(architecture)์ ํ๋ผ๋ฏธํฐ๋ฅผ ์ ์ฅํ๋ค.
  - ๋ง๋ค์ด์ง ๋ชจ๋ธ์ ์ธ๋ถ ์ฐ๊ตฌ์์ ๊ณต์ ํ์ฌ ํ์ต ์ฌ์ฐ์ฑ ํฅ์.

- checkpoints

  - ํ์ต์ ์ค๊ฐ ๊ฒฐ๊ณผ๋ฅผ ์ ์ฅํ์ฌ ์ต์ ์ ๊ฒฐ๊ณผ๋ฅผ ์ ํ.
  - earlystopping ๊ธฐ๋ฒ ์ฌ์ฉ์ ์ด์  ํ์ต์ ๊ฒฐ๊ณผ๋ฌผ์ ์ ์ฅ.
  - loss์ metric ๊ฐ์ ์ง์์ ์ผ๋ก ํ์ธ ์ ์ฅ.
  - ์ผ๋ฐ์ ์ผ๋ก epoch, loss, metric์ ํจ๊ป ์ ์ฅํ๋ค.
  - colab์์ ์ง์์ ์ธ ํ์ต์ ์ํด ํ์.

- Transfer learning

  - ๋ค๋ฅธ ๋ฐ์ดํฐ์์ผ๋ก ๋ง๋  ๋ชจ๋ธ์ ํ์ฌ ๋ฐ์ดํฐ์ ์ ์ฉ.
  - '์ผ๋ฐ์ ์ผ๋ก' ๋์ฉ๋ ๋ฐ์ดํฐ์์ผ๋ก ๋ง๋ค์ด์ง ๋ชจ๋ธ์ ์ฑ๋ฅ์ด ๋๊ณ  ํ์ฌ์ DL์์๋ ๊ฐ์ฅ ์ผ๋ฐ์ ์ธ ํ์ต ๊ธฐ๋ฒ.

- Freezing

  - pretrained model์ ํ์ฉ์ ๋ชจ๋ธ์ ์ผ๋ถ๋ถ์ ๊ณ ์ .
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img00.PNG" alt="pretrained model"></p>

---

### Monitoring tools for PyTorch

- Tensorboard

  - TensorFlow์ ํ๋ก์ ํธ๋ก ๋ง๋ค์ด์ง ์๊ฐํ ๋๊ตฌ.
  - ํ์ต ๊ทธ๋ํ, metric, ํ์ต ๊ฒฐ๊ณผ์ ์๊ฐํ ์ง์.
  - PyTorch๋ ์ฐ๊ฒฐ ๊ฐ๋ฅ โ DL ์๊ฐํ ํต์ฌ ๋๊ตฌ.
  - scalar : metric ๋ฑ ์์ ๊ฐ์ ์ฐ์(epoch)์ ํ์.
  - graph : ๋ชจ๋ธ์ computational graph ํ์.
  - histogram : weight ๋ฑ ๊ฐ์ ๋ถํฌ๋ฅผ ํํ.
  - Image : ์์ธก๊ฐ๊ณผ ์ค์  ๊ฐ์ ๋น๊ต ํ์.
  - mesh : 3d ํํ์ ๋ฐ์ดํฐ๋ฅผ ํํํ๋ ๋๊ตฌ.

- weight & biases

  - ๋จธ์ ๋ฌ๋ ์คํ์ ์ํํ ์ง์ํ๊ธฐ ์ํ ์์ฉ๋๊ตฌ.
  - ํ์, code versioning, ์คํ ๊ฒฐ๊ณผ ๊ธฐ๋ก ๋ฑ ์ ๊ณต.
  - MLOps์ ๋ํ์ ์ธ ํด๋ก ์ ๋ณ ํ๋ ์ค.

---

### ๊ธฐ๋ณธ ์ฐจํธ์ ์ฌ์ฉ 2-2 ~ 2-3๊ฐ

- Line Plot

  - ์ฐ์์ ์ผ๋ก ๋ณํํ๋ ๊ฐ์ ์์๋๋ก ์ ์ผ๋ก ๋ํ๋ด๊ณ , ์ด๋ฅผ ์ ์ผ๋ก ์ฐ๊ฒฐํ ๊ทธ๋ํ.
  - ๊บพ์์  ๊ทธ๋ํ, ์  ๊ทธ๋ํ, line chart, line graph ๋ฑ์ ์ด๋ฆ์ผ๋ก ์ฌ์ฉ๋จ.
  - ์๊ฐ/์์์ ๋ํ ๋ณํ์ ์ ํฉํ์ฌ ์ถ์ธ๋ฅผ ์ดํผ๊ธฐ ์ํด ์ฌ์ฉ. ์๊ณ์ด ๋ถ์์ ํนํ.
  - .plot()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img01.PNG" alt="Line plot"></p>

-
  - ์ฌ์ฉ์ ๊ฐ๋์ฑ์ ์ํด 5๊ฐ ์ดํ์ ์ ์ ์ฌ์ฉํ์. ๋ง์ผ๋ฉด ํ์ ๋๋๊ฐ ์ฌ๋ผ๊ฐ.
  - ์์๊ฐ๊ฐ ๋ณ๋ํ๋ ๋ฐ์ดํฐ๋ Noise๋ก ์ธํด ํจํด ๋ฐ ์ถ์ธ ํ์์ด ์ด๋ ค์ฐ๋ฏ๋ก smoothing์ฌ์ฉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img02.PNG" alt="smoothing"></p>

- ์ ํํ Line Plot

  - ์ถ์ธ๋ฅผ ๋ณด๊ธฐ ์ํ ๋ชฉ์ ์ด๋ฏ๋ก Bar plot๊ณผ ๋ค๋ฅด๊ฒ ๊ผญ ์ถ์ 0์ ์ด์ ์ ๋ ํ์๋ ์๋ค.
  - ๋๋ฌด ๊ตฌ์ฒด์ ์ธ line plot๋ณด๋ค๋ ์๋ต๋ line plot์ ์ฌ์ฉํ๊ธฐ. ๋ํ์ผํ ์ ๋ณด๋ ํ๋ก ์ ๊ณต.
  - ์๋ต๋์ง ์๋ ์ ์์ ๋ฒ์๋ฅผ ์กฐ์ ํ์ฌ ๋ณํ์จ ๊ด์ฐฐ. (.set_ylim())
  - ๊ท์น์ ์ธ ๊ฐ๊ฒฉ์ ๋ฐ์ดํฐ๊ฐ ์๋๋ผ๋ฉด ๊ฐ ๊ด์ธก ๊ฐ์ ์ ์ผ๋ก ํ์ํ์ฌ ์คํด๋ฅผ ์ค์ด์.
  - ๋ณด๊ฐ : ์ ๊ณผ ์  ์ฌ์ด์ ๋ฐ์ดํฐ๊ฐ ์๊ธฐ์ ์ด๋ฅผ ์๋ ๋ฐฉ๋ฒ. ๋ฐ์ดํฐ์ error๋ noise๊ฐ ํฌํจ๋์ด ์๋ ๊ฒฝ์ฐ, ๋ฐ์ดํฐ์ ์ดํด๋ฅผ ๋๋ ๋ฐฉ๋ฒ. ๊ทธ๋ฌ๋ ์๋ ๋ฐ์ดํฐ๋ฅผ ์๋ค๊ณ  ์๊ฐํ๊ฒ ํ  ์ ์์ผ๋ฉฐ ์์ ์ฐจ์ด๋ฅผ ์์จ ์ ์์ผ๋ฏ๋ก ์ผ๋ฐ์ ์ธ ๋ถ์์์๋ ์ง์.
  - ์ด์ค ์ถ : ํ plot์ ๋ํด 2๊ฐ์ ์ถ. 2๊ฐ์ plot์ ๊ทธ๋ฆฌ๋ ๊ฒ์ด ์ด์ค ์ถ ์ฌ์ฉ๋ณด๋ค ๋ซ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img03.PNG" alt="์ด์ค ์ถ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img04.PNG" alt="์ด์ค ์ถ->๋ ๊ฐ ํ๋กฏ"></p>

-
  - ETC : ๋ผ์ธ ๋ ๋จ์ ๋ ์ด๋ธ์ ์ถ๊ฐํ๋ฉด ์๋ณ์ ๋์ (๋ฒ๋ก ๋์ ). Min/Max ์ ๋ณด(๋๋ ์ํ๋ ํฌ์ธํธ)๋ ์ถ๊ฐํด์ฃผ๋ฉด ๋์์ด ๋  ์ ์์. (annatation) ๋ณด๋ค ์ฐํ ์์ ์ฌ์ฉํ์ฌ uncertainty ํํ ๊ฐ๋ฅ (์ ๋ขฐ๊ตฌ๊ฐ, ๋ถ์ฐ ๋ฑ).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img05.PNG" alt="๋ผ์ธ ๋ ๋จ์ ๋ ์ด๋ธ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img06.PNG" alt="Min/Max ์ ๋ณด"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img07.PNG" alt="uncertainty ํํ"></p>

- Scatter Plot

  - ์ ์ ์ฌ์ฉํ์ฌ ๋ feature๊ฐ์ ๊ด๊ณ๋ฅผ ์๊ธฐ ์ํด ์ฌ์ฉํ๋ ๊ทธ๋ํ. ์ฐ์ ๋. ์ ์์ ๋ค์ํ variation ์ฌ์ฉ ๊ฐ๋ฅ(์, ๋ชจ์, ํฌ๊ธฐ).
  - ์ง๊ต ์ขํ๊ณ์์ x์ถ/y์ถ์ feature ๊ฐ์ ๋งคํํด์ ์ฌ์ฉ.
  - .scatter()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img08.PNG" alt="Scatter Plot"></p>

-
  - Scatter plot์ ๋ชฉ์  : ์๊ด ๊ด๊ณ ํ์ธ(์, ์, ์์), ๊ตฐ์ง, ๊ฐ ์ฌ์ด ๊ฐ๊ทน, ์ด์์น ์ธก์ .
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img09.PNG" alt="Scatter plot ๊ด์ฐฐ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img10.PNG" alt="Scatter plot ๊ด์ฐฐ"></p>

- ์ ํํ Scatter Plot

  - ์ ์ด ๋ง์์ง์๋ก ์ ์ ๋ถํฌ๋ฅผ ํ์ํ๊ธฐ ํ๋ค๋ค -> ํฌ๋ช๋ ์กฐ์ , ์งํฐ๋ง(jittering), 2์ฐจ์ ํ์คํ ๊ทธ๋จ, Contour plot (๋ฑ๊ณ ์ )ํ์ฉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img11.PNG" alt="Scatter plot ์กฐ์ "></p>

-
  - ์ : ์ฐ์์ gradient, ์ด์ฐ์ ๊ฐ๋ณ ์์์ผ๋ก.
  - ๋ง์ปค : ๊ฑฐ์ ๊ตฌ๋ณํ๊ธฐ ํ๋ค๋ค + ํฌ๊ธฐ๊ฐ ๊ณ ๋ฅด์ง ์์.
  - ํฌ๊ธฐ : ๋ฒ๋ธ ์ฐจํธ (bubble chart). ๊ด๊ณ๋ณด๋ค๋ ๊ฐ ์ ๊ฐ ๋น์จ์ ์ด์ . SWOT ๋ถ์ ๋ฑ์ ํ์ฉ.
  - ์ธ๊ณผ ๊ด๊ณ (causal relation)๊ณผ ์๊ด ๊ด๊ณ (correlation)๋ ๋ค๋ฅด๋ค. ์ธ๊ณผ ๊ด๊ณ๋ ํญ์ ์ฌ์  ์ ๋ณด์ ํจ๊ป ๊ฐ์ ์ผ๋ก ์ ์.
  - ์ถ์ธ์ ์ ์ฌ์ฉํ๋ฉด scatter์ ํจํด์ ์ ์ถํ  ์ ์์. ๋จ, 2๊ฐ ์ด์์ด ๋๋ฉด ๊ฐ๋์ฑ์ด ๋จ์ด์ง๋ฏ๋ก ์ฃผ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img12.PNG" alt="์ถ์ธ์ "></p>

-
  - Grid๋ ์ง์. ์ฌ์ฉํ๋ค๋ฉด ์ต์ํ์ผ๋ก. ๋ฒ์ฃผํ์ด ํฌํจ๋ ๊ด๊ณ์์๋ heatmap ๋๋ bubble chart๋ฅผ ์ถ์ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day13_img13.PNG" alt="Grid&๋ฒ์ฃผ"></p>


# โ๏ธ Doodle

- ์ ๋ฆฌ๋ณด๋ค ๊ณผ์ ๊ฐ ์ ์. ๊ทธ๋์ ๋ด ์๋ง์ด ๋ถ์กฑํ๋ค. ๊ณผ์ ๋ ์ผ๋จ ํด๊ฒฐ์ด ์ฐ์ ์ด๋ผ๋ ์์ผ๋ก ์ง ๋์์ ๋ค์ ํ๋ฒ ๋ค์ถฐ์ผ ํ  ๊ฒ ๊ฐ๋ค. ๋ฌธ์ ๋ ๋ค์์ฃผ์ ๋ํ๋ผ๋ ๊ฑฐ์ง. ์ค๋์ ๋์ ์ด๋ฏธ ์ง๋ฌ์ง๋ง, ๊ทธ๋๋! ์ค๋์ ๋์ ํ๋ฆฌ๋ค ์นผ๋ก.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Frida_Kahlo_1951_Still_Life_with_Parrot_and_Flag.jpg"></p>
<p align="center">Frida Kahlo, &ltStill Life with Parrot and Flag&gt, 1951. Oil on masonite, 28x40cm.</p>

- Day 13 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day12/Note.md "Day12 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day14/Note.md "Day14 Note")
