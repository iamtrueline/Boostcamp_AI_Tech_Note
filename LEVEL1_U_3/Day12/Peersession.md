## 📒 금일 질문 목록

- nn.Linear에서의 크기 변환의 원리는 어떻게 되는가?

  - Linear(NH, NH) 이므로 H값이 변경
  - torch.swipdim(input, dim0, dim1)

- Hook의 실제 사용 사례는 대표적으로 어떤게 있는가?

  - CNN모델에서 filter 설계에 사용되는것으로 알고있다.

- register_forward_pre_hook(), register_forward_hook(), register_full_backward_hook() 의 차이는 무엇인가?

  - forward_pre_hook():
  - forward가 진행되기 전에 어떠한 작용을 하겠다
  - pre_hook : parameter가 어떻게 변하는지 확인할 때 사용, input밖에 없다.
  - full_hook: input output이 있다.

- Apply 문제 해결을 방법은 어떤것이 있는가?

  - apply를 이용하거나 split을 사용하여 해결할 수 있다.

- 일반적으로 Model에서 Parameter정의를 하는데 외부에서 Parameter 정의가 가능한가?

  - 명확한 해답을 결론짓지 못했다.
  - 
## 📎 금일 과제 분석

- Dataloader의 num_workers는 무엇인가?

  - 데이터를 불러올때 사용하는 서브 프로세스(subprocess) 개수이다.

- collate_fn의 역할은 무엇인가?

  - [[data1, data2, ...], [label1, label2, ...]] → [[data1,label1],[data2,label2],...]

- batch_size 문제

  - 명확한 해답을 결론짓지 못했다.
