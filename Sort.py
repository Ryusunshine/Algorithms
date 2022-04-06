# 버블 정렬(bubble sort)
# 두 인접한 데이터를 비교해서 앞에있는 데이터가 뒤에 있는 데이터보다 크면 자리를 바꾸는 정렬 알고리즘

#알고리즘 구현

# n개의 리스트가 있는 경우 최대 n-1 번의 로직을 적용한다.
# 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정된다
# 로직이 경우에 따라 일찍 끝날 수도 있으므로 로직을 적용할 때는 한번도 데이터가 교환된 적이 없다면 이미 정렬된 상태이므로 더 이상 로직을 반복 적용할 필요가 없다.

def bubblesort(data):

    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data) - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break
    return data

import random
data_list = random.sample(range(100),50)
print(bubblesort(data_list))

# 삽입 정렬(insertion sort)

# 삽입 정렬은 두 번째 인덱스부터 시작
# 해당 인덱스(key값) 이전의 데이터와 비교해서 key값이 더 작으면, B값을 뒤 인덱스로 복사
# 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동하여 자료를 오름차순으로 정렬.

# 알고리즘 구현

# n개의 리스트가 있는 경우 최대 n-1 번의 로직을 적용한다.
# 처음 실행할때는 두번째 인덱스 데이터와 첫번째 인덱스를 비교한후 데이터가 작으면 앞으로 이동.
# 첫번째 for문은 로직 실행 횟수, 두번째 for문은 데이터가 바뀌는 횟수.
# 로직이 경우에 따라 일찍 끝날 수도 있다. 따라서 로직을 적용할 때 한 번도 데이터가 교환된 적이 없다면 이미 정렬된 상태이므로 더 이상 로직을 반복 적용할 필요가 없다.

def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1,0,-1): # 인덱스 i부터 1까지 1씩 감소하여 반복
            if data[index2 - 1] > data[index2]: # 한칸씩 왼쪽으로 이동
                 data[index2], data[index2 - 1] = data[index2 -1], data[index2]
            else:
                break
    return data

import random
data_list = random.sample(range(100),50)
print(insertion_sort(data_list))

#삽입 정렬의 시간 복잡도
# 삽입 정렬의 시간 복잡도는 O(N**2)이며 선택 정렬과 마찬가지로 반복문이 두번 중첩되어 사용된다.
# 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
# 삽입 정렬은 이전의 데이터와 비교해서 자기가 어느 부분에 들어가는지 고르는게 단순 상수로 대체될수있기때문에 최선의 경우 O(N)의 시간 복잡도를 가진다.

# 선택 정렬 (Selection sort)

# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다.

#알고리즘 구현
# 1. 주어진 데이터 중, 최소값을 찾음
# 2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

def selection_sort(data):
    for i in range(len(data)-1):
        lowest_i = i
        for index in range(i+1, len(data)):
            if data[lowest_i] > data[index]:
                data[lowest_i], data[index] = data[index], data[lowest_i]
                lowest_i = index
    return data

import random
data_list = random.sample(range(10),5)
selection_sort(data_list)








