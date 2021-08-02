def digits_to_words(input_string):
    """
    인풋으로 받는 스트링에서 숫자만 추출하여 영어 단어로 변환하여 단어들이 연결된 스트링을 반환함
    아래의 요건들을 충족
    * 반환하는 단어들은 영어 소문자
    * 단어들 사이에는 띄어쓰기 한칸
    * 만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환
    """
    dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
    letters = []
    for i in range(len(input_string)):
      if input_string[i] in dic:
        letters.append(dic[input_string[i]])
    digit_string = " ".join(letters)
    return digit_string
  

def to_camel_case(underscore_str):
    """
    'underscore variable' 에서 'camelcase variable'으로 변환함
    * 앞과 뒤에 여러개의 'underscore'는 무시
    * 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환
    """
    if '_' not in underscore_str:
      return underscore_str
    camelcase_str = ''.join(word.title() for word in underscore_str.split('_'))
    if len(camelcase_str) != 0:
      camelcase_str = camelcase_str[0].lower() + camelcase_str[1:]
    return camelcase_str
