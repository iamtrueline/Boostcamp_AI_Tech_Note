## ๐ AI Math 9๊ฐ ํด์ฆ - CNN ์ฒซ๊ฑธ์ 1~5

### 1. ๋ค์ ๋ณด๊ธฐ ์ค, ์ฐ์์ ์ธ ๋ณ์์ ๋ํ ํจ์ f, g์ฌ์ด์ convolution์ ๋ํ๋ด๋ ์์์ผ๋ก ๊ฐ์ฅ ์ ์ ํ ๊ฒ์ ๊ณ ๋ฅด์์ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img15.PNG" alt="๋ณด๊ธฐ"></p>

- ๋ต : 3
- ํด์ค : ์ฐ์์ ์ธ ๋ณ์์ ๋ํ ํจ์๋ 3๋ฒ์ด๋ค.

### 2. ์๋ ฅ ๋ฒกํฐ x ์ ๊ฐ์ค์น ๋ฒกํฐ V๊ฐ ๋ค์๊ณผ ๊ฐ์ด ์ฃผ์ด์ง ๋, ๋ค์ ๋ณด๊ธฐ ์ค ์ฌ๋ฐ๋ฅธ h๋ฅผ ๊ณ ๋ฅด์์ค. ์ด ๋, k๋ V์ ์ฌ์ด์ฆ์ด๊ณ , ์ธ๋ฑ์ค๋ 1๋ถํฐ ์์ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img16.PNG" alt="๋ณด๊ธฐ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img17.PNG" alt="๋ณด๊ธฐ"></p>

- ๋ต : 1
- ํด์ค : ์ฃผ์ด์ง ์๋๋ก ์ ๊ฐํ๋ฉด h๋ 1๋ฒ์ด๋ค.

### 3. ๋ฒกํฐ x์ h๊ฐ ๋ค์๊ณผ ๊ฐ์ด ์ฃผ์ด์ง ๋, y1๊ฐ์ ๊ตฌํ์์ค. m์ h์ ์์์ ๊ฐ์์ด๊ณ , ์ธ๋ฑ์ค๋ 1๋ถํฐ ์์ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img18.PNG" alt="๋ณด๊ธฐ"></p>

- ๋ต : 14
- ํด์ค : y1 = x1 X h1 + x2 X h2 = 14

### 4. ์๋ ฅ ํ๋ ฌ X์ ์ปค๋ K๊ฐ ๋ค์๊ณผ ๊ฐ์ด ์ฃผ์ด์ง ๋,  Y(1,2)๊ฐ์ ๊ตฌํ์์ค.  m์ K์ ํ ์ฌ์ด์ฆ,  n ์ K์ ์ด ์ฌ์ด์ฆ์ด๊ณ , ์ธ๋ฑ์ค๋ 1๋ถํฐ ์์ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img19.PNG" alt="๋ณด๊ธฐ"></p>

- ๋ต : 5
- ํด์ค : Y(1,2) = K(1,1)*X(1,2) + K(1,2)*X(1,3) + K(2,1)*X(2,2) + K(2,2)X(2,3) = 0 + 2 + 3 + 0 = 5

### 5. ์๋ ฅ ํ๋ ฌ X์ ์ปค๋ K๊ฐ ๋ค์๊ณผ ๊ฐ์ด ์ฃผ์ด์ง ๋, Y(2,2) + Y(3,3)๊ฐ์ ๊ตฌํ์์ค. m์ K์ ํ ์ฌ์ด์ฆ,  n์ K์ ์ด ์ฌ์ด์ฆ์ด๊ณ , ์ธ๋ฑ์ค๋ 1๋ถํฐ ์์ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day03_img20.PNG" alt="๋ณด๊ธฐ"></p>

- ๋ต : 9
- ํด์ค : Y(2,2) + Y(3,3) = (1 + 3) + (3 + 4 - 2) = 9
