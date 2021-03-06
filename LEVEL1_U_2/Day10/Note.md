# ๐ Note

### Sequential Models - Transformer

- Transformer

  - ์ํ์ ๋ชจ๋ธ์ ์ ๋ค๋ฃจ๊ธฐ ์ด๋ ค์ธ๊น? ๊ฐ์ ๋ป์ด๋ผ๋ ์ด๋๊ฐ ์๋ฆฌ๊ฑฐ๋(Trimmed), ์ค๊ฐ์ ๋ญ๊ฐ ๋น ์ง๊ฑฐ๋(Omitted), ์์๊ฐ ๋ฐ๋ ์(Permuted)์๋ ๋ฐ, ์ด๋ฐ ๋ฐ์ดํฐ๋ ๋ค๋ฃจ๊ธฐ ์ด๋ ต๋ค.
  - ํธ๋์คํฌ๋จธ(Transformer)๋ attention ๊ตฌ์กฐ๋ฅผ ํ์ฉํ์ฌ ์ํ์ค๋ฅผ ๋ค๋ฃจ๋ ๋ชจ๋ธ. ์ฒซ ์์์ ๊ธฐ๊ณ์ด ๋ฒ์ญ์ด์๋ค. ํ์ฌ๋ ๋ค๋ฐฉ๋ฉด์์ ํ์ฉ์ค.
  - ์ด๋ค ๋ฌธ์ฅ(์ํ์ค)์ด ์ฃผ์ด์ง ๋ ๋ค๋ฅธ ๋ฌธ์ฅ(์ํ์ค)์ผ๋ก ๋ณ๊ฒฝ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img00.PNG" alt="Transformer"></p>

-
  - ์๋ ฅ ์ํ์ค, ์ถ๋ ฅ ์ํ์ค ๊ฐ์์ ๋๋ฉ์ธ์ด ๋ค๋ฅผ ์ ์๋ค.
  - RNN์ ๊ฒฝ์ฐ ๋ค์ด๊ฐ ๊ฐ์๋งํผ ์ฌ๊ท์ ์ผ๋ก ๋์ํ์ง๋ง Transformer๋ ํ ๋ฒ ๋์(encoder ๋จ).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img01.PNG" alt="Transformer"></p>

- Transformer - Encoders

  - ์ธ์ฝ๋ ๊ตฌ์กฐ : Self-Attention -> Feed Forward Neural Network -> Next Encoder
  - Self-Attention : ์ฃผ์ด์ง ์ธํ์ ๊ฐ๊ฐ์ ๋ฐ๋ฅธ ๋ฒกํฐ๊ฐ ์ฃผ์ด์ง ๋, ํ๋์ ๋ฒกํฐ ๋ฟ ์๋๋ผ ๋๋จธ์ง ๋ฒกํฐ๋ ๊ฐ์ด ๊ณ ๋ ค. ํน์  ๋จ์ด๊ฐ ๋ค๋ฅธ ๋จ์ด์ ์ด๋ค ๊ด๊ณ์ฑ์ด ์๋ ์ง ๊ณ ๋ คํ๋ ๊ฒ. ๋จ์ด๋ง๋ค ์ฃผ์ด์ง๋ ๋ฒกํฐ๋ 3๊ฐ(Queries, Keys, Values). ๊ฐ ๋จ์ด๊ฐ ์ฃผ์ด์ง ๋, ํ์ฌ ์ธ์ฝ๋ฉํ  ๋จ์ด์ Queries์ ๋๋จธ์ง ๋จ์ด์ Keys๋ฅผ ๋ด์ ํ์ฌ ์ ์ฌ๋๋ฅผ ๊ตฌํ๊ณ  Score ๋ฒกํฐ๋ฅผ ์์ฑํ์ฌ ๋ด๋๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img02.PNG" alt="Self-Attention"></p>

-
  - Score ๋ฒกํฐ๋ Keys(Queries ๋ฒกํฐ ์ฐจ์๊ณผ ๊ฐ๋ค) ๋ฒกํฐ์ ์ฐจ์์ ๋ฃจํธ๋ฅผ ์ทจํ ๊ฐ์ผ๋ก ๋๋๊ณ  Softmax๋ฅผ ๊ฑฐ์ณ Nomalize. ์ด๋ ๊ฒ ๋์จ ๊ฒ์ด attention rate. ์ต์ข์ ์ผ๋ก Value ๋ฒกํฐ์ weighted sum ํ์ฌ ์ต์ข๊ฐ์ ์ถ์ถ.
  - ํ๋ ฌ๋ก ํํํ๋ฉด ๋ค์๊ณผ ๊ฐ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img03.PNG" alt="Self-Attention in matrix"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img04.PNG" alt="Self-Attention in matrix"></p>

-
  - Multi-headed attention(MHA) : Attention์ ์ฌ๋ฌ ๋ฒ. ํ๋์ ์ธํ์ ๋ํด ์ฟผ๋ฆฌ, ํค, ๋ฐธ๋ฅ๋ฅผ ์ฌ๋ฌ ๊ฐ ์์ฑ. N๋ฒ ๋ฐ๋ณตํ๋ฉด N๊ฐ์ attention์ด ๋์ค๊ฒ ๋จ. ์ด ๋ ์ถ๋ ฅ ์ฐจ์์ ๋ง์ถ๊ธฐ ์ํ ํ์ฒ๋ฆฌ๋ก ํ๋ ฌ๊ณฑ ์ฌ์ฉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img05.PNG" alt="Transformer ์ฐจ์ ๋ง์ถ๊ธฐ"></p>

-
  - ์ธ์ฝ๋ฉ ๊ฐ ์์ฒด์ ์ํ์ ์ ๋ณด๋ ๋ค์ด๊ฐ ์์ง ์๋ค. ๊ฐ์ ๋จ์ด๊ฐ ๋ค๋ฅธ ์์๋ก ์ฃผ์ด์ง ๋ฌธ์ฅ์ด ๋ค๊ฐ๋คํด๋, ์ฃผ์ด์ง ์๋ ฅ์ด ๊ฐ๋ค๋ฉด ๊ฐ์ ๊ฐ์ด ๋์ค๋๊น. So, positional encoding ํ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img06.PNG" alt="Positional encoding"></p>

- Transformer - Decoders

  - ์ธ์ฝ๋๋ก๋ถํฐ ์ฒ๋ฆฌ๋ฅผ ๊ฑฐ์น ํค์ ๋ฐธ๋ฅ๊ฐ์ ์ ๋ฌ๋ฐ๋๋ค.
  - ๊ธฐ๋ณธ์ ์ผ๋ก ๋์ฝ๋์ ๋ฐ๋ ๊ณผ์ .
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img07.PNG" alt="Encoder and Decoder"></p>

-
  - Transformer๋ ๊ธฐ์กด์ ๋ฒ์ญ ๋ถ์ผ์์๋ง ํ์ฉ๋๋ค๊ฐ ์ต๊ทผ ์ด๋ฏธ์ง ๋ถ๋ฅ ๋ฑ ๋ค์ํ ๋ถ์ผ์์ ํ์ฉ ์ค. ๋น์ฐํ ๋ณํ์ ์ .

---

### Generative Models 1

- ๋จ์ํ ๋ชจ๋ธ ์์ฑ์ด ์ ๋ถ์ผ๊น?

  - Generation : sample ์์ฑ.
  - Density estimation : ๋ฎ์ ์ ๋(ํ๋ฅ ๊ฐ) ์ธก์ . ์ฆ, ๋จ์ ์์ฑ ๋ฟ ์๋๋ผ ๋ถ๋ฅ ๋ชจ๋ธ์ ํฌํจ.
  - Unsupervised representation learning : feature learning. ํน์ง์  ์ก๊ธฐ.

- Basic Discrete Distributions

  - ํ๋ฅ ๊ฐ์ ํํํ๋ ๋ฐ ํ์ํ ํ๋ผ๋ฏธํฐ๋ ์นดํ๊ณ ๋ฆฌ-1 ๊ฐ.
  - ๋์ ์ ์๋ฉด ํ๋ฅ ์ด p ๋ผ๋ฉด ๋ท๋ฉด์ p-1.
  - ์ฃผ์ฌ์ ํ๋ฅ ์ ํํํ  ๋๋ ํ์ํ ํ๋ผ๋ฏธํฐ๋ 5.
  - ๋ฐ์ด๋๋ฆฌ ๋ฐ์ดํฐ๋ง ๋ณด๋๋ผ๋ ํ์ํ ํ๋ผ๋ฏธํฐ๋ 2^n -1๊ฐ. ์ฆ, ๋๋ฌด ๋ง๋ค. ๋ง์ผ๋ฉด ํ์ต์ด ์ด๋ ค์. ์ด๊ฑธ ์ด๋ป๊ฒ ์ค์ผ๊น?
  - ๋ชจ๋  state๊ฐ ๋๋ฆฝ์ ์ด๋ผ ๊ฐ์ ํ๊ณ  ๊ทธ๋ฅ n์ผ๋ก ์ค์ฌ๋ฒ๋ฆฌ๊ธฐ -> ํ๋ผ๋ฏธํฐ๋ ์ค์ง๋ง ํํ๋ ฅ์ด ๋จ์ด์ง๋ค. ๊ทธ๋์ ๋ฑ์ฅํ๋ ๊ฒ ์ด ๋์ ์ค๊ฐ ์ด๋๊ฐ, Conditional Independence.

- Conditional Independence

  - ๋ ๊ฐ์ ํ์ ์  ์ด๋ก 
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img08.PNG" alt="Chain rule and Bayes' rule"></p>

-
  - ๊ฐ์ 
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img09.PNG" alt="Conditional Independence"></p>

-
  - Chain rule์ ํตํ๋ฉด ํ๋ผ๋ฏธํฐ๋ ์์ ๊ฐ์ด ์ฌ์ ์ด 2^n -1.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img10.PNG" alt="Chain rule ex."></p>

-
  - Markov assumption : ํ๋ผ๋ฏธํฐ๊ฐ ๋ฐ๋ก ์ง์ ์(i+1 ๋ฒ์งธ ํ๋ผ๋ฏธํฐ๊ฐ i๋ฒ์งธ ํฝ์์)๊ฒ๋ง dependentํ๋ค๋ ๊ฐ์ . ์ด ๊ฒฝ์ฐ ํ๋ผ๋ฏธํฐ๋ 2n -1 ๋ก ์ถ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img11.PNG" alt="Markov assumption"></p>

- Auto-regressive Model

  - ์ฒด์ธ๋ฃฐ๋ก ํ๋ผ๋ฏธํฐ๋ฅผ ํํ
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img12.PNG" alt="Auto-regressive Model"></p>

- NADE(Neural Autoregressive Density Estimator)

  - ์๋ ฅ ์ฐจ์์ด ๋ฌ๋ผ์ง์ ๋ฐ๋ผ weight์ด ๋ฐ๋๋ Neural Network + n๋ฒ์งธ ํ๋ผ๋ฏธํฐ๋ฅผ ์ํด n-1๋ฒ์งธ ํ๋ผ๋ฏธํฐ ์ ๋ณด๋ง ํ์ํ Autoregressive.
  - NADE๋ ๋จ์ํ generation๋ง ์ํํ  ๋ฟ ์๋๋ผ ์์์ ์ธํ์ ๋ํ density๋ฅผ ๊ณ์ฐํ  ์ ์๋ค.(explicit model)
  - Continuous Random Variables ์ ๊ฒฝ์ฐ ๋ง์ง๋ง์ Gaussian mixture model ํ์ฉ.

- Pixel RNN

  - RNN +  Autoregressive.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img13.PNG" alt="Pixel RNN example"></p>

-
  - ordering์ ๋ฐ๋ผ Row LSTM(์๋จ ์ ๋ณด๋ง์ ํ์ฉ), Diagonal BiLSTM(์์ธก์ ์ด์  ์ ๋ณด๋ฅผ ๋ค ํ์ฉํ RNN)
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day10_img14.PNG" alt="Row LSTM and Diagonal BiLSTM"></p>


# โ๏ธ Doodle

- ๋ ๋ฒ์งธ ์ฃผ์ ๋ง์ง๋ง ๋ . ์๊ฐ์ด ๋น ๋ฅด๊ฒ ๊ฐ๋ค. ์ถ๊ทผํ  ๋ ์ ๊ทธ๋ฌ๋๋ฐ. ์ฌ๋ฐ๋ ์๊ฐ๋ง ๋นจ๋ฆฌ ๊ฐ๋ ๊ฒ ์๋๋ผ ์ํ ๋ชฉํ๊ฐ ๋ง์ ๋ ๋ ์๊ฐ์ด ๋นจ๋ฆฌ ๊ฐ๋ค. ๋ชฉํ์น๋งํผ ๋ฌ์ฑํ๋๋์ ๋ต๋ณํ๋ค๋ฉด '๊ทธ๋ ์ง ์๋ค'์ง๋ง ์ถฉ๋ถํ ๋ง์กฑ์ ํ๋ค. ๋ค๋ง ๋๋๊ฐ ์ด๋ ต๊ณ  ๊ณต๋ถ๋์ด ๋ถ์กฑํ์ผ๋ ์ฃผ๋ง์ ์ถค์ถ๊ธฐ๋ ๊ธ๋ ๋ค. ์ค๋์ ๋์ ๋ง๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Edouard_Manet_1863_Luncheon_on_the_Grass.jpg"></p>
<p align="center">Edouard Manet, &ltLuncheon on the Grass&gt, 1863. Oil on canvas, 208x264.5cm.</p>

- Day 10 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day9/Note.md "Day9 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day11/Note.md "Day11 Note")
