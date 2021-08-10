## 🔍 지난 질문들

- SVD 특이값 분해
  - Q. SVD에서 Singular value가 원래 크기 순으로 정렬되어 있는가?
  - 맞습니다.
  
## 📒 강의 관련 질문

- Q. Adadelta : 실제로 거의 사용하지 않는 이유는 성능이 낮기 때문인가요?
  - 성능이 낮다기 보다 learning rate가 없어 최적화가 관여할 요인이 없다.
  - 다른 optimizer가 일반적으로 학습에 관여할 부분이 많아 성능이 더 잘나온다.

## 📌 선택과제 1번 ViT 관련 질문

- Q. Transformer encoder 구현할 때 residual 부분이 다른 코드와 비교했을때, class로 구현하지 않더라도 맞나요?
  - 맞습니다.

- Q. attention visualization에서 error가 납니다.
  - slack에서 다른 캠퍼분께서 수정하는 부분을 알려주셨다.
  - 수정하지 않고도 attention을 리스트에 append하면서 shape을 맞추었더니 작동했다.

- Q. position embedding을 할때 random한 값을 넣는 이유?
  - 학습하는 값으로 생각해 랜덤하게 생성한 후 더해주었다.

- Q. cls_token과의 concat으로 x의 shape이 어떻게 바뀌는 건가요?
  - x의 shape이 (1, 49, 16)에서 concat으로 (1, 50, 16)이 된다.
  - 이후 position의 shape이 (50, 16)이므로 x와 position을 더하는 과정에서 broadcasting이 일어난다.

- Q. nn.linear mlp와의 차이가 없는건가요?
  - nn.linear는 layer 그 자체로 fully connected된 선형변환이라고 생각.
  - mlp는 activation function이 들어갔다.

- Q. colab과 구글드라이브에서 데이터 저장이 마운트 없이 가능한가요?
  - 가능하지만 구글드라이브에 저장하면 다운로드도 가능하다.

- 해결하지 못한 질문들은 대부분 아직 배우지않은 모델에서 나왔습니다. 이후 멘토님과의 시간에서 질문하기로 했습니다.

- Q. attention을 넣을때 list를 만들어 넣어도 잘 작동하는 이유는 무엇인가요?

- Q. transformer에 들어가는 latent vector는 각각의 patch를 의미하나요?

- Q. self-attention의 shape이 768 -> 64 ->768로 바뀌는데 어떻게 되는건가요?
