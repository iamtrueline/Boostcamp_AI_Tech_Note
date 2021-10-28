# CycleGAN

- GAN : Generator와 Discriminator, 자강두천결투.
- Generator는 이미지를 생성하고 Discriminator는 이미지가 진짜 이미지인지 Generator가 생성한 이미지인지 판별.
- Generator는 생성한 이미지를 Discriminator가 진짜 이미지로 판단하도록 점점 더 그럴 듯 한 이미지를 생성한다.
- 과정이 반복될수록 Discriminator는 점점 더 진짜 이미지와 생성 이미지를 잘 판별한다.
- CycleGAN : 하나의 이미지 도메인을 다른 이미지의 도메인으로 바꾸는 모델.
- Input dataset과 Target dataset이 존재한다면 그 수가 반드시 동일할 필요는 없음.
- X 도메인에 존재하는 사진을 Y 도메인으로 변환 G, 반대로 Y 도메인의 사진을 X 도메인으로 변환하는 F, 총 두개의 생성자 사용.
- 목적함수는 adversarial losses와 cycle consistency losses, 두 종류의 항으로 구성.
- F(G(X)) 는 X, F(G(Y)) 는 Y로 최대한 근사하는 것이 목표. 이는 순환일관성(Cycle Consistency)으로 표현.
- 참조 : https://junyanz.github.io/CycleGAN/
