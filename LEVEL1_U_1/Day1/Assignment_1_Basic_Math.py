import numpy as np


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함
    """
    greatest_number = max(number_list)
    return greatest_number
  

def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함
    """
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.
    """
    mean = np.mean(number_list)
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.
    """
    median = np.median(number_list)
    return median
