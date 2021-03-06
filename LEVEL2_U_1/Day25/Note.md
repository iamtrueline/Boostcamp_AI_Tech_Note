# ๐ Note

### Intro to NLP, Bag-of-Words

- ์์ฐ์ด ์ฒ๋ฆฌ

  - ์์ฐ์ด ์ฒ๋ฆฌ : ํฌ๊ฒ ์ปดํจํฐ๊ฐ ์ฃผ์ด์ง ๋จ์ด๋ ๋ฌธ์ฅ, ๋ฌธ๋จ ๋ฑ ๊ธ์ ์ดํดํ๋ ๊ณผ์ ๊ณผ ์์ฑํ๋ ๊ณผ์  ๋๊ฐ์ง๋ก ๋ถ๋ฅ.
  - ์ต์  ๊ธฐ์ ์ ACL, EMNLP, NAACL ๋ฑ์์ ๋ฐํ.
  - Low-level parsing : ์ฃผ์ด์ง ๋ฌธ์ฅ์ ๋จ์ด ๋จ์๋ก ์ชผ๊ฐ๊ณ (Tokenization), ์ด๋ฏธ ๋ณํ๋ฑ์ ์์ค ์ด๊ทผ์ ์ถ์ถ(stemming).
  - Word and parase level : ๊ณ ์ ๋ช์ฌ๋ฅผ ๊ฐ๋ฆฌ๋ Named entity recognition(NER), ํ์ฌ๋ฅผ ํ๋จํ๋ Part of speech(POS) ๋ฑ.
  - Sentence level : ๊ธ์  ๋ถ์  ์ด์กฐ ๋ถ๋ฅ, ๊ธฐ๊ณ ๋ฒ์ญ ๋ฑ.
  - Multi-sentence and paragraph level : ๋ ๋ฌธ์ฅ๊ฐ ๋ผ๋ฆฌ ํ๋จ, ์ง๋ต, ๋ํ ์์คํ, ์์ฝ ๋ฑ.
  - ์ง๋ต ๊ณผ์ ์ ๊ด๋ จํ์ฌ ์๋ฅผ ๋ค๋ฉด, ๊ฒ์ ์์คํ์ ๊ฒฝ์ฐ ์ด์  ๊ฒ์์ด๋ฅผ ๋ฆฌ์คํธ๋ก ๋์ดํ  ๋ฟ ์๋๋ผ ์ง๋ฌธ์ ๋ํ ์์ง๋ฅผ ํ๋จํ๊ณ  ์ต์๋จ์ ๋ต๋ณ์ ๋ฐ๋ก ๋ฌ์์ค๋ค.
  - Text mining : ๊ธด ๊ธฐ๊ฐ์ ๊ธฐ์ฌ๋ค์ ๋ชจ์ ํค์๋ ๋ฐ ๋ฐ์ดํฐ๋ฅผ ๋ถ์ํ๊ณ  ํธ๋ ๋๋ฅผ ๋ถ์. ์ํ ๋ฐ์ ๋ถ์. ์์ ๊ด๊ณ๋ ์ฌํ ๋ฐ์ ๋ถ์ ๋ฑ. ํน์  ๋ถ์ผ์ ๋ํ ํ์คํธ, ๋ฌธ์๋ฅผ ๊ตฐ์งํํด์ ๋ถ์ํ๋ค. KDD, WebConf(WWW), WSDM, CIKM, ICWSM๋ฑ์์ ์ต์  ๋ํฅ ๋ฐํ.
  - Information retreval : ๊ฒ์ ์ฑ๋ฅ ๊ณ ๋ํ. ๊ฒ์ ๊ธฐ์ ์ ์ด๋ ์ ๋ ์ฑ์ํ ์ํ์ ์ด๋ฅด๋ ๋ค๊ณ  ๋ณธ๋ค. ์ถ์ฒ์์คํ์ด ์ด ์์ญ. SIGIR, WSDM, CIKM, RecSys๋ฑ์์ ์ต์  ๋ํฅ ๋ฐํ.

- ์์ฐ์ด ์ฒ๋ฆฌ ๋ํฅ

  - Word2Vec, Glove๋ฅผ ํตํด ํ์คํธ ์ํ์ค ๋ด ๋จ์ด๋ฅผ ํน์  ์ฐจ์ ๋ฒกํฐ๋ก ์๋ฒ ๋ฉ. ์ด ๋ ์ํ์ค๋ ์์ ์ ๋ณด๋ฅผ ํฌํจํ๋ค.
  - ์ํ์ค ์ฒ๋ฆฌ์ ํนํ๋ RNN ๋ชจ๋ธ(LSTM, GRU)์ด ์์ฐ์ด ์ฒ๋ฆฌ์ ํต์ฌ ๋ชจ๋ธ๋ก ์๋ฆฌ์ก์.
  - Transformer ๋ชจ๋ธ ๋ฑ์ฅ(Attention is all you need). ํฐ ์ฑ๋ฅ ํฅ์ ์ด๋ฃฉ. ํ์ฌ ๋๋ถ๋ถ ์ด ๋ชจ๋ธ์ ์ฑํํ๋ค. Transformer๋ ์์ฐ์ด ๋ฟ ์๋๋ผ, ์์, ์๊ณ์ด ์์ธก ๋ฑ์๋ ๋ค์ํ๊ฒ ์ฌ์ฉ๋จ.
  - Transformer๋ฅผ ํฌํจํ ๋๋ถ๋ถ์ ๊ณ ๊ธ NLP ๋ชจ๋ธ์ ์๋ ๊ธฐ๊ณ ๋ฒ์ญ ์์์ ๊ฐ์ ํ๊ธฐ ์ํด์ ๊ฐ๋ฐ๋์๋ค.
  - ์ด์ ์ NLP ํ์คํฌ๋ง๋ค ๋ถ๋ฆฌ๋ ๋ง์ถคํ ๋ชจ๋ธ์ด ์์๋ค. ํ์ฌ๋ ๋ฒ์ฉ ์ฌ์ ํ์ต๋ชจ๋ธ์ ์ ์ดํ์ต ์ํค๋ ๋ฑ์ผ๋ก ์ฌ์ฉํ๋ค. ๊ธฐ์กด์ ๋ง์ถค ๋ชจ๋ธ๋ณด๋ค๋ ์๋ฑํด์ง ์ฑ๋ฅ์ ๋ณด์ฌ์ค.
  - ์๊ฐ์ง๋ํ์ต(self-supervised training) : ์ ํ์ ์ธ ์ธ๊ณต์ง๋ฅ์์ ๋ฒ์ฉ์ผ๋ก ๋์ค๋ ๋ฐ ๊ธฐ์ฌํ ๋ฐฉ๋ฒ.
  - ํ์ต์ ๋์ด ํ์ํ๋ค. ๊ทธ๋์ ํฐ ๊ธฐ์์ด ์ฃผ์ถ.

- Bag-of-Words

  - Step 1 : ์ฃผ์ด์ง ๋ฌธ์์์ ์ชผ๊ฐ  ๋จ์ด๋ค ์ค ์ค๋ณต์ ์ ๊ฑฐํ๊ณ  ๋์ดํ๊ธฐ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img00.PNG" alt="Bag-of-Words"></p>

-
  - Step 2 : ๋์ด๋ ๋จ์ด๋ฅผ Categorical variable๋ก ๋ณด๊ณ  ๊ฐ๊ฐ ์ํซ๋ฒกํฐ๋ก ํํ. ์ด ๋ ๋ชจ๋  ๋จ์ด์์ ์ ํด๋ฆฌ๋์ ๊ฑฐ๋ฆฌ๋ ๋ฃจํธ2. ์ ์ฌ๋๋ 0.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img01.PNG" alt="Bag-of-Words"></p>

-
  - Step 3 : ์ดํ ํ๋จํ  ๋ฌธ์ฅ๋ค์ ์ด ์ํซ๋ฒกํฐ๋ฅผ ๋ํ ํํ๋ก ํํ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img02.PNG" alt="Bag-of-Words"></p>

-
  - ์ด๋ ๊ฒ ๋ฌธ์ฅ(๋ฒกํฐ)์ ์นดํ๊ณ ๋ฆฌ๋ฅผ ํ๋จํ๋ ๊ฒ์ Classifier์ ๋ชซ.

- NaiveBayes Classifier for Document Classification

  - ํน์  ๋ฌธ์ d๊ฐ C๊ฐ ๊ฐ๊ฐ ํด๋์ค์ ์ํ  ํ๋ฅ  ๋ถํฌ๋ P(c|d).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img03.PNG" alt="NaiveBayes Classifier"></p>

-
  - ๊ฐ ๋จ์ด(w)๊ฐ ๋ํ๋  ํ๋ฅ ์ด ๋๋ฆฝ์ด๋ผ๋ฉด ๋ค์ ์์ผ๋ก๋ ํํ ๊ฐ๋ฅ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img04.PNG" alt="NaiveBayes Classifier"></p>

-
  - ์์ . CV ์นดํ๊ณ ๋ฆฌ ๋ฌธ์ 2๊ฐ, NLP ์นดํ๊ณ ๋ฆฌ ๋ฌธ์ 2๊ฐ. ์๋ก ๋ค์ด์จ ๋ฌธ์๋ ์ด๋ ์นดํ๊ณ ๋ฆฌ์ผ๊น?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img05.PNG" alt="NaiveBayes Classifier"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img06.PNG" alt="NaiveBayes Classifier"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img07.PNG" alt="NaiveBayes Classifier"></p>

  - NaiveBayes Classifier๋ train์ ํน์  ๋จ์ด๊ฐ ํฌํจ๋์ง ์๋๋ค๋ฉด ํ๋ฅ ๊ฐ์ 0. ๋ฐ๋ผ์ ํ์ต๋์ง ์์ ๋จ์ด๊ฐ ๋ฑ์ฅํ  ๋ ํด๋น ๋ฌธ์๊ฐ ์ค๋ น ์ด๋ฏธ ํ์ต๋ ์นดํ๊ณ ๋ฆฌ์ ์ํ๋๋ผ๋(์ ์ฌ๋๊ฐ ๋๋๋ผ๋) ๋ถ๋ฅ๋ฅผ ์ ํํ๊ฒ ํด๋ผ ์ ์๋ค.

### Word Embedding

- Word Embedding

  - Word Embedding : ์์ฐ์ด์ ๋จ์ด๋ฅผ ์ ๋ณด์ ๊ธฐ๋ณธ๋จ์๋ก ์ฑ์ ํ๊ณ  ๊ฐ ๋จ์ด๋ฅผ ํน์  ์ฐจ์ ๋ฒกํฐ๋ก ๋ณํ.
  - ๊ธฐ๋ณธ ์์ด๋์ด๋ ๋น์ทํ ๋จ์ด๋ ๋น์ทํ ์์น. ์ ์ฌํ ๋จ์ด๊ฐ ๊ฑฐ๋ฆฌ๋ ์งง๊ณ  ๊ทธ๋ ์ง ์์ ๋จ์ด๊ฐ ๊ฑฐ๋ฆฌ๋ ๊ธธ ๊ฒ.

- Word2Vec

  - ์ธ์  ๋จ์ด์์ ๋จ์ด์ ๋ฒกํฐ ํํ์ ๊ต์กํ๊ธฐ ์ํ ์๊ณ ๋ฆฌ์ฆ. ๋จ์ํ ์ํซ๋ฒกํฐ๋ง ์ฌ์ฉํ๋ฉด ์ ์ฌ๋๋ ๊ณ ๋ คํ  ์ ์์๋ค. ์ด๋ฅผ ๋ณด์ํ๊ธฐ.
  - ์ ์ฌํ ๋งฅ๋ฝ์ ๋จ์ด๋ ๋น์ทํ ์๋ฏธ๋ฅผ ๊ฐ์ง ๊ฒ์ด๋ค๋ผ๋ ๊ฐ์ ์ ์ ์ ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img08.PNG" alt="Word2Vec"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img09.PNG" alt="Word2Vec"></p>

-
  - ์ฌ๋ผ์ด๋ฉ ์๋์ฐ : ์๋ค ๋จ์ด์์ ํจ๊ป ๊ณ ๋ ค. ๊ฐ์ด 3์ด๋ผ๋ฉด ์ฆ์ฌ๋จ์ด์ ์๋ค 1๊ธ์์ฉ์ ์ถ๊ฐํด ์ด 3๊ฐ ๋จ์ด๋ก ์ค์ฌ๋จ์ด ์ ๊ตฌ์ฑ.  
  - ์ฃผ์ด์ง ํ์ต ๋ฐ์ดํฐ๋ฅผ ๋จ์ด๋ณ๋ก Tokenization ํ ์ ์๋ฏธํ ๋จ์ด๋ค๋ก๋ง ์ฌ์ ์ ๊ตฌ์ฑ -> ์ํซ๋ฒกํฐ๋ก ๊ตฌ์ฑ -> ์ฌ๋ผ์ด๋ฉ ์๋์ฐ ๋ฐฉ์์ ์ฐจ์ฉํ์ฌ ๋จ์ด์์ ๊ตฌ์ฑํ๊ณ  ๋จ์ด๊ฐ ์ ์ฌ๋ ๊ณ์ฐ
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img10.PNG" alt="Word2Vec"></p>

-
  - ๊ฒฐ๊ณผ๋ก ๋์ค๋ ๋ฒกํฐ ๊ฐ ๊ฑฐ๋ฆฌ๋ ๋น์ทํ ๊ด๊ณ์ผ ๊ฒฝ์ฐ ๋น์ทํ๊ฒ ๋ํ๋๋ค. ex) vec[queen] โ vec[king] = vec[woman] โ vec[man]
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img11.PNG" alt="Word2Vec"></p>

-
  - ํ์ต ์ฐธ์กฐ : ํ์ต https://ronxin.github.io/wevi , ํ๊ตญ์ด http://w.elnn.kr/search , ๋จ์ด์ ์ฌ http://wonjaekim.com/archives/50 , ์๋ฏธ๊ฐ ๊ฐ์ฅ ์์ดํ ๋จ์ด ์์น https://github.com/dhammack/Word2VecExample
  - Word2Vec์ ๋ค์ํ ์์ฐ์ด์ฒ๋ฆฌ ์์ญ์์ ํ์ฉ๋๋ค. ๋จ์ด ์ ์ฌ๋, ๊ธฐ๊ณ ๋ฒ์ญ, Part-of-speech(PoS) tagging, Named entity recognition(NER), ๊ฐ์  ๋ถ์, ํด๋ฌ์คํฐ๋ง, Semantic lexicon building, ์ด๋ฏธ์ง ์บก์๋ ๋ฑ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img12.PNG" alt="๋ฒ์ญ"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img13.PNG" alt="Semantic lexicon building"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img14.PNG" alt="์ด๋ฏธ์ง์บก์๋"></p>

- GloVe

  - ์๋ ฅ ๋ฐ ์ถ๋ ฅ ์๋์ ๊ฐ ์์ ๊ฒํ ํ๋ ๋์  ๋จผ์  ํ ์๋์ฐ ๋ด ๋จ์ด์ ๋น๋๋ฅผ ๋จผ์  ๊ณ์ฐ. ์ค๋ณต๊ณ์ฐ์ ์ค์ฌ์ Word2Vec๋ณด๋ค ํ์ต์ด ๋น ๋ฅด๊ณ  ์์ ๋ฐ์ดํฐ์์๋ ์ ๋์ํ๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img15.PNG" alt="GloVe"></p>

-
  - ๋น๋ฒํ๊ฒ ๋ฑ์ฅํ๋ ๋จ์ด์์ Word2Vec์ ๋ชจ๋ ๊ณ์ฐํ์ง๋ง GloVe๋ ํ ๋ฒ๋ง ์ทจํจ.
  - ์ถ์ฒ ์์คํ์ ๋ง์ด ์ฐ์ธ๋ค.
  - Word2Vec ์์์ ๊ฐ์ด, ์ฑ๋ณ์ ์ฐจ์ด๋ฟ์ธ ๋จ์ด๊ฐ์ ๊ฑฐ๋ฆฌ, ๊ฐ์กฐ ์ฐจ์ด๋ฟ์ธ ๋จ์ด๊ฐ์ ๊ฑฐ๋ฆฌ ๋ฑ์ด ์ผ์ ํ ๊ฒ์ ํ์ธ ๊ฐ๋ฅ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img16.PNG" alt="GloVe"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img17.PNG" alt="GloVe"></p>

  - ์คํ ์์ค ์ฐธ์กฐ : https://nlp.stanford.edu/projects/glove

# โ๏ธ Doodle

- ์๋ก์ด U์คํ์ด์ง, ์๋ก์ด ํ. ์ด์  NLP์ ์ง์คํ๋ ๊ฐ์๋ฅผ ๋ฃ๊ณ  ๋ค์ P์คํ์ด์ง๋ฅผ ์ค๋นํ๋ค. ํญ์ ๊ณํ์ ์ฒซ๋ ์ ์์ ๋์น๊ธฐ ๋ง๋ จ์ด๋ ์ด๋ฒ์๋ ๊ทธ ํจ๊ณผ ๋์ ๋ณด๊ธธ ๋ฐ๋๋ค. ํน๋ณํ ์ด์๊ฐ ์๋ ํน๋ณํ ๋ . ์ค๋์ ๋์ ๋ฅด๋ค.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Rene_Magritte_1953_Golconda.jpg"></p>
<p align="center">Renรฉ Magritte, &ltGolconda&gt, 1953. Oil on canvas, 81x100cm.</p>

- Day 25 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_2/Day24/Note.md "Day24 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day26/Note.md "Day26 Note")
