# ๐ Note

### Convolution์ ๋ฌด์์ธ๊ฐ?

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
  - ํํฐ๋ฅผ ์ด๋ฏธ์ง์ ์ ์ฉํ๋ฉด ํฌ๊ธฐ๋ ์ด๋ฏธ์ง - ํํฐ + 1(Stride 1, None Padding ์กฐ๊ฑด ์์). ์ด ๋, ํํฐ๋ Stack-Up ํ์ฌ ์ต์ข ๊ฒฐ๊ณผ์ ํฌ๊ธฐ๋ฅผ ์์ ์๋ ์๋ค. (ex. 32*32*3 ์ด๋ฏธ์ง๋ฅผ 5*5*3ํํฐ ์ ์ฉ ํ 28*28*4 ๋ก ์ถ๋ ฅ = ํํฐ๋ 4๊ฐ)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img03.PNG" alt="ํํฐ ์ ์ฉ ์์"></p>

-
  - CNN์ Convolution layer, pooling layer, fully connected layer์ ์กฐํฉ.
  - Convolution, pooling layer : feature extraction
  - Fully connected layer : decision making (๋ถ๋ฅ ๋ฑ)
  - Stride : ์ผ๋ง๋ ์ด์ดํ๊ฒ ํํฐ(์ปค๋)๋ฅผ ์ฐ์๊ฑฐ์ผ? ๊ธฐ๋ณธ : 1. ๋ง์ฝ 2๋ผ๋ฉด ์ด๋ฏธ์ง๋ฅผ ๋ ์นธ์ฉ ๋ผ์ ์ฐ๋๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img04.PNG" alt="Stride"></p>

-
  - Padding : ๋ง๋๋ ๊ฐ. ๊ฐ์ ์๋ ๊ฐ๊น์ง ํฌํจํด์ ์ฐ์ผ๋ฉด ์์ํ์ ์ฐจ์๋ ๋๊ฐ์์ง๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img05.PNG" alt="Padding"></p>

- 1*1 Convolution

  - ์ฐจ์ ์ถ์.
  - ๊น์ด๋ ๊น๊ฒ, ํ๋ผ๋ฏธํฐ๋ ์ค์ด๊ธฐ.
  - CNN์ ๋ท ๋จ, Fully convolution์ ์ฐจ์์ด ๋์ผ๋ฉด ๋น์ฉ์ด ๋๋ฌด ๋๊ฒ ์ฐ์ถ๋จ. ์ฐจ์ ์ถ์๋ ๋น์ฉ์ ์ค์ด๊ณ  ์ฑ๋ฅ์ ๋์ด๋ ๋ฐฉ๋ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img06.PNG" alt="CNN ์ ์ฒด"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day08_img07.PNG" alt="Convolution"></p>

# โ๏ธ Doodle

- ๋ด์ฉ์ด ์์ฃผ ๊น์ง ์์ง๋ง ์๋ฒฝํ๊ฒ ์ํํ๋ ค๋ฉด ์๊ฐ์ด ํ์ํ๋ค. ๋ง์ด ๋ค์ด๋ดค๋ ์ฐ์ฌ, ์ด๊ณ ์๋์ ๊นํ๋ธ ๊ฐ์๋ ํจ๊ป ์๋ ๋ . ์ถฉ๋ถํ ์ํ๋ฅผ ํ๋์ง ๋ชจ๋ฅด์ง๋ง ๋ธ๋ ฅํด์ผ์ง. ๋ชธ์ด ๋๋ฌด ์ ์ข์ ๋ธํธ ๊ธฐ๋ก์ ์ ์ ์ถ์. ๋ด์ผ ํ๋ด. ์ค๋์ ๋์ ๋ณดํฐ์ฒผ๋ฆฌ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Sandro_Botticelli_1484_The_Birth_of_Venus.jpg"></p>
<p align="center">Sandro Botticelli, &ltThe Birth of Venus&gt, 1484-1486. Tempera on canvas, 172.5x278.9cm.</p>

- Day 8 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day7/Note.md "Day7 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day9/Note.md "Day9 Note")
