# ๐ Note

### Competition with AI Stages!

- P Stage?

  - U Stage๋ ๋ฐ์ดํฐ ์ฌ์ด์ธ์ค ๊ธฐ๋ณธ ์ง์ํ์ต๊ณผ ํ์ด์ฌ ๋ฐ ๋ฅ๋ฌ๋ ํ๋ ์์ํฌ ๊ธฐ์ด ๊ณผ์ .
  - P Stage๋ ๊ฒฝ์ง๋ํ๋ฅผ ํตํ ํ๋ก์ ํธ ์ค์ต.
  - ์ ์ฒ๋ฆฌ, ํ์ต, ์ถ๋ก ๊น์ง ์ ์ฒด์ ์ธ ๊ณผ์ .
  - ์ด๋ก ์ ๋ฐํ์ผ๋ก ๋ฐฐ์ด ๊ฒ์ ์ค์  ๋ฐ์ดํฐ์ ์ฝ๋๋ฒ ์ด์ค๋ก ์ ์ฉํด ๋ณด์. ์ด์ ์ ์ดํดํ์ง ๋ชปํ ๊ฒ๋ค์..? ๋ค์ ๋ณด๋ ์๋ฐ์.

- Competition

  - ์ฃผ์ด์ง ๋ฐ์ดํฐ๋ฅผ ์ด์ฉํด ์ํ๋ ๊ฒฐ๊ณผ๋ฅผ ๋ง๋ค๊ธฐ ์ํ ๊ฐ์ฅ ์ข์ ๋ฐฉ๋ฒ์ ์ฐพ์๋ณด๊ธฐ. ex) Kaggle, DACON
  - ์ฐธ์ฌํด์ ๋ฐฐ์ฐ๊ธฐ.
  - Problem Definition : ๋ฌธ์  ์ ์. ๋ด๊ฐ ์ง๊ธ ํ์ด์ผ ํ  ๋ฌธ์ ๋ ๋ฌด์์ธ๊ฐ? ์ด ๋ฌธ์ ์ Input๊ณผ Output์ ๋ฌด์์ธ๊ฐ? ์ด ์๋ฃจ์์ ์ด๋์ ์ด๋ป๊ฒ ์ฌ์ฉ๋๋๊ฐ? ์งํ์ ํ๊ธฐ ์ ์ ๊ผญ ์ ํด์ผ ํ  ๊ฒ๋ค.
  - Data Description : ๋ฐ์ดํฐ ์คํ์ ์์ฝํด๋์ ๋ช์ธ์. ์์ ์ ๊ฒํ  ํ์.
  - Notebook : ๋ฐ์ดํฐ ๋ถ์, ๋ชจ๋ธ ํ์ต, ํ์คํธ ์ ์ถ๋ก ์ ๊ณผ์ ์ ์๋ฒ์์ ์ฐ์ต ๊ฐ๋ฅํ๊ฒ ํด์ฃผ๋ ์ฅ์น.
  - Submission & Leaderboard : ํ์คํธ ๊ฒฐ๊ณผ ์ ์ถ ํ ์์ธก ๊ฒฐ๊ณผ๋ฌผ์ ์์๋ฅผ ํ์ธ.
  - Discussion : ๋ฑ์๋ฅผ ์ฌ๋ฆฌ๋ ๊ฒ๋ณด๋ค ์ค์ํ ๊ณผ์ . ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ๋ ค๋ ๋ชฉ์ .

- Machine Learning Pipeline
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day15_img00.PNG" alt="Machine Learning Pipeline"></p>

---

### Image Classification & EDA

- EDA(Exploratory Data Analysis)

  - ํ์์  ๋ฐ์ดํฐ ๋ถ์.
  - ์ด ๋ฐ์ดํฐ๋ฅผ ์ ์ค ๊ฑธ๊น? ๋ฌด์จ ์์ํ์ ๋ด์ผ ํ ๊น? ๋ฐ์ดํฐ์ ํน์ง์ ๋ญ๊น?
  - EDA์์ ๋ญ ์จ์ผ ํ๋์ง, ์ด๋๋ถํฐ ์์ํด์ผ ํ ์ง ๋ชจ๋ฅด๋ ๊ฒฝ์ฐ๋ ์๋๋ฐ? -> ์ค์  ๋ฐ์ดํฐ์ ๋ชฉ์ ๊ณผ ์ฃผ์ , ์๊ณ  ์ถ์ ๊ฒ์ ์์๋ณด๊ธฐ. ์ ๋ฐ ์กฐ์ฌ.
  - ๋งค๋ฒ ์์๋ฅผ ๊ฑฐ์น๋ฉด์ ํ๊ทํ  ์๋ ์๋ค. ์๋ฅผ ๋ค์ด ํธ๋ ์ด๋ ํ ๋ค์ ๋ฐ์ดํฐ ํ์. ์ ๋๊น์ง ๋ณด๊ธฐ.
  - ์ถ์์ ์ธ ํํ๋ฅผ ๋ด ๊ฒ์ผ๋ก ๋ง๋๋ ๊ณผ์ .
  - ์๋ฌด๋ ๊ฒ๋ ์๋ํด๋ ํผ๋์ง ์์ผ๋ ๊ฒ๋ด์ง ๋ง๊ณ  ์ผ๋จ ํด๋ณด๊ธฐ.

- Image

  - ์๊ฐ์  ์ธ์์ ํํํ ์ธ๊ณต๋ฌผ(Artifact)
  - width, height, channel.
  - R, G, B.

- Model

  - Input + Model = Output
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day15_img01.PNG" alt="Model"></p>

  - Image + Classification Model = Class
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day15_img02.PNG" alt="Image Classification Model"></p>

- ์์ผ๋ก์ ํ๋ฆ
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day15_img03.PNG" alt="Baseline flow"></p>

# โ๏ธ Doodle

- P์คํ์ด์ง ์์! ์๋ฐ์ ๋๋์ด ๊ฐํ ๊ฐ์๋ผ๊ณ  ์๊ฐํ์ผ๋, EDA๊ฐ ์๋ค. ์ง์  ์ง  ์ฝ๋๋ณด๋จ ์ฐธ๊ณ  ์์ค๋ฅผ ๋ง์ด ์ฐพ์๋ค. ์ฌํ ํ ๋ก ์ด๋ ์ง์ ๊ฒ์ํ์ ์ ๋ค๋ฌ๋ณด์ง ์์๋๋ฐ, ์๊ฐ๋ณด๋ค ์๋ฃ๊ฐ ํจ์ฌ ๋ง์์ ๋๋๋ค. ์ ์ฝ๋์ ๊ฐ์๊ฐ ์ ๋ถ๋ผ๊ณ  ์๊ฐํ์๊น? ์์ง ์๋ฒ ํ ๋น์ด ๋์ง ์์ ์๋ก์ด ํ๊ฒฝ์์ ์ฝ๋ฉ์ ํ์ง ๋ชปํ์ง๋ง, ์ด์  ํ์ต ์ฝ๋๋ฅผ ์ ๋ฆฌํ๋ ๊ฑธ๋ก๋ ์๊ฐ์ด ๋ถ์กฑํ๋ค. ์ค๋์ ๋์ ํด๋ฆผํธ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Gustav_Klimt_1901_Judith_and_the_Head_of_Holofernes.jpg"></p>
<p align="center">Gustav Klimt, &ltJudith and the Head of Holofernes&gt, 1901. Oil on canvas, 84x42cm.</p>

- Day 15 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day14/Note.md "Day14 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day16/Note.md "Day16 Note")
