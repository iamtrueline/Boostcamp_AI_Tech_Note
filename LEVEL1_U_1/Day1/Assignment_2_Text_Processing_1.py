def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족
    * 모든 단어들은 소문자로
    * 띄어쓰기는 한칸으로
    * 앞뒤 필요없는 띄어쓰기는 제거
    """
    words = input_string.split()
    normalized_string = " ".join(words)
    normalized_string = normalized_string.lower()
    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함
    """
    letters = list(input_string)
    no_vowel_string = ''
    for i in range(len(input_string)):
        if letters[i] not in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
            no_vowel_string += letters[i]
    return no_vowel_string
