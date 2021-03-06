# ๐ Note

### Dataset

- Pre-processing

  - ์ฃผ์ด์ง ๋ฐ๋๋ผ ๋ฐ์ดํฐ๋ฅผ ๋ชจ๋ธ์ด ํ์ตํ  ์ ์๋ ํํ๋ก ๋ง๋ค๊ธฐ.
  - ๋ณดํต ๊ฒฝ์ง๋ํ์ฉ ๋ฐ์ดํฐ๋ ํ์ง์ด ์ข๋ค. ๋ํ ํจ์จ != ์ค์  ํจ์จ.
  - Bounding box : ํ์ ์ด์์ ์ ๋ณด๋ผ๋ฉด ๊ฐํ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img00.PNG" alt="Bounding box"></p>

-
  - Resize : ํจ์จ์ ์ธ ๊ณ์ฐ์ ์ํด ์ฌ์ด์ฆ ๋ณ๊ฒฝ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img01.PNG" alt="Resize"></p>

-
  - ์ ์ฒ๋ฆฌ๋ ๋ฐ์ดํฐ ํ์๊ณผ ๋ชฉ์ ์ ๋ฐ๋ผ ์ฌ๋ฌ ํํ๊ฐ ์กด์ฌ. ๊ณ ๋ฏผ๊ณผ ์ฐ๊ตฌ๊ฐ ๋ต.

- Generalization

  - Bias & Variance : ํ์ต์ด ๋๋ฌด ์๋๋ฉด ๋ฌธ์ . ๋๋ฌด ๋ง์ถค์ด์ด๋ ๋ฌธ์ . -> ealry stopping์ด ์ด๋ด ๋ ์ฐ์ธ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img02.PNG" alt="Bias & Variance"></p>

-
  - Train / Validation : ํ๋ จ ์ ์ค ์ผ๋ถ๋ฅผ ๊ฒ์ฆ ์์ผ๋ก ํ์ฉํ๊ธฐ(cf.K-fold). ํ์คํธ ์์ ๊ฑด๋๋ฆฌ์ง ์๋๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img03.PNG" alt="Train / Validation"></p>

-
  - Data Augmentation : ์ฃผ์ด์ง ๋ฐ์ดํฐ์ ์ผ์ด์ค ๋ค์ํ. ๋ฐค๊ณผ ๋ฎ, ๊ฐ๋, ์ฃผ๋ณ ํ๊ฒฝ ๋ฑ์ ๋ฐ์ํ ๋ฐ์ดํฐ. ๋ฌธ์ ๊ฐ ๋ง๋ค์ด์ง ๋ฐฐ๊ฒฝ๊ณผ ๋ชจ๋ธ์ ๋ถ์ํ์ฌ ๋์ถํ๊ธฐ. ๋ฒ์ฃผ๋ด์์ ์ต๋ํ ๋ค์ํ๊ฒ, ๋๋ฆฌ๊ธฐ, ์๋ฅด๊ธฐ, ์๊ณก, ํ๋ฐธ ๋ฑ.
  - torchvision.transforms : ์ ์ฉ.
  - ๋ชจ๋  ๊ณผ์ ์ ๋ชจ๋  ๋ฐ์ดํฐ์ ๋ฌด์กฐ๊ฑด ํตํ๋ ์์ฝ์ ์๋ค.

---

### Data Generation

- Data Feeding

  - ๋ชจ๋ธ์ ์ ํฉํ dataset์ ์๋ง๊ฒ ๋ฃ๊ธฐ. -> ํจ์จ ์ฆ๋.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img04.PNG" alt="Data Feeding"></p>

- Dataset & DataLoader

  - Dataset : VanillaData๋ฅผ Dataset์ผ๋ก ๋ณํ.
  - DataLoader : Dataset์ ํจ์จ์ ์ผ๋ก ์ฌ์ฉํ  ์ ์๋๋ก ๊ด๋ จ ๊ธฐ๋ฅ ์ถ๊ฐ. ๋ฐฐ์น ์ฌ์ด์ฆ, num workers, ์ฑ๋ ๋ฑ.
  - Dataset๊ณผ DataLoader๋ ๋ถ๋ฆฌ๋๋ ๊ฒ์ด ์ข๋ค. ์ฌํ์ฉ(์ฌ์ฉ)์ฑ์ ๋์ด๊ธฐ ์ํด. Dataset๋ Vanilla๋ฐ์ดํฐ๋ฅผ ์ํ๋ ํํ๋ก ์ถ๋ ฅํด์ฃผ๋ ํด๋์ค. DataLoader๋ Dataset์ ํจ์จ์ ์ฌ๋ฆฌ๋ ๊ฒ ๋ชฉ์ ์ธ ์ ํธ.

---

### ํต๊ณ์ ์ฐจํธ 4-1๊ฐ

- Seaborn ์๊ฐ

  - Seaborn : Matplotlib ๊ธฐ๋ฐ ํต๊ณ ์๊ฐํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ. Matplotlib ๊ธฐ๋ฐ์ด๋ผ Matplotlib์ผ๋ก ์ปค์คํ ๊ฐ๋ฅํ๋ฉฐ, ์ฌ์ด ๋ฌธ๋ฒ๊ณผ ๊น๋ํ ๋์์ธ์ด ํน์ง.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day16_img05.PNG" alt="Seaborn example"></p>

-
  - ๋ถ๋ฌ์ฌ ๋ ์ผ๋  sns๋ก(import seaborn as sns).
  - ์๊ฐํ์ ๋ชฉ์ ๊ณผ ๋ฐฉ๋ฒ์ ๋ฐ๋ผ API๋ฅผ ๋ถ๋ฅํ์ฌ ์ ๊ณต -> Categorical API, Distribution API, Relational API, Regression API, Multiples API, Theme API ๋ฑ.

# โ๏ธ Doodle

- ๊ฐ์๋ ๊ฐ๋จ, ์ค์ต์ ๋ธ๊ฐ๋จ. ๊ธฐ๋ณธ์ ์ผ๋ก ๋ค์ด๋ณธ ๋ด์ฉ๋ค์ด์ง๋ง ์๋ก ๊ตฌ์ฑํ๋ ๊ฑด ๋ ๋ค๋ฅธ ์ผ์ด๋ผ๋ ๊ฒ ์๋ฟ๋๋ค. ๋ํ์ฉ์ผ๋ก ์ฃผ์ด์ง ๋ฐ์ดํฐ๊ฐ ์ ๊ฐํ๋ค๊ณ  ์๊ฐํ๋๋ฐ(๋ฌผ๋ก  ๋น๊ต์  ์ ๊ฐํ์ง๋ง) ์๊ฐ๋ณด๋ค ๋ธ์ด์ฆ๊ฐ ๋ง๋ค. ๋ถ์์ ์ฌ๋ฐ์ด๋ ๋ด ์ฝ๋๊ฐ ์ค๋ฅ๋ง ๋ฑ์ผ๋ฉด ์ฌํ์ง. ์ฌ์ค ์๋ ์ธ์ ๋ ๊ทธ๋ฌ์ด. ์บก์คํค์ ๋ค์ ํ๋ ๋ง์์ผ๋ก ์งํํ๊ธฐ. ํ์๋ค์ด ๋ชจ๋ ์์ ๋๊ฐ์ ์ ๋ง ๋ค๊ธํ๊ณ  ๋์๋๋ค. ์คํ์ ๋ฏธ์์ ๋ฒ ์ด์ค ์ฝ๋๊ฐ ์ด๋ ธ๋๋ฐ, ๋ EDA ๋ดํฌ๋ฅผ ๋ฏ๊ณ  ๋์๋ง ๋งก์ ๊ฒฉ์ด์๋ค. ์๊ฐ์ ์์๋๋ฐ ํํ๋ก ๋จ์ ๊ฒ ๋ณ๋ก ์๋ ํ๋ฃจ. ๊ทธ๋ฆผ ๊ทธ๋ฆฌ๋ฌ ๊ฐ๊ณ  ์ถ๋ค. ์ค๋์ ๋์ ์ธ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Paul_Cezanne_1905_Still_Life_with_Apples_and_Peaches.jpg"></p>
<p align="center">Paul Cezanne, &ltStill Life with Apples and Peaches&gt, 1905. Oil on canvas, 81x100.5cm.</p>

- Day 16 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day15/Note.md "Day15 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day17/Note.md "Day17 Note")
