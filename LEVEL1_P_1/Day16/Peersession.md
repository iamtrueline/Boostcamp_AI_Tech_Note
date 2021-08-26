## 🔍 마스크 데이터 분류 대회

- 어느 부분에 집중하고 있는지?

  - 모델
  - 전처리

- batsize에 대한 custom data 처리 방식

  - collate_fn 사용해줬다. 질문: collate_fn은 필수인가? <- DataLoader를 사용하면 colalte_fn은 필수가 아니다.
  - x와 label를 따로 따로 해주었다.

- Label 새로 생성

  - glob 사용
  - 규칙을 발견해서 코드 작성

- DataLoader

  - 이미지 폴더 모듈 관련 :torchvision안에 있는 ImageForder 
  - 장점 : labeling이 어느정도 되어 있어서 전처리시 편리
  - 단점 : 복사로 인한 메모리 차지 
  - tranforms 함수 중에서-  getitem관련 문제 

- 모델 관련

  - VGG  + 2 layer추가 = 높은 validation 값
  - wild-resnet : train set 에서 90%까지 나옴 but overfiting 조심해야 된다.
  - 정확도가 터무니없게 나올때 어디부분이 잘못된 것인지 확인할 수 있는 방법?

- 학습 관련

  - train, validation split 
  - transform에서 normalization해주는 이유
  - 불균형을 해결할 수 있다.
  - 속도가 빨라진다. 
  - 예를 들어서 MNIST에서 반전시킬 경우255값에 치우쳐있게 된다. 이럴때 분산에 정도를 줄여줄 수 있다.

- EDA 활용에 대해서

  - 마스크별 RGB histogram,  마스크 착용여부 RGM histogram 
  - open cv의 casecadeclassifcation 이용 -> BUT 예전에 만들어진 거라서 성능이 좋지 않다.
  - open cv의 detect_face, detect_gender 이용하면 좋다. <- 모든 이미지에 대해서 bounding box를 찾아서 활용하면 좋지 않을까 싶다. 잘못된 라벨링에 대한 문제를 해결할 수 있다.
  - PCA를 활용해보자
  - 공개 코드 -> range(len())부분 오타 : 지워주면 될 것 같다.

- 기타

  - CrossEntropy함수 안에서 자동으로 softmax를 취해준다.
