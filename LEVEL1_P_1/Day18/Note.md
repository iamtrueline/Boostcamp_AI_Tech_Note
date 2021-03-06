# ๐ Note

### Training & Inference 1

- Loss

  - ์ค์ฐจ ์ญ์ ํ -> Loss ํจ์ = Cost ํจ์ = Error ํจ์
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img00.PNG" alt="์ค์ฐจ ์ญ์ ํ"></p>

-
  - ์ด์ ์ ํ์ตํ๋ ์ญ์ ํ์ ๋์ผ.
  - Loss์จ ๊ณ์ฐ์ ๋ฐ๋ผ ํ์ต๋ ๋ฌ๋ผ์ง๋ค.
  - nnํจํค์ง ๋ด _Loss๋ nn.Module Family = foward() ์์.
  - loss.backward() : ํจ์ ์คํ ์ ์ฐ๊ฒฐ๋ chain์ ํตํด ๋ชจ๋ธ ํ๋ผ๋ฏธํฐ์ grad ๊ฐ์ด ์๋ฐ์ดํธ. ๋ง๊ณ  ์ถ๋ค๋ฉด required_grad=false.
  - Focal Loss : ClassImbalance ๋ฌธ์ ๊ฐ ์๋ ๊ฒฝ์ฐ, ๋ง์ถ ํ๋ฅ ์ด ๋์ Class๋ ๋ฎ์ loss, ๋ง์ถ ํ๋ฅ ์ด ๋ฎ์ Class๋ ๋์ loss๋ฅผ ๋ถ์ฌ.
  - Label Smoothing Loss : Class targetlabel์ Onehot์ด ์๋ Smoothํ ํํ๋ก ํํ.

- Optimizer

  - ์ด๋ ๋ฐฉํฅ์ผ๋ก ์ผ๋ง๋ ๋นจ๋ฆฌ ์์ง์ผ๊น?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img01.PNG" alt="ํ์ต๋ฅ "></p>

-
  - LR(Learning Rate) scheduler : ํ์ต๋ฅ ์ ๋์ ์ผ๋ก ์กฐ์ ํ๋ ์ฅ์น. ํ์ต๋ฅ ์ด ๊ณ ์ ๋๋ฉด ์๋ฒฝํ ํ์ต๊ณผ ๊ฑฐ๋ฆฌ๊ฐ ์์ ์ ์๋ค. ํ์ต ์์ ํ์ต๋ฅ ์ ๋์ ์ผ๋ก ์กฐ์ ํ๋ฉด ๋ ์ ํํ ์๋ ดํ  ๊ฒ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img02.PNG" alt="ํ์ต๋ฅ  ๋ณ๋๊ฐ๋ถ์ ๋ฐ๋ฅธ ์์ ๊ทธ๋ํ"></p>

-
  - StepLR : ๊ฐ์ฅ ๋ง๋ค๊ธฐ ์ฌ์ด LR scheduler. ํน์  Step๋ง๋ค ํ์ต๋ฅ ์ด ๊ฐ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img03.PNG" alt="StepLR"></p>

-
  - CosineAnnealingLR : Cosine ํจ์ ํํ์ฒ๋ผ LR์ ๊ธ๊ฒฉํ ๋ณ๊ฒฝ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img04.PNG" alt="CosineAnnealingLR"></p>

-
  - ReduceLROnPlateau : ๊ฐ์ฅ ์ผ๋ฐ์ ์ผ๋ก ์ฐ์ด๋ scheduler. ๋ ์ด์ ์ฑ๋ฅ ํฅ์์ด ์์ ๋ LR ๊ฐ์.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img05.PNG" alt="ReduceLROnPlateau"></p>

- Metric

  - ํ์ต์ ์ง์ ์ ์ผ๋ก ์ฌ์ฉ๋๋ ๊ฒ์ ์๋์ง๋ง ํ์ต๋ ๋ชจ๋ธ์ ๊ฐ๊ด์ ์ผ๋ก ํ๊ฐํ  ์ ์๋ ์งํ๊ฐ ํ์. Classification, Regression, Ranking ๋ฑ.
  - Classification : Accuracy, F1-score, precision, recall, ROC&AUC
  - Regression : MAE, MSE
  - Ranking : MRR, NDCG, MAP
  - ํ์์์๋ Metric์ด ๋ฏธ๋ฆฌ ์ค์ ๋์ด์์ง ์๋ค. ๊ทธ๋ฌ๋ฏ๋ก ๋ฐ์ดํฐ ์ํ์ ๋ฐ๋ผ ์ ์ ํ Metric์ ์ ํํ๋ ๊ฒ์ด ํ์. ex) Class ๋ณ๋ก ๋ฐธ๋ฐ์ค๊ฐ ์ ์ ํ ๋ถํฌ? -> Accuracy, Class๋ณ ๋ฐธ๋ฐ์ค๊ฐ ์ข์ง ์์์ ๊ฐ ํด๋์ค ๋ณ๋ก ์ฑ๋ฅ์ ์ ๋ผ ์ ์๋์ง ํ์ธ ํ์? -> F1-Score ๋ฑ.

---

### Training & Inference 2

- Training

  - ํธ๋ ์ด๋์ ์ํด ํ์ํ ์ค๋น๋ฌผ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day18_img06.PNG" alt="ํธ๋ ์ด๋์ ์ํด ํ์ํ ์ค๋น๋ฌผ"></p>

-
  - ํธ๋ ์ด๋ ํ๋ก์ธ์ค๋?
  - model.train() -> optimzer.zero_grad() -> loss=criterion(outputs,labels) -> loss๋ฅผ ๋ง์ง๋ง์ผ๋ก chain์์ฑ -> loss์ grad_fn chainโ loss.backward() -> optimizer.step()

- Inference

  - Inference ํ๋ก์ธ์ค๋?
  - model.eval() -> withtorch.no_grad()
  - ์ถ๋ก  ๊ณผ์ ์ Validation set๊ฐ ๋ค์ด๊ฐ๋ค๋ฉด ๊ฒ์ฆ ๊ณผ์ .
  - ๋ชจ๋  ์ ์ฐจ๊ฐ ๋๋๋ฉด Submission ์คํ์ ๋ง์ถ์ด ํ์ผ ๋ณํ ํ ์ ์ถ.

- Pytorch Lightning

  - ์์ฐ์ฑ์ ์ํ ํจํค์ง.
  - ์์์ ๊ฑฐ์น ๋จ๊ณ๋ฅผ ํ๋์ ์ ์์ ์ผ๋ฐ์ ์ธ ๋ฐ์ดํฐ๋ก ๋๋ธ๋ค.
  - ๋ฐฐ์ฐ๋ ๋จ๊ณ๋ฅผ ์ง๋ ํ๋ก์ธ์ค๋ฅผ ์ฝ๊ณ  ๋น ๋ฅด๊ฒ ์ดํดํ  ์ ์๋ค๋ฉด ์ฌ์ฉํ๊ธฐ.

# โ๏ธ Doodle

- ํ์ ์ฝ๋ ๋ฆฌ๋ทฐ๋ฅผ ํตํด ์ฑ๋ฅ์ด ์ ๋์ค๋ ๋ชจ๋ธ, ํน์ ์ ๋์ค๊ธฐ ์ํด ์ฌ๋ฌ ์๋๋ฅผ ํ ๋ชจ๋ธ์ ๋ณธ ๋ . ์ฌ๊ธฐ์ ๊ฐ์ฅ ๋ง์ด ๋ฐฐ์ด ๊ฑด ์ฝ๋ ๊ณต์ ๊ฐ ์ค์ค๋ผ์๋ค๋ ์ ์ด๋ค. ๋ด ์ฝ๋๋ ๋ ํผ์ ๋ณผ ๋ ์์คํ์ง๋ง ๋ค๋ฅธ ์ฌ๋๋ค ์์ ๋ฐ๋ฆฌ๊ณ  ๋์ค๊ธฐ ์ซ์๋ฐ. ์ด์ ๋์น๋ ์ข์ ์ฌ๋๋ค ์ฌ์ด์์  ํ์คํ ๋ ๋ง์ด ๋ฐฐ์ธ ์๋ฐ์ ์๋ค. ๋ด๊ฐ ๊ทธ๊ฑธ ์ ๋ด์ ์ ์๋ ๊ทธ๋ฆ์ด ๋๊ธธ ๋ฐ๋. Resnet50 ๋ชจ๋ธ์ ๊ฐ์ ธ์ ๋๋ ค๋ณด์๊ณ , ๊ฒฐ๊ณผ๋ ๋์์ง๋ง ๋ฐ์ดํฐ ์ฒ๋ฆฌ๊ฐ ์๋ง์ด์๋์ง ์ฑ๋ฅ์ ๋ฎ๋ค. ์ฌ์ง์ด ์ ์ถ ํ์ผ ์ฒ๋ฆฌ๋ฅผ ์๋ชปํด์ submit fail๋ ์ฌ๋ฌ ๋ฒ ๋ด๋ค. ๋์ด ์์ธก๋ฅ ์ด ๊ฐ์ฅ ๋ฎ์๋ฐ, ์ด๊ฑด ๋ด ๋์ผ๋ก ๋ด๋ ์ด๋ ค์ฐ๋ ๋ด์ค๋ค. ๊ทธ๋๋ ๋จธ๋ฆฌ๊ฐ ์๋ค๊ณ  ๋ฌด์กฐ๊ฑด ์๊ธฐ๋ผ๊ณ  ๋จ์  ์ง๋ ๊ฑด ๋๋ฌด ๊ฒ์ผ๋ฅด๋ค. ๋ชจ๋ธ๋ฟ ์๋๋ผ ๋ฐ์ดํฐ๋ ๊ทธ๋๋ก ๋์ด์ค๋ ๊ฒ ์ข์๊น? ์ค๋๋ถํฐ ๋ํ์ ํ์ผ๋ก ๋ณํฉ๋์ด์ ์ ์ถ ํ์ ์ ํ์ด ๋ ์ ์ด์ง๋ค. ๋ง์๋๋ก ๋ผ ์ ์์ ๊ฒ์ด๊ธฐ ๋๋ฌธ์ ๋ก์ปฌ์์ ์ ํ๋๋ฅผ ์ธก์ ํ๊ณ  ์๋ค. ํ์ต ์ ํ๋๊ฐ ๋๊ฒ ๋์๋ ์ํ ๊ฒฐ๊ณผ๋ 20~30% ์ธ์ ๋ฆฌ์ ๋จธ๋ฌด๋ฅด๊ณ  ์๋ค. ์๋ง ์ค์  ์ ์ถ ์์ ์ค์ฐจ ๋๋ฌธ์ ๋ ๋ฎ์ ๊ธฐ๋ก์ ํ  ๊ฒ. ์์ง? ์์ง์ ๋ชจ๋ฅด๊ฒ ๋ค. ์ด์   ๊ฟ์์๋ ๋ชจ๋ธ์ ๋๋ฆฌ๊ณ  ์๋ค. ์ ์ ์ฌ๊ณ , ๋ง์๊ณ , ์์. ์ค๋์ ๋์ ์นด๋ผ๋ฐ์กฐ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Caravaggio_Merisi_1595_The_adolescent_Bacchus.jpg"></p>
<p align="center">Caravaggio Merisi, &ltThe adolescent Bacchus&gt, 1595-1597. Oil on canvas, 95x85cm.</p>

- Day 18 ๋ง์นจ.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day17/Note.md "Day17 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_1/Day19/Note.md "Day19 Note")
