# π Note

### Introduction to PyTorch

- νλ μμν¬

  - μ΄μ  κ΅¬νμ 0λΆν° μμν  νμλ μλ€.
  - μλ£λ λ§κ³  κ΄λ¦¬λ μ λκ³  μ¬μ€μ νμ€μΌλ‘ μ°λ λ§μ νλ μμν¬λ€ like νμνλ‘, νμ΄ν μΉ.
  - PyTorch : Dynamic Computation Graph
  - TensorFlow : Define and run
  - Computational Graph : μ°μ°μ κ³Όμ μ κ·Έλνλ‘ ννν κ². νμνλ‘λ κ·Έλνλ₯Ό λ¨Όμ  μ μνκ³  μ€ν μμ μ feed, νμ΄ν μΉλ μ€νμ νλ©΄μ κ·Έλνλ₯Ό μμ±.
  - νμ΄ν μΉμ κ°μ  : Define by Run = μ¦μ νμΈ κ°λ₯->pythonic code. GPU support, Good API and community, μ¬μ© μ©μ΄. Numpy + AutoGrad + Function. Numpy κ΅¬μ‘°λ₯Ό κ°μ§λ Tensor κ°μ²΄λ‘ μ΄λ μ΄ νν. μλ λ―ΈλΆ μ§μ, DL μ°μ° μ§μ, λ€μν ννμ DLμ μ§μνλ ν¨μμ λͺ¨λΈ μ§μ.

---

### PyTorch Basics

- PyTorch?

  - numpy + AutoGrad
  - Tensor : λ€μ°¨μ μ΄λ μ΄λ₯Ό νννλ PyTorch ν΄λμ€. μ¬μ€μ numpyμ ndarrayμ λμΌ(TFμ Tensorμλ λμΌ). μμ± ν¨μλ κ±°μ λμΌ. listλ ndarry μ¬μ© κ°λ₯. κΈ°λ³Έμ μΌλ‘ κ°μ§ μ μλ λ°μ΄ν° νμμ΄ numpyμ λμΌνλ©° μ¬μ©λ²λ κ·Έλλ‘ μ μ©λ¨.
  - νμ΄ν μΉμ Tensorλ GPUμ μ¬λ €μ μ¬μ© κ°λ₯.
  - view : reshapeμ²λΌ tensorμ shapeμ λ³ν.
  - squeeze : μ°¨μμ κ°μκ° 1μΈ μ°¨μμ μ­μ  (μμΆ)
  - unsqueeze : μ°¨μμ κ°μκ° 1μΈ μ°¨μμ μΆκ°.
  - κΈ°λ³Έμ μΈ μ°μ°μ numpyμ λμΌ.
  - mmμ μλ broadcastion no, matmulμ yes.
  - nn.functional λͺ¨λμ ν΅ν΄ λ€μν μμ λ³ν μ§μ.
  - μλ λ―ΈλΆ μ§μ. backward()

---

### PyTorch νλ‘μ νΈ κ΅¬μ‘° μ΄ν΄νκΈ°

- Overview

  - μ΄κΈ° λ¨κ³μμλ λνμ κ°λ° κ³Όμ μ΄ μ λ¦¬. νμ΅κ³Όμ κ³Ό λλ²κΉ λ± μ§μμ μΈ νμΈμ΄ νμ.
  - λ°°ν¬ λ° κ³΅μ  λ¨κ³μμλ λΈνΈλΆ κ³΅μ κ° μ΄λ €μ. μ¬μ΄ μ¬νμ΄ μ΄λ ΅κ³  μ€ν μμκ° κΌ¬μ.
  - DL μ½λλ νλμ νλ‘κ·Έλ¨μΌλ‘, κ°λ° μ©μ΄μ± νλ³΄μ μ μ§λ³΄μ ν₯μ νμ.
  - μ£ΌνΌν°λ‘λ μ μ§λ³΄μ ν₯μμ νκ³κ° μμ.
  - λ€μν νλ‘μ νΈ ννλ¦Ώμ΄ μμΌλ―λ‘ μ¬μ©μ νμμ λ°λΌ μμ νμ¬ μ¬μ©.

---

### κΈ°λ³Έ μ°¨νΈμ μ¬μ© 2-1κ°

- Bar Plot

  - μ§μ¬κ°ν λ§λλ₯Ό μ¬μ©νμ¬ λ°μ΄ν°μ κ°μ νννλ μ°¨νΈ/κ·Έλν. = λ§λ κ·Έλν, bar chart, bar graph.
  - λ²μ£Ό(category)μ λ°λ₯Έ μμΉ κ°μ λΉκ΅νκΈ°μ μ ν©ν λ°©λ². κ°λ³ λΉκ΅μ κ·Έλ£Ή λΉκ΅ λͺ¨λμ μ ν©νλ€.
  - .bar() = μμ§, .barh() = μν. μμ§(vertical)μ xμΆμ λ²μ£Ό, yμΆμ κ°μ νκΈ°νκ³  μν(horizontal)μ yμΆμ λ²μ£Ό, xμΆμ κ°μ νκΈ°νλ€. μ μκ° λν΄νΈ, νμλ λ²μ£Όκ° λ§μ λ μ ν©.
  - κ·Έλ£Ήμ΄ 5κ°~7κ° μ΄νμΌ λ ν¨κ³Όμ μ΄λ©°, κ·Έλ£Ήμ΄ μ΄λ³΄λ€ λ§λ€λ©΄ λΉμ€μ΄ μμ κ·Έλ£Ήμ ETC μ²λ¦¬.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img00.PNG" alt="Bar Plot"></p>

-
  - Bar Plotμμλ λ²μ£Όμ λν΄ κ° κ°μ νν -> μ¦ 1κ°μ featureμ λν΄μλ§ λ³΄μ¬μ£Όλ―λ‘ μ¬λ¬ κ·Έλ£Ήμ λ³΄μ¬μ£ΌκΈ° μν΄μλ μ¬λ¬κ°μ§ λ°©λ²μ΄ νμ. μ΄μ, νλ‘―μ μ¬λ¬κ° κ·Έλ¦¬κ±°λ ν κ°μ νλ‘―μ λμμ λνλ΄λ λ°©λ²λ±μ μΈ μ μλ€.

- Multiple Bar Plot

  - νλ‘―μ μ¬λ¬ κ° κ·Έλ¦¬κΈ°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img01.PNG" alt="Multiple Bar Plot"></p>

- Stacked Bar Plot

  - 2κ° μ΄μμ κ·Έλ£Ήμ μμμ(stack) νν. λ§¨ λ°μ bar νμμ μ½μ§λ§ κ·Έ μΈλ μ΄λ ΅λ€.
  - .bar()μμλ bottom νλΌλ―Έν°λ₯Ό μ¬μ©, barh()μμλ left νλΌλ―Έν°λ₯Ό μ¬μ©.
  - μμ©νμ¬ μ μ²΄μμ λΉμ¨μ λνλ΄λ Percentage Stacked Bar Chartκ° μμ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img02.PNG" alt="Stacked Bar Plot"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img03.PNG" alt="Overlapped Bar Plot"></p>

- Grouped Bar Plot

  - κ·Έλ£Ήλ³ λ²μ£Όμ λ°λ₯Έ barλ₯Ό μ΄μλκ² λ°°μΉνλ λ°©λ². 
  - MatplotlibμΌλ‘λ λΉκ΅μ  κ΅¬νμ΄ κΉλ€λ‘μ°λ, λ°©λ²μ .set_xticks(), .set_xticklabels()
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img04.PNG" alt="Grouped Bar Plot"></p>

- μ νν Bar Plot

  - Principle of Proportion Ink : μ€μ  κ°κ³Ό κ·Έμ ννλλ κ·Έλν½μΌλ‘ ννλλ μν¬μμ λΉλ‘. μ΄λ λλΆλΆ μκ°νμμ μ μ©λλ λ£°.
  - λ°λμ xμΆμ μμμ 0(zero).
  - λ μ νν μ λ³΄λ₯Ό μ λ¬νκΈ° μν΄μλ μ λ ¬μ΄ νμ. λ°μ΄ν° μ’λ₯μ λ°λΌ, μκ³μ΄ = μκ°μ, μμΉν = ν¬κΈ°μ, μμν = λ²μ£Όμμ, λͺλͺ©ν = λ²μ£Όμ κ°μΌλ‘ μ λ ¬.
  - μ¬λ°±κ³Ό κ³΅κ° μ‘°μ  λ±μΌλ‘ κ°λμ± λμ΄κΈ°.
  - μ ννκ³  λ¨μνκ². λ¬΄μλ―Έν 3Dλ νμ μλ€. μ§μ¬κ°νμ΄ μλ λ€λ₯Έ ννμ barλ μ§μ.
  - μ€μ°¨ λ§λλ₯Ό μΆκ°νμ¬ Uncertainty μ λ³΄λ₯Ό μΆκ° κ°λ₯.
  - Bar μ¬μ΄ Gapμ΄ 0μ΄λΌλ©΄ -> νμ€ν κ·Έλ¨(Histogram).
  - Text μ λ³΄(μ λͺ©, λΌλ²¨)λ₯Ό λ€μνκ² νμ©νκΈ°.

---

### Generative Models 2

- Variational Auto-encoder(VAE)

  - Variational inference(λ³λΆμΆλ‘ )μ λͺ©μ μ Posterior distribution(μ¬νλΆν¬)λ₯Ό μ°Ύλ κ².
  - κ·Έλ¬λ μΌλ°μ μΌλ‘λ Posterior distribution(p(z|x))μ κ΅¬νκΈ° μ΄λ €μ. κ·Έλμ μ΅λν κ·Όμ¬ν κ°, Variational distribution(q(x))μ μ΄λ€. 
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img05.PNG" alt="Variational inference"></p>

-
  - λ¬Έμ λ, λͺ¨λ₯΄λ κ°μ κ·Όμ¬ν  μ μλκ°? So, ELBO(Evidence Lower BOund)λ₯Ό κ³μ°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img06.PNG" alt="ELBO"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img07.PNG" alt="ELBO"></p>

-
  - Reconstruction Term : μ΄μμ μΈ μνλ§ ν¨μλ‘λΆν° μΌλ§λ μ λ³΅μμ νλκ°?
  - Regularlization Term : μ΄μμ μΈ μνλ§ ν¨μκ° μ΅λν priorμ κ°λλ‘ λ§λ€κΈ°. μ¬λ¬ μν μ€μμ priorμ μ μ¬ν κ°μ μνλ§νλλ‘ μ‘°κ±΄ λΆμ¬.
  - Key limitation : intractable λͺ¨λΈ. μΌλ§λ κ·Όμ¬νμ§ μκΈ° νλ¦. KL divergenceκ° λ―ΈλΆ κ°λ₯ν΄μΌνλ―λ‘ λ³΄ν΅ λͺ¨λ  μμνμ΄ independentν isotropic Gaussianμ μ¬μ©.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img08.PNG" alt="KL divergence"></p>

- Adversarial Auto-encoder(AAE)

  - κ°μ°μμμ νμ©νκ³ μΆμ§ μμΌλ©΄? latent distributionμ λ§μΆκΈ° μν΄ GANμ νμ©νλ AAEμ¬μ©.
  - μ±λ₯λ μΌλ°μ μΌλ‘ VAEλ³΄λ€ λ«λ€.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img09.PNG" alt="KL divergence"></p>

- GAN

  - νλ¦μ? νμͺ½(discriminator)μ μ΅λλ‘, νμͺ½(generator)μ μ΅μ λ‘ λ?μΆκΈ°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img10.PNG" alt="GAN"></p>

-
  - GANκ³Ό VAE μ°¨μ΄
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img11.PNG" alt="GAN and VAE"></p>

- GAN κ΄λ ¨ λΌλ¬Έλ€ μ°Έμ‘°

  - DCGAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img12.PNG" alt="DCGAN"></p>

-
  - Info-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img13.PNG" alt="Info-GAN"></p>

-
  - Text2Image
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img14.PNG" alt="Text2Image"></p>

-
  - Puzzle-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img15.PNG" alt="Puzzle-GAN"></p>

-
  - CycleGAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img16.PNG" alt="CycleGAN"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img17.PNG" alt="CycleGAN"></p>

-
  - Star-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img18.PNG" alt="Star-GAN"></p>

-
  - Progressive-GAN
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day11_img19.PNG" alt="Progressive-GAN"></p>

# βοΈ Doodle

- κΈ΄ ν΄μΌ λ. κΈ΄ λΌλ¬Έ μ λ. λ€λλ©΄ μλλ° λ³΅μ΅μ νμ§ μλ κ±΄ λ§λ μ λλ€. κ·Έλ¦¬κ³  λ μ΄λΆμ±μ€μ μμ΄μ½μ΄μ§. μ§λμ£Όμ μ΄ν΄κ° λ?μ μ λΆ κΈ°λ‘νμ§ λͺ»νλ Generative Modelμ λ€μ κΈ°λ‘νκ³ , μ κ³Όμ λ₯Ό μμνλ€. μ νμ΄ν μΉλ₯Ό λ°°μ°λ μμκ° λ€μλμ§ μμνλλ° λμ΄λλ₯Ό λ³΄λ μ΄ν΄λλ€. λ§ν¬κ° μΉμ ν΄μ λ΄μ©λ μΉμ ν  κ±°λΌ μκ°νλλ° μλμμ΄. μ¬λμ΄λ  κ³Όμ λ  κ²λͺ¨μ΅λ§ λ³΄κ³  νλ¨νμ§ λ§λΌλ λ©ν λ€μ κ΅νμ΄λΌκ³  μκ°νλ€. μ€λμ λμ λ λΈλνΈ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Rembrandt_1642_The_Night_Watch.jpg"></p>
<p align="center">	Rembrandt van Rijn, &ltThe Night Watch&gt, 1642. Oil on canvas, 363x437cm.</p>

- Day 11 λ§μΉ¨.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_2/Day10/Note.md "Day10 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_U_3/Day12/Note.md "Day12 Note")
