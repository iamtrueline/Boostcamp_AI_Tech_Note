# ๐ Note

### Numpy ๊ธฐ์ด :: [๊ธฐ์ด ๋ณต์ต] Python Basics for AI 6๊ฐ

- numpy

  - ํ๋ ฌ์ด๋ ๋๊ท๋ชจ ๋ค์ฐจ์ ๋ฐฐ์ด์ ์ฝ๊ฒ ์ฒ๋ฆฌํ  ์ ์๋๋ก ์ง์ํ๋ ํ์ด์ฌ์ ๊ณ ์ฑ๋ฅ ๊ณผํ ๊ณ์ฐ์ฉ ํจํค์ง. ์ด๋ฆ์ Numerical Python์ ์ฝ์.
  - Matrix์ Vector์ ๊ฐ์ Array ์ฐ์ฐ์ ์ฌ์ค์ ํ์ค.
  - ํ์ด์ฌ์ ์ธํฐํ๋ฆฌํฐ ์ธ์ด์ด๋ฏ๋ก ํฐ ๋งคํธ๋ฆญ์ค์ ๋ํ ๋น ๋ฅธ ์ฒ๋ฆฌ ์๋๋ฅผ ์ํด ์ ์ ํ ํจํค์ง ์ฌ์ฉ ๊ถ์ฅ.
  - ์ผ๋ฐ ๋ฆฌ์คํธ์ ๋นํด ๋น ๋ฅด๊ณ  ๋ฉ๋ชจ๋ฆฌ ํจ์จ์ .
  - ๋ฐ๋ณต๋ฌธ ์์ด ๋ฐ์ดํฐ ๋ฐฐ์ด์ ๋ํ ์ฒ๋ฆฌ ์ง์.
  - ์ ํ๋์์ ๊ด๋ จ๋ ๋ค์ํ ๊ธฐ๋ฅ ์ ๊ณต.

- ndarray

  - np.array ๋ก ์ ์ธ.
  - ํ๋์ ๋ฐ์ดํฐ ํ์๋ง ๋ฐฐ์ด์ ๋ฃ์ ์ ์๋ค. ๋ค์ด๋๋ฏน ํ์ดํ ์ง์ ์ ๋จ.
  - C์ Array๋ฅผ ์ฌ์ฉํ์ฌ ๋ฐฐ์ด ์์ฑ.
  - dtype : ๋ฐฐ์ด ์ ์ฒด์ ๋ฐ์ดํฐ ํ์ ๋ฐํ.
  - shape : ๋ฐฐ์ด์ ์ฐจ์ ๊ตฌ์ฑ์ ๋ฐํ. 0 = scalar, 1 = vector, 2 = matrix, 3 = 3-tensor, n = n-tensor
  - ndim : ์ฐจ์ ์ ๋ฐํ.
  - size : ๋ฐ์ดํฐ์ ๊ฐ์ ๋ฐํ.

- Handling shape

  - reshape : Array(๋ฐฐ์ด)์ shape(์ฐจ์ ๊ตฌ์ฑ)์ ํฌ๊ธฐ ๋ณ๊ฒฝ. element(์์)์ ๊ฐ์์ ์์๋ ๋์ผ. -1์ ๋๋จธ์ง ๊ฐ์ ๋ง์ถฐ ์๋ ์ ๋ ฌ.
  - flatten : ๋ค์ฐจ์ Array๋ฅผ 1์ฐจ์์ผ๋ก ๋ณ๊ฒฝ.

- Indexing & Slicing

  - ์ด์ฐจ์ ๋ฐฐ์ด์์ [n, m] ํ๊ธฐ๋ฒ ์ ๊ณต. ์์ row, ๋ค๋ col.
  - ํ๊ณผ ์ด์ ๋๋ ์ slicing ๊ฐ๋ฅ. Matrix์ ๋ถ๋ถ์งํฉ ์ถ์ถ์ ์ ์ฉํ๋ค.

- Creation function

  - arange : Array์ ๋ฒ์๋ฅผ ์ง์ ํ์ฌ ๊ฐ์ ๋ฆฌ์คํธ ์์ฑ.
  - zeros : 0์ผ๋ก ์ฐฌ ndarray ์์ฑ.
  - ones : 1๋ก ์ฐฌ ndarray ์์ฑ.
  - empty : ๋น์ด์๋ ndarray ์์ฑ. ๋ฉ๋ชจ๋ฆฌ ์ด๊ธฐํ๋ ๋์ง ์์.
  - identity : ๋จ์ ํ๋ ฌ ์์ฑ.
  - eye : ์์์ ์ ์ ํ ์ํ๋ก ๋๊ฐ์ ์ด 1์ธ ํ๋ ฌ ์์ฑ.
  - diag : ๋๊ฐํ๋ ฌ์ ๊ฐ์ ์ถ์ถ.
  - random sampling : ๋ฐ์ดํฐ ๋ถํฌ์ ๋ฐ๋ฅธ ์ํ๋ง์ผ๋ก Array๋ฅผ ์์ฑ.

- Operation function

  - sum : ์์ฑ๊ฐ ๋ํ๊ธฐ.
  - axis : ๋ชจ๋  Operation function์ ์คํํ  ๋ ๊ธฐ์ค์ด ๋๋ ์ฐจ์์ถ.
  - mean : ์์ฑ๊ฐ ํ๊ท .
  - std :  ์์ฑ๊ฐ ํ์ค ํธ์ฐจ.
  - concatenate : numpy array๋ฅผ ๋ถ์ด๋ ํจ๊ตฌ. vstack = ๋ฐฐ์ด์ ์ธ๋ก๋ก ๊ฒฐํฉ, hstack = ๋ฐฐ์ด์ ๊ฐ๋ก๋ก ๊ฒฐํฉ ๋ฑ.

- Araay operations

  - numpy๋ array๊ฐ ๊ธฐ๋ณธ์ ์ธ ์ฌ์น ์ฐ์ฐ์ ์ง์ํจ.
  - dot : ํ๋ ฌ ๊ธฐ๋ณธ ์ฐ์ฐ. Dot product.
  - transpose, T : ์ ์นํ๋ ฌ.
  - Shape์ด ๋ค๋ฅธ ๋ฐฐ์ด ๊ฐ ์ฐ์ฐ ์ง์. broadcasting. Scalar-Vector ๋ฟ ์๋๋ผ Vector-Matrix ์ฐ์ฐ๋ ์ง์.
  - timeit: ์ฃผํผํฐ ํ๊ฒฝ์์ ์ฝ๋์ ํผํฌ๋จผ์ค ์ฒดํฌ ํจ์.
  - ์ผ๋ฐ์ ์ผ๋ก for loop < list comprehension < numpy ๋ก ๊ฐ์๋ก ์๋๊ฐ ๋น ๋ฅด๋ค. 1์ต ๋ฒ loop ๋ ๋ ์ฝ 4๋ฐฐ ์ด์ ์ฑ๋ฅ ์ฐจ์ด.
  - ๊ทธ๋ฅ ํ ๋น์์๋ ์ฐ์ฐ ์๋ ์ฐจ์ด ์์.

- Comparisons

  - any : ํ๋๋ผ๋ ์กฐ๊ฑด์ ๋ง์กฑํ๋ค๋ฉด True
  - all : ๋ชจ๋๊ฐ ์กฐ๊ฑด์ ๋ง์กฑํ๋ค๋ฉด True
  - numpy๋ ๋ฐฐ์ด์ ํฌ๊ธฐ๊ฐ ๋์ผํ  ๋ ์์ ๊ฐ ๋น๊ต ๊ฒฐ๊ณผ๋ฅผ T/F๋ก ๋ฐํ.
  - logical_and, logical_not, logical_or ๋ฑ.
  - np.where ์ ๋ก ์กฐ๊ฑด์ ๋ง์กฑํ๋ ๊ฐ๋ง ์ถ์ถ ๊ฐ๋ฅ.
  - argmax & argmin : Array ๋ด ์ต๋๊ฐ ๋๋ ์ต์๊ฐ์ ์ธ๋ฑ์ค ๋ฐํ. axis ๊ธฐ๋ฐ ๋ฐํ ๊ฐ๋ฅ.

- boolean & fancy index

  - boolean index : ํน์  ์กฐ๊ฑด์ ๋ฐ๋ฅธ ๊ฐ์ ๋ฐฐ์ด ํํ๋ก ์ถ์ถ. ๋น๊ต ์ฐํ ํจ์๋ค์ ๋ชจ๋ ์ด์ฉ ๊ฐ๋ฅ.
  - fancy index : array๋ฅผ index value๋ฅผ ์ฌ์ฉํด์ ๊ฐ์ ์ถ์ถํ๋ ๋ฐฉ๋ฒ. a[b]์ a.take(b)๋ ๋์ผํ ๋์. ๋งคํธ๋ฆญ์ค ํํ๋ ์ ์ฉ ๊ฐ๋ฅ.

- numpy data I/O

  - loadtxt & savetxt : text ๋ฐ์ดํฐ๋ฅผ ์ฝ๊ณ  ์ ์ฅํ๋ ๊ธฐ๋ฅ.

---

### Pandas ๊ธฐ์ด :: [๊ธฐ์ด ๋ณต์ต] Python Basics for AI 7-1 ~ 7-2๊ฐ

- Pandas

  - ๊ตฌ์กฐํ๋ ๋ฐ์ดํฐ์ ์ฒ๋ฆฌ๋ฅผ ์ง์ํ๋ ํ์ด์ฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ. ํ์ด์ฌ๊ณ์ ์์. ์ด๋ฆ์ Panel Data์ ์ฝ์.
  - numpy์ ๊ฒฐํฉํ์ฌ ๊ฐ๋ ฅํ ์คํ๋ ๋์ํธ ์ฒ๋ฆฌ ๊ธฐ๋ฅ ์ ๊ณต.
  - ์ธ๋ฑ์ฑ, ์ฐ์ฐ์ฉ ํจ์, ์ ์ฒ๋ฆฌ ํจ์ ์ ๊ณต.
  - ๋ฐ์ดํฐ ์ฒ๋ฆฌ ๋ฐ ํต๊ณ ๋ถ์์ ์ํด ์ฌ์ฉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day05_img00.PNG" alt=""></p>

- ๊ธฐ๋ณธ ํ์ฉ

  - Series : DataFrame ์ค ํ๋์ Column์ ํด๋นํ๋ ๋ฐ์ดํฐ์ ๋ชจ์ Object.
  - DataFrame : Data Table ์ ์ฒด๋ฅผ ํฌํจํ๋ Object. numpy Array์ ๋น์ทํ๋ ๊ฐ Column์ด ๋ค๋ฅธ ํ์์ ์ ๋ณด๋ฅผ ๋ด์ ์ ์๋ค.
  - Series๋ฅผ ๋ชจ์์ ๋ง๋  Data Table = ๊ธฐ๋ณธ 2์ฐจ์.
  - Selection & Drop : ๊ธฐ๋ณธ ์ธ๋ฑ์ค ์๋ ์๊ณผ ๋ค๋ฅด์ง ์์. Drop์ .drop์ผ๋ก.

- Dataframe operations

  - ์ธ๋ฑ์ค ๊ธฐ์ค์ผ๋ก ์ฐ์ฐ ์ํ. ๊ฒน์น๋ ์ธ๋ฑ์ค๊ฐ ์์๊ฒฝ์ฐ NaN ๊ฐ์ผ๋ก ๋ฐํ.
  - Operation types : add, sub, div, mul

- lambda, map, apply

  - series type์ ๋ฐ์ดํฐ์๋ ํ์ด์ฌ์ map ํจ์ ์ฌ์ฉ๊ฐ๋ฅ.
  - function ๋์  dict, sequenceํ ์๋ฃ ๋ฑ์ผ๋ก ๋์ฒด ๊ฐ๋ฅ. ์๋ ๊ฐ์ NaN.
  - replace : Map ํจ์์ ๊ธฐ๋ฅ์ค ๋ฐ์ดํฐ ๋ณํ ๊ธฐ๋ฅ๋ง ๋ด๋น. ๋ฐ์ดํฐ ๋ณํ์ ๋ง์ด ์ฌ์ฉ.
  - apply : map๊ณผ ๋ฌ๋ฆฌ, series ์ ์ฒด(column)์ ํด๋น ํจ์๋ฅผ ์ ์ฉ. ์๋ ฅ๊ฐ์ด series ๋ฐ์ดํฐ๋ก ์๋ ฅ๋ฐ์ handling ๊ฐ๋ฅํ๋ฉฐ ๋ด์ฅ ์ฐ์ฐ ํจ์ ์ฌ์ฉ ์์๋ ๋์ผ. mean, std ์ง์. scalar ๊ฐ ์ด์ธ์ series๊ฐ์ ๋ฐํ๋ ๊ฐ๋ฅํ๋ค.

- ํ๋ค์ค ๋นํธ์ธ functions

  - describe : Numeric type ๋ฐ์ดํฐ์ ์์ฝ ์ ๋ณด๋ฅผ ๋ณด์ฌ์ค.
  - unique : series data์ ์ ์ผํ ๊ฐ์ list๋ฅผ ๋ฐํ.
  - sum : ๊ธฐ๋ณธ์ ์ธ ์ฐ์ฐ ์ง์. ์ด ์ธ sub, mean, min, max, conut, median, mad, var ๋ฑ ๋์ผ.
  - isnull : NaN ๊ฐ์ด ์ธ๋ฑ์ค ๋ฐํ.
  - sort_values : column ๊ฐ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌ.
  - Correlation(corr) & Covariance(cov) : ์๊ด๊ณ์์ ๊ณต๋ถ์ฐ ๋ฐํ.

- Groupby

  - split > apply > combine์ ๊ฑฐ์น๋ group ์ฐ์ฐ.
  - ํ ๊ฐ์ด์์ column์ ๋ฌถ์ ์ ์์.
  - Groupby ๋ช๋ น์ ๊ฒฐ๊ณผ๋ฌผ๋ ๊ฒฐ๊ตญ์ dataframe์ด๋ฏ๋ก ๋ ๊ฐ์ column์ผ๋ก groupby๋ฅผ ํ  ๊ฒฝ์ฐ, index๊ฐ ๋ ๊ฐ ์์ฑ.
  - unstack() : Group์ผ๋ก ๋ฌถ์ธ ๋ฐ์ดํฐ๋ฅผ matrix ํํ๋ก ์ ํ.
  - swaplevel() : Index level์ ๋ณ๊ฒฝ.
  - Index level ์ ๊ธฐ์ค์ผ๋ก ๊ธฐ๋ณธ ์ฐ์ฐ ์ํ ๊ฐ๋ฅ.
  - grouped : Groupby์ ์ํด Split๋ ์ํ๋ฅผ ์ถ์ถ. ํน์  key๊ฐ์ ๊ฐ์ง ๊ทธ๋ฃน์ ์ ๋ณด๋ง ์ถ์ถํ๋ ๊ฒ๋ ๊ฐ๋ฅ. ์ถ์ถ๋ ๊ทธ๋ฃน ์ ๋ณด์ Aggregation, Transformation, Filtration ์ด๋ ๊ฒ ์ธ ๊ฐ์ง ์ ํ์ apply๊ฐ ๊ฐ๋ฅํ๊ณ  ๊ฐ ๊ธฐ๋ฅ์ ์์ฝ ํต๊ณ์ ๋ณด, ํด๋น ์ ๋ณด ๋ณํ(์์ฝ ์ ๋ณด ์๋, ๊ฐ๋ณ ๋ฐ์ดํฐ ๋ณํ ์ง์), ํน์  ์ ๋ณด ์ ๊ฑฐ(ํํฐ๋ง, boolean ์กฐ๊ฑด ํ์).

- Pivot table & Crosstab

  - Pivot table : ์์ ํ ํํ.
  - Crosstab : Pivot table์ ํน์ ํํ. ๋ ์นผ๋ผ์ ๊ต์ฐจ ๋น๋, ๋น์จ, ๋ง์ ๋ฑ์ ๊ตฌํ  ๋ ์ฌ์ฉ.

- Merge & Concat

  - Merge : ๊ณ ์ ๊ฐ ๊ธฐ์ค์ผ๋ก ๋ ๋ฐ์ดํฐ๋ฅผ ํ๋๋ก ํฉ์นจ. like join in SQL.
  - Concat : ๊ฐ์ ํํ์ ๋ฐ์ดํฐ๋ฅผ ๋จ์ํ ํฉ์นจ.

- Persistence

  - Database connection : Data loading์ db connection ๊ธฐ๋ฅ์ ์ ๊ณต.
  - XLS persistence : Dataframe์ ์์ ์ถ์ถ ์ฝ๋.
  - Pickle persistence : ๊ฐ์ฅ ์ผ๋ฐ์ ์ธ ํ์ด์ฌ ํ์ผ persistence.

# โ๏ธ Doodle

- ์ฒซ ์ฃผ์ ๋ง๋ฌด๋ฆฌ. ๋จ์ ์๊ฐ์ ๋ฏธ๋ฆฌ ๋ค์๋ ๊ฐ์์ ๋ณต์ต, ์ ํ ๊ณผ์  ์์ฑ. ์ฃผ๋ง์ ์ฐธ๊ณ  ์ฝ๋์ ์ฐธ์กฐ ๊ฐ์๋ค์ ๋ฆฌ๋ทฐํ  ์์ . ์์ผ๋ก์ ํ์ต๋์ ์ด์ ๋น์ทํ๊ฑฐ๋ ๋์ด๋ ๊ฑฐ๋ผ๊ณ  ํ๋ค. ์ค๊ฐ ๊ธฐ๋ง ์ํ์ ์์ง๋ง ์ ์ฌํ ๋ํ๊ฐ ์์ด์ ์ฌ์ ๋ถ๋ฆด ์๊ฐ์ด ์๋ค. ์ผ๋จ ๊ธ์์ผ์ ์ด๋ฅด๊ฒ ๋ง์น๊ธฐ. ์ค๋์ ๋์ ๊ณ ํ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Vincent_van_Gogh_1890_Wheat_Field_with_Crows.jpg"></p>
<p align="center">Vincent van Gogh, &ltWheat Field with Crows&gt, 1890. Oil on canvas, 50.2x103cm.</p>

- Day 5 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_1/Day4/Note.md "Day4 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day6/Note.md "Day6 Note")
