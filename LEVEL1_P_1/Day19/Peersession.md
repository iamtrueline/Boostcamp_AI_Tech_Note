## 🔍 질의응답

- K-fold
- Boosting & Bagging

  - boosting : 직렬적. 모델의 성능에 따라 가중치를 줘서 결과를 내는 것. 하나의 모델을 통과하고 다음 모델을 통과할 때 부족한 부분을 개선. Bias가 높을 때 사용.
  - bagging : 병렬적. 각 모델을 통과해서 나온 결과값들을 다수결 또는 가중치를 이용하여 Output 출력. Varience 가 높을 때 사용.

## 📒 코드리뷰

- 성욱 캠퍼님 : Agumentation 추가. EDA를 통해 확인한 Age, Gender 별 데이터 불균형 해소 시도. HorizontalFlip, GausianNoise 등 다양한 transform 이용하여 agumentation 수행. 데이터 회전 시 발생하는 빈 공간 처리는 shift scale rotate 를 사용했다.
- 진선 캠퍼님 : Age 부분 Classification acc 문제 해결 시도, Data agumentation 수행
- 원진 캠퍼님: ResNext를 이용하여 acc 개선 시도, Data agumentation 수행
- 범수 캠퍼님: Bbox 를 이용하여 Data agumentation 계획 및 구상
- 승찬 캠퍼님: Data agumentation 수행 및 모델 개선 시도
- 우창 캠퍼님: Underfitting 시도 및 모델, 데이터 갯수, agumentation 여부 등 분석

## 📎 향후 팀프로젝트 계획

- 팀 단위 제출로 인한 제출횟수를 고려하여, 가장 성능이 좋은 모델을 basecode로 하여 각각 다양한 시도를 하는 방향 고려

## 📎 팀 회고지 피드백
