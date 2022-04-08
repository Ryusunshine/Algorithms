# 병합 정렬(merge sort)

# 재귀용법을 활용한 정렬 알고리즘
# 1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다

# 알고리즘 구현
# mergesplit 함수 만들기
# 만약 리스트 갯수가 한개이면 해당 값 리턴. 그렇지 않으면, 리스트를 앞뒤, 두 개로 나누기
# left = mergesplit(앞)
# right = mergesplit(뒤)
# merge(left, right)

# merge 함수 만들기

# 리스트 변수 하나 만들기 (sorted)
# left_index, right_index = 0
# while left_index < len(left) or right_index < len(right):
# 만약 left_index 나 right_index 가 이미 left 또는 right 리스트를 다 순회했다면, 그 반대쪽 데이터를 그대로 넣고, 해당 인덱스 1 증가
# if left[left_index] < right[right_index]:
# sorted.append(left[left_index])
# left_index += 1
# else:
# sorted.append(right[right_index])
# right_index += 1

# 재귀용법을 활용해서 다음 코드 작성해보기

# mergesplit 함수 만들기
# 만약 리스트 갯수가 한개이면 해당 값 리턴
# 그렇지 않으면, 리스트를 앞뒤, 두 개로 나누기
# left = mergesplit(앞)
# right = mergesplit(뒤)
# merge(left, right)

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

# merge 함수 만들기
# 목표: left와 right의 리스트 데이터를 정렬해서 sorted_list 라는 이름으로 return하기
# left와 right는 이미 정렬된 상태 또는 데이터가 하나임
#  ↓       ↓
# [1 , 2] [3, 4]

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - right 데이터가 없을때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - left 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

import random

data_list = random.sample(range(100), 10)
mergesplit(data_list)