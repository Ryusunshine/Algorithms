# 이진 탐색 (Binary Search) 이란?

# 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법
# 검색할 숫자 (search) > 중간값 이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
# 검색할 숫자 (search) < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.

# 코드-1
def binary_search(data_list, search):
    if len(data_list) == 1 and search == data_list[0]:
        return True
    if len(data_list) == 1 and search != data_list[0]:
        return False
    if len(data_list) == 0:
        return False

    medium = len(data_list) // 2
    if search == data_list[medium]:
        return True
    else:
        if data_list[medium] < search:
            return data_list[medium + 1:], search
        else:
            return data_list[:medium - 1], search


import random

data_list = random.sample(range(100), 10)
data_list.sort()  # sort()함수는 원본 데이터를 바꿈
print(data_list)
test = binary_search(data_list, 66)
print(test)


# 코드-2
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾고자 하는 데이터가 중간값일 경우 그대로 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
            return None

#파이썬 이진 탐색 라이브러리
# bisect_left(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right
a = [1,2,4,4,5]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x)

# 이진 탐색 라이브러리를 활용하여 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index # 해당 범위에 속하는 인덱스 개수 반환

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터 개수 출력
print(count_by_range(a,4,4)

#값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# 파라메트릭 서치(parametric search)
# 파라메트릭 서치란 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용해서 해결할수있다.
