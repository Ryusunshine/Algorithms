# 퀵 정렬(Quick sort)

# 기준점(pivot 이라고 부름)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right) 으로 모으는 함수를 작성함
# 각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
# 함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right) 을 리턴함
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 퀵 정렬은 평균의 경우O(NlogN)의 시간 복잡도를 가진다.
# 하지만 이미 정렬된 배열에 대해서는 최악의 경우 O(N**2)의 시간 복잡도를 가진다.


# 3. 알고리즘 구현
# quicksort 함수 만들기
# 만약 리스트 갯수가 한개이면 해당 리스트 리턴
# 그렇지 않으면, 리스트 맨 앞의 데이터를 기준점(pivot)으로 놓기
# left, right 리스트 변수를 만들고,
# 맨 앞의 데이터를 뺀 나머지 데이터를 기준점과 비교(pivot)
# 기준점보다 작으면 left.append(해당 데이터)
# 기준점보다 크면 right.append(해당 데이터)
# return quicksort(left) + pivot + quicksort(right) 로 재귀 호출
# 리스트로 만들어서 리턴하기: return quick_sort(left) + [pivot] + quick_sort(right)


def qsort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list() #left, right에 해당하면 넣을 각 리스트를 만든다
    pivot = data[0]
    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    # 데이터 길이가 2 이상이면 다시 이 과정을 반복해야하므로 재귀함수 호출
    # pivot 를 그냥 더하면 숫자를 더하게되는것이므로 리스트형태 [] 로 만든다
    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100),10)
#print(qsort(data_list))


#list comprehension을 사용하여 더 깔끔하게 작성
def qsort2(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item] # 슬라이싱을 통해 하나씩 반환하는데 조건에 맞는 애들만 반환
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100),10)
print(qsort2(data_list))


