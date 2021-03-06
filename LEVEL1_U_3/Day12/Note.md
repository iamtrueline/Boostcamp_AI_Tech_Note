# ๐ Note

### AutoGrad & Optimizer

- Module

  - torch.nn.Module : ๋ฅ๋ฌ๋์ ๊ตฌ์ฑํ๋ Layer์ base class, Input, Output, Forward, Backward ์ ์, ํ์ต์ ๋์์ด ๋๋ parameter(tensor) ์ ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day12_img00.PNG" alt="Forwardpass and Backwardpass"></p>

- Parameter

  - nn.Parameter : Tensor ๊ฐ์ฒด์ ์์ ๊ฐ์ฒด, nn.Module ๋ด์ attribute๊ฐ ๋  ๋๋ required_grad=True๋ก ์ง์ ๋์ด ํ์ต ๋์์ด ๋๋ Tensor(AutoGrad).
  - ์ฐ๋ฆฌ๊ฐ ์ง์  ์ง์ ํ  ์ผ์ ์ ์๊ณ  ๋๋ถ๋ถ์ layer์๋ weights ๊ฐ๋ค์ด ์ง์ ๋์ด ์๋ค. ์ฌ๋งํ๋ฉด ํ์๋ก.

- Backward

  - Layer์ ์๋ Parameter๋ค์ ๋ฏธ๋ถ์ ์ํ.
  - Forward์ ๊ฒฐ๊ณผ๊ฐ (model์ output=์์ธก์น)๊ณผ ์ค์ ๊ฐ ๊ฐ์ ์ฐจ์ด(loss) ์ ๋ํด ๋ฏธ๋ถ์ ์ํํ๊ณ  ํด๋น ๊ฐ์ผ๋ก ํ๋ผ๋ฏธํฐ ์๋ฐ์ดํธ.
  - Backward from the scratch : ์ค์  backward๋ Module ๋จ๊ณ์์ ์ง์  ์ง์  ๊ฐ๋ฅ. Module์์ backward์ optimize ์ค๋ฒ๋ผ์ด๋ฉ, ์ฌ์ฉ์๊ฐ ์ง์  ๋ฏธ๋ถ ์์์ ์จ์ผ ํ๋ ๋ถ๋ด(์ธ ์ผ์ ์์ผ๋ ์์๋ ์ดํดํด์ผํ๋ค). ๋ณดํต ๋ ์ด์ด๊ฐ ๋ง์ผ๋๊น.

---

### Dataset & Dataloader

- ๋ชจ๋ธ์ ๋ฐ์ดํฐ๋ฅผ ๋ฃ๊ธฐ
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day12_img01.PNG" alt="Data -> Model"></p>

- Dataset

  - ๋ฐ์ดํฐ ์๋ ฅ ํํ๋ฅผ ์ ์ํ๋ ํด๋์ค. ๋ฐ์ดํฐ๋ฅผ ์๋ ฅํ๋ ๋ฐฉ์์ ํ์คํ.
  - Image, Text, Audio ๋ฑ์ ๋ฐ๋ผ ํจ์ ์๋ ฅ ์ ์๊ฐ ๋ค๋ฅด๋ค.
  - ๋ชจ๋  ๊ฒ์ ๋ฐ์ดํฐ ์์ฑ ์์ ์ ์ฒ๋ฆฌํ  ํ์๋ ์๋ค. ์๋ฅผ ๋ค์ด image์ Tensor ๋ณํ๋ ํ์ต์ ํ์ํ ์์ ์ ๋ณํ.
  - ๋ฐ์ดํฐ ์์ ๋ํ ํ์คํ๋ ์ฒ๋ฆฌ๋ฐฉ๋ฒ์ด ์ ๊ณต๋์ด์ผ ์ง์ ์ฌ์ฉ์ด ์ฉ์ดํ๋ค.
  - ํ์คํ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ : HuggingFace ๋ฑ.

- DataLoader

  - Data์ Batch๋ฅผ ์์ฑํด์ฃผ๋ ํด๋์ค.
  - ํ์ต์ง์ (GPU feed์ ) ๋ฐ์ดํฐ์ ๋ณํ์ ์ฑ์.
  - Tensor๋ก ๋ณํ + Batch ์ฒ๋ฆฌ๊ฐ ๋ฉ์ธ ์๋ฌด.

# โ๏ธ Doodle

- ๊ณผ์  ํด๊ฒฐ์ด ์ค๋ ๊ฑธ๋ฆฐ๋ค. ๊นจ๋ฌ์ ์ ์, ๋ ํ์ด์ฌ ๋ชจ๋ฅด๋ค? ํ์ดํ ์น ๋ฌธ์๋์ ์๋๋ผ์ ํ๋ํ๋ ์ฐพ์๋ณผ ์ ์์ง๋ง, ํ์ ๊ณผ์ ๋งํผ์ ์ํํด์ผ ํ๋๋ฐ. ์ค๋ ๋ณธ ๊ฐ์์ ์ถฉ์คํ์ง ์์์ ๋์ค์ ๋ค์ ํ๋ฒ ์ ๋ฆฌํด์ผ ํ๋ค. ์ฝ๋ ์ค์ฌ ๊ฐ์์ฌ์ ๋ฐ๋ก ์ ์ด๋๋ ๊ฒ ๋์ ๋ฏ. ์ค๋์ ๋์ ์ํ๋ค์ค ํ๋ฅด๋ฉ์ด๋ฅด.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Johannes_Vermeer_1665_Girl_with_a_Pearl_Earring.jpg"></p>
<p align="center">	Johannes Vermeer, &ltGirl with a Pearl Earring&gt, 1665. Oil on canvas, 44.5x39cm.</p>

- Day 12 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day11/Note.md "Day11 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day13/Note.md "Day13 Note")
