# 📙 Note

### Intro to NLP, Bag-of-Words

- 자연어 처리

  - 자연어 처리 : 크게 컴퓨터가 주어진 단어나 문장, 문단 등 글을 이해하는 과정과 생성하는 과정 두가지로 분류.
  - 최신 기술은 ACL, EMNLP, NAACL 등에서 발표.
  - Low-level parsing : 주어진 문장을 단어 단위로 쪼개고(Tokenization), 어미 변화등을 없앤 어근을 추출(stemming).
  - Word and parase level : 고유명사를 가리는 Named entity recognition(NER), 품사를 판단하는 Part of speech(POS) 등.
  - Sentence level : 긍정 부정 어조 분류, 기계 번역 등.
  - Multi-sentence and paragraph level : 두 문장간 논리 판단, 질답, 대화 시스템, 요약 등.
  - 질답 과제에 관련하여 예를 들면, 검색 시스템의 경우 이제 검색어를 리스트로 나열할 뿐 아니라 질문에 대한 요지를 판단하고 최상단에 답변을 바로 달아준다.
  - Text mining : 긴 기간의 기사들을 모아 키워드 및 데이터를 분석하고 트렌드를 분석. 상품 반응 분석. 소셜 관계나 사회 반응 분석 등. 특정 분야에 대한 텍스트, 문서를 군집화해서 분석한다. KDD, WebConf(WWW), WSDM, CIKM, ICWSM등에서 최신 동향 발표.
  - Information retreval : 검색 성능 고도화. 검색 기술은 어느 정도 성숙한 상태에 이르렀다고 본다. 추천시스템이 이 영역. SIGIR, WSDM, CIKM, RecSys등에서 최신 동향 발표.

- 자연어 처리 동향

  - Word2Vec, Glove를 통해 텍스트 시퀀스 내 단어를 특정 차원 벡터로 임베딩. 이 때 시퀀스는 순서 정보를 포함한다.
  - 시퀀스 처리에 특화된 RNN 모델(LSTM, GRU)이 자연어 처리의 핵심 모델로 자리잡음.
  - Transformer 모델 등장(Attention is all you need). 큰 성능 향상 이룩. 현재 대부분 이 모델을 채택한다. Transformer는 자연어 뿐 아니라, 영상, 시계열 예측 등에도 다양하게 사용됨.
  - Transformer를 포함한 대부분의 고급 NLP 모델은 원래 기계 번역 작업을 개선하기 위해서 개발되었다.
  - 이전엔 NLP 테스크마다 분리된 맞춤형 모델이 있었다. 현재는 범용 사전학습모델에 전이학습 시키는 등으로 사용한다. 기존의 맞춤 모델보다도 월등해진 성능을 보여줌.
  - 자가지도학습(self-supervised training) : 제한적인 인공지능에서 범용으로 나오는 데 기여한 방법.
  - 학습엔 돈이 필요하다. 그래서 큰 기업이 주축.

- Bag-of-Words

  - Step 1 : 주어진 문자에서 쪼갠 단어들 중 중복을 제거하고 나열하기.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img00.PNG" alt="Bag-of-Words"></p>

-
  - Step 2 : 나열된 단어를 Categorical variable로 보고 각각 원핫벡터로 표현. 이 때 모든 단어쌍의 유클리디안 거리는 루트2. 유사도는 0.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img01.PNG" alt="Bag-of-Words"></p>

-
  - Step 3 : 이후 판단할 문장들은 이 원핫벡터를 더한 형태로 표현.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img02.PNG" alt="Bag-of-Words"></p>

-
  - 이렇게 문장(벡터)의 카테고리를 판단하는 것은 Classifier의 몫.

- NaiveBayes Classifier for Document Classification

  - 특정 문서 d가 C개 각각 클래스에 속할 확률 분포는 P(c|d).
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img03.PNG" alt="NaiveBayes Classifier"></p>

-
  - 각 단어(w)가 나타날 확률이 독립이라면 다음 식으로도 표현 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img04.PNG" alt="NaiveBayes Classifier"></p>

-
  - 예제. CV 카테고리 문서 2개, NLP 카테고리 문서 2개. 새로 들어온 문서는 어느 카테고리일까?
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img05.PNG" alt="NaiveBayes Classifier"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img06.PNG" alt="NaiveBayes Classifier"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img07.PNG" alt="NaiveBayes Classifier"></p>

  - NaiveBayes Classifier는 train에 특정 단어가 포함되지 않는다면 확률값은 0. 따라서 학습되지 않은 단어가 등장할 땐 해당 문서가 설령 이미 학습된 카테고리에 속하더라도(유사도가 높더라도) 분류를 정확하게 해낼 수 없다.

### Word Embedding

- Word Embedding

  - Word Embedding : 자연어의 단어를 정보의 기본단위로 책정하고 각 단어를 특정 차원 벡터로 변환.
  - 기본 아이디어는 비슷한 단어는 비슷한 위치. 유사한 단어간 거리는 짧고 그렇지 않은 단어간 거리는 길 것.

- Word2Vec

  - 인접 단어에서 단어의 벡터 표현을 교육하기 위한 알고리즘. 단순히 원핫벡터만 사용하면 유사도는 고려할 수 없었다. 이를 보완하기.
  - 유사한 맥락의 단어는 비슷한 의미를 가질 것이다라는 가정을 전제한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img08.PNG" alt="Word2Vec"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img09.PNG" alt="Word2Vec"></p>

-
  - 슬라이딩 윈도우 : 앞뒤 단어쌍을 함께 고려. 값이 3이라면 증심단어의 앞뒤 1글자씩을 추가해 총 3개 단어로 중심단어 쌍 구성.  
  - 주어진 학습 데이터를 단어별로 Tokenization 후 유의미한 단어들로만 사전을 구성 -> 원핫벡터로 구성 -> 슬라이딩 윈도우 방식을 차용하여 단어쌍을 구성하고 단어간 유사도 계산
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img10.PNG" alt="Word2Vec"></p>

-
  - 결과로 나오는 벡터 간 거리는 비슷한 관계일 경우 비슷하게 나타난다. ex) vec[queen] – vec[king] = vec[woman] – vec[man]
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img11.PNG" alt="Word2Vec"></p>

-
  - 학습 참조 : 학습 https://ronxin.github.io/wevi , 한국어 http://w.elnn.kr/search , 단어유사 http://wonjaekim.com/archives/50 , 의미가 가장 상이한 단어 서치 https://github.com/dhammack/Word2VecExample
  - Word2Vec은 다양한 자연어처리 영역에서 활용된다. 단어 유사도, 기계 번역, Part-of-speech(PoS) tagging, Named entity recognition(NER), 감정 분석, 클러스터링, Semantic lexicon building, 이미지 캡셔닝 등.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img12.PNG" alt="번역"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img13.PNG" alt="Semantic lexicon building"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img14.PNG" alt="이미지캡셔닝"></p>

- GloVe

  - 입력 및 출력 워드의 각 쌍을 검토하는 대신 먼저 한 윈도우 내 단어의 빈도를 먼저 계산. 중복계산을 줄여서 Word2Vec보다 학습이 빠르고 작은 데이터에서도 잘 동작한다.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img15.PNG" alt="GloVe"></p>

-
  - 빈번하게 등장하는 단어쌍을 Word2Vec은 모두 계산했지만 GloVe는 한 번만 취함.
  - 추천 시스템에 많이 쓰인다.
  - Word2Vec 예시와 같이, 성별의 차이뿐인 단어간의 거리, 강조 차이뿐인 단어간의 거리 등이 일정한 것을 확인 가능.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img16.PNG" alt="GloVe"></p>
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/day25_img17.PNG" alt="GloVe"></p>

  - 오픈 소스 참조 : https://nlp.stanford.edu/projects/glove

# ✏️ Doodle

- 새로운 U스테이지, 새로운 팀. 이제 NLP에 집중하는 강의를 듣고 다음 P스테이지를 준비한다. 항상 계획의 첫날은 의욕 넘치기 마련이니 이번에도 그 효과 덕을 보길 바란다. 특별한 이슈가 없는 특별한 날. 오늘의 끝은 르네.
<p align="center"><img src="https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/Rene_Magritte_1953_Golconda.jpg"></p>
<p align="center">René Magritte, &ltGolconda&gt, 1953. Oil on canvas, 81x100cm.</p>

- Day 25 마침.

[<p align="center"><img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/back.png" width ="50px" />](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL1_P_2/Day24/Note.md "Day24 Note")   [<img src = "https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/images/next.png" width ="50px" /></p>](https://github.com/iamtrueline/Boostcamp_AI_Tech_Note/blob/main/LEVEL2_U_1/Day26/Note.md "Day26 Note")
