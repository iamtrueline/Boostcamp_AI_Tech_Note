import random


def get_random_number():
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # '''
    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # '''
    result = True if int(user_input_number)>=100 and int(user_input_number)<1000 else False
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    # '''
    temp = ''.join(c for c in three_digit if three_digit.count(c) == 1)
    result = False if len(temp) == 3 else True
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # '''
    result = True if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number)  else False
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # '''
    while(1):
      temp = get_random_number()
      test = test = is_duplicated_number(str(temp))
      if test == False:
        break
    result = temp
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # '''
    s_cnt = 0
    b_cnt = 0
    for i in range(0, 3):
            for j in range(0, 3):
                if random_number[i] == user_input_number[j] and i == j:
                    s_cnt += 1
                elif random_number[i] == user_input_number[j] and i != j:
                    b_cnt += 1
    result = [s_cnt, b_cnt]
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # '''
    result = True if one_more_input.lower() == 'yes' or one_more_input.lower() == 'y' else False
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # '''
    result = True if one_more_input.lower() == 'no' or one_more_input.lower() == 'n' else False
    return result


def main():
    print("Play Baseball")

    while 1:
      random_number = str(get_not_duplicated_three_digit_number())
      print("Random Number is : ", random_number)

      while 1:
        user_input_number = input("Input guess number : ")
        end_check = 0

        if user_input_number == '0':
          print("Thank you for using this program")
          print("End of the Game")
          return

        if is_validated_number(user_input_number) == False:
          print("WRONG INPUT")

        elif get_strikes_or_ball(user_input_number, random_number) == [3, 0]:
          print(random_number, user_input_number, '3 Strikes 0 Balls')
          while(1):
              user_input_code = input("Play again? : ")
              if is_yes(user_input_code):
                end_check = 2
                break
              elif is_no(user_input_code):
                end_check = 1
                break
              else:
                print("WRONG INPUT")

        else:
          print(random_number, user_input_number, get_strikes_or_ball(user_input_number, random_number)[0], 'Strikes', get_strikes_or_ball(user_input_number, random_number)[1], 'Balls')

        if end_check == 1:
          print("Thank you for using this program")
          print("End of the Game")
          return
          
        elif end_check == 2:
          break

    print("Thank you for using this program")
    print("End of the Game")
