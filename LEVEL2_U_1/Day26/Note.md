# π Note

### Recurrent Neural Network and Language Modeling

- RNN

  - μνμ€λ°μ΄ν°κ° μμΆλ ₯. κΈ°λ³Έ κ΅¬μ‘°λ μ΄μ  νμ΅κ³Ό λμΌ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img00.PNG" alt="RNN basic structure"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img01.PNG" alt="RNN basic structure"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img02.PNG" alt="RNN basic structure"></p>

- Types of RNNs

  - One-to-one : Standard Neural Networks. μμΆλ ₯μ΄ λ¨ νλμΈ, μνμ€ λ°μ΄ν°κ° μλ μΌλ°μ μΈ κ²½μ°. ex) μ¬λμ λͺΈλ¬΄κ², ν€, λμ΄ λ±μ μλ ₯λ°κ³  κ·Έ μ¬λμ κ³ /μ /μ μνμμ λΆλ₯.
  - One-to-many : μλ ₯μ νλ, μΆλ ₯μ μ¬λ¬ κ°. λνμ μΌλ‘ Image Captioning. νλμ μ΄λ―Έμ§λ₯Ό μλ ₯ λ°κ³  μ΄λ―Έμ§μ λν μ€λͺκΈμ νμν λ¨μ΄λ€μ μΆμΆ. μ΄ κ²½μ° μ²« λ²μλ§ μλ ₯μ΄ λ€μ΄κ°λ―λ‘ λ§€ νμ μ€ν­λ§λ€ λ€μ΄κ°λ λ°λ³΅ μλ ₯μ 0μΌλ‘.
  - Many to one : μ¬λ¬ μλ ₯κ°μ λ°μ μ΅μ’ μΆλ ₯μ νλλ‘. λνμ μΌλ‘ Sentiment Classification. μ΄ μμ κ²½μ°, μλ ₯ λ¬Έμ₯μ κ° λ¨μ΄λ₯Ό μλ μλ² λ©νμ¬ κ° νμμ€νμμ λ°κ³ , κ²°κ³Όμ μΌλ‘ νλμ μμν λμΆ.
  - Many to many : μμΆλ ₯ λͺ¨λ μνμ€ λ°μ΄ν°. λνμ μΌλ‘ Machine Translation. μ΄ κ²½μ°λ μλ ₯μ λ€ λ°μ ν μΆλ ₯ μμ±μ νλ κ²½μ°. Video classification on frame levelμ κ²½μ°, μλ ₯κ³Ό λμμ μΆλ ₯ μμ±.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img03.PNG" alt="Types of RNNs"></p>

- Character-level Language Model

  - μΈμ΄ λͺ¨λΈμ μ£Όμ΄μ§ λ¬Έμμ΄ νΉμ λ¨μ΄ μμλ₯Ό λ°νμΌλ‘ λ€μ λ¨μ΄λ₯Ό μμΈ‘νλ νμ€ν¬.
  - Many to many νν.
  - μλ μλ² λ© κ±°μΉ ν μΈμ΄ λͺ¨λΈ μν.
  - 'hello' μμ. 'h'κ° λμ¬ λ 'e'λ₯Ό μμΈ‘ν΄μΌ ν¨.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img04.PNG" alt="Character-level Language Model with 'hello'"></p>

-
  - μ μμ μ²«λ²μ§Έ μμνμ κ²½μ° 'o'κ°μ΄ μ μΌ λμΌλ―λ‘(4.1), 'e'κ°μ΄(2.2) κ°μ₯ λμμ§λ λ°©ν₯μΌλ‘ νμ΅ν΄μΌ ν¨.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img05.PNG" alt="Character-level Language Model with 'hello'"></p>

-
  - νμ΅μ΄ μμΌμλ‘ μΆλ ₯κ°μ κ·Έλ΄λ―ν΄μ§λ€.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img06.PNG" alt="λͺ¨λΈμ νμ΅ λ³ν"></p>

- BPTT (BackPropagation Through Time)

  - BPTT : κΈ°μ‘΄ μ κ²½λ§μ μ­μ ν(backprop)μλ λ¬λ¦¬ νμ μ€νλ³λ‘ λ€νΈμν¬λ₯Ό νΌμΉ λ€μ, μ­μ ν μκ³ λ¦¬μ¦μ μ¬μ©.
  - μμ£Ό λ§μ μνμ€κ° μ£Όμ΄μ§ λ, λͺ¨λ  μμνμ κ³μ°νκ³  λ‘μ€ κ³μ°μ νλ €λ©΄ GPUκ° λλ¬Όμ νλ¦°λ€. -> ν λ²μ νμ΅ν  λ°μ΄ν°λ₯Ό chunkλ‘ μλΌμ νμ΅νλ κ²μΌλ‘ ν΄κ²°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img07.PNG" alt="BPTT-entire data"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img08.PNG" alt="BPTT-chunk data"></p>

-
  - Vanila RNNμ λ§μ΄ μ¬μ©λμ§ μλλ€. μ­μ νμ κ·ΈλλμΈνΈκ° λλ¬΄ μμμ§κ±°λ, λ°λλ‘ λλ¬΄ μ»€μ Έμ νμ΅μ΄ μ λλ‘ μ΄λ€μ§μ§ μλ κ²½μ°κ° λ§κΈ° λλ¬Έ. μ΄μ λν ν΄κ²°μ, BPTTμ μ‘°μ μ κ°νλ κ²(Truncated BPTT). κ·Έλ¬λ μ΄ λν νμ΅ λ°μ΄ν°κ° μ₯κΈ°κ°μ κ±Έμ³ ν¨ν΄μ΄ λ°μ ν  λ νμ΅μ΄ μ΄λ ΅λ€. μ΄μ  λμμ RNNκ΅¬μ‘°λ₯Ό λ°κΎΈλ κ²(LSTM, GRU).
  - Truncated BPTT : BPTTλ μ μ²΄μ νμ μ€νλ§λ€ μ²μλΆν° λκΉμ§ μ­μ νλ₯Ό νκΈ° λλ¬Έμ νμ μ€νμ΄ ν΄ μλ‘ κ³μ°λμ΄ λ§μμ§λ λ¬Έμ κ° μλ€. μ΄λ¬ν κ³μ°λ λ¬Έμ λ₯Ό ν΄κ²°νκΈ° μν΄ μ μ²΄ νμ μ€νμ μΌμ  κ΅¬κ°μΌλ‘ λλ  μ­μ νλ₯Ό νλ Truncated BPTTλ₯Ό μ¬μ©.

---

### LSTM and GRU

- LSTM (Long Short-Term Memory)

  - RNNμ νλ  stateμ cell-stateλ₯Ό μΆκ°ν κ΅¬μ‘°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img09.PNG" alt="LSTM"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img10.PNG" alt="LSTM"></p>

-
  - Cell state : μμ linear interactionλ§μ μ μ©μν€λ©΄μ μ μ²΄ μ²΄μΈμ κ³μ κ΅¬λ. LSTMμ cell stateμ λ­κ°λ₯Ό λνκ±°λ μμ¨ μ μλ λ₯λ ₯μ΄ μλλ°, μ΄ λ₯λ ₯μ gateλΌκ³  λΆλ¦¬λ κ΅¬μ‘°λ‘ μ μ΄λλ©°, μκ·Έλͺ¨μ΄λ λ μ΄μ΄μ Pointwise κ³±μμΌλ‘ μ΄λ£¨μ΄μ Έ μλ€.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img11.PNG" alt="LSTM Cell state"></p>

-
  - Forget gate layer : LSTMμ μ²« λ¨κ³λ‘λ cell stateλ‘λΆν° μ΄λ€ μ λ³΄λ₯Ό λ²λ¦΄ κ²μΈμ§λ₯Ό μ νλ κ²μΌλ‘, sigmoid layerμ μν΄ κ²°μ λλ€. μ΄ λ¨κ³μμ λμΆλλ κ°μ΄ 1μ΄λ©΄ μ λ³΄ λ³΄μ‘΄, 0μ΄λ©΄ λΉλ³΄μ‘΄.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img12.PNG" alt="LSTM Forget gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img13.PNG" alt="LSTM Forget gate layer"></p>

-
  - Input gate layer : λ€μ λ¨κ³λ μμΌλ‘ λ€μ΄μ€λ μλ‘μ΄ μ λ³΄ μ€ μ΄λ€ κ²μ cell stateμ μ μ₯ν  κ²μΈμ§λ₯Ό μ νλ€. sigmoid layerμΈ input gate layerκ° μ΄λ€ κ°μ μλ°μ΄νΈμ§ μ ν ν tanh layerκ° μλ‘μ΄ νλ³΄κ° λ²‘ν°λ₯Ό λ§λ  ν cell state μλ°μ΄νΈλ₯Ό μ€λΉ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img14.PNG" alt="LSTM Input gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img15.PNG" alt="LSTM Input gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img16.PNG" alt="LSTM Input gate layer"></p>

-
  - μ΄ν κ³Όκ±° stateλ₯Ό μλ°μ΄νΈν΄μ μλ‘μ΄ cell stateλ₯Ό λ§λ λ€.
  - Output gate layer : λ§μ§λ§μΌλ‘ λ¬΄μμ outputμΌλ‘ λ΄λ³΄λΌ μ§ μ νλ€.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img17.PNG" alt="LSTM Output gate layer"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img18.PNG" alt="LSTM Output gate layer"></p>

- GRU (Gated Recurrent Unit)

  - LSTMμ κ΅¬μ‘°λ₯Ό κ²½λν. λΉ λ₯Έ κ³μ° μκ°. LSTMμ cell stateμ hidden stateλ₯Ό μΌμνν΄μ hidden state vectorλ§ μ‘΄μ¬. LSTMμ΄λ κ·Έ κ²½λν λ²μ  GRUλ λμμ λΉμ·νλ νμνλ©΄ λ λ€ λλ €λ³΄κΈ°.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img19.PNG" alt="GRU"></p>

-
  - Backpropagation in LSTM & GRU
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day26_img20.PNG" alt="Backpropagation in LSTM & GRU"></p>

# βοΈ Doodle

- λΆλͺ κ΅¬λ©΄μΈλ° μ΅μνμ§ μμ RNN. λ³Ό λλ§λ€ μΉ¨μΉ¨ν λ―ΈλΆκ°μ μΉκ΅¬. μ€λͺμ λ€μ λ μΌλ¨ κ·μ λ€μ΄μ€μ§λ§ μ§μ  κ΅¬ν λ¨κ³λ κΉλ§λνλ€. κ°μμ κ΄λ ¨λ λΌλ¬Έμ μμ½νμ¬ νμκ³Ό κ³΅μ νκΈ°λ‘ νλ€. λ¨μ΄ μ΄ν΄ν  μ μλ κΈμ μ°λ €λ©΄ λμ²΄ μΌλ§λ κ³ λ―Όν΄μΌ νλκ±ΈκΉ. λͺ¨μͺΌλ‘ λ­κ° μ»μ μ μλλ‘ μ΄μ¬ν μ’ ν΄. μ€λμ λμ μλ₯Έμ€νΈ.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Max%20Ernst_1921_The_Elephant_Celebes.jpg"></p>
<p align="center">Max Ernst, &ltThe Elephant Celebes&gt, 1921. Oil on canvas, 125.4x107.9cm.</p>

- Day 26 λ§μΉ¨.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day25/Note.md "Day25 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day27/Note.md "Day27 Note")
