import heapq
from collections import Counter
from itertools import permutations, combinations

이진탐색


def binarysearch(data, search):
    if len(data) == 1 and data[0] == search:
        return True


    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False
        medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search < data[medium]:
            return binarysearch(data[:medium], search)
        else:
            return binarysearch(data[medium:],search)

def dfs(data, start_node):
    need_visit, visited = list(), list()
    sum_time = 0
    graph = 0
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.append(graph[node])

            n = int(input('사람수?'))
            time = list(map(int, input('시간'.split(' '))))
            time.sort()
            for i in range(n):
                sum_time += sum(time[:i + 1])

            coin_list = list()
            coin_list.sort(reverse=True)

coin_list = [500, 100, 10, 20]
def minimum_coin(list, value):
    total_count = 0
    detail = list()
    for coin in coin_list:
        coin_num = value // coin
        value -= coin_num * coin
        total_count += coin_num
        detail += (coin, coin_num)
        return detail


def dijkstra(graph, start):
    queue = []
    distance = [0] * 7
    heapq.push(queue, [distance, start])
    while queue:
        current_distance, current_node = heapq.pop(queue)
        if distance[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            new_distance = current_distance + weight
        if new_distance < distance[adjacent]:
            distance[adjacent] = new_distance
        heapq.push(queue, [distance, adjacent])
    return distance

#리스트 컴프리헨션
array = [i for i in range(10)]
print(array)

array = [i for i in range(20) if i % 2 == 1]

# 언더바는 언제 사용?
# 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용. 즉 변수필요없이 단순반복을 할때

for _ in range(5):
    print("Hello World")

#문제 101

a = [1, 4, 3]

# 리스트에 원소 삽입(맨 뒤에 삽입)
a.append(2)
print('삽입: ', a)

# 오름차순 정렬
a.sort()
print('오름차순 정렬: ', a)

# 내림차순 정렬
a.sort(reverse=True)
print('내림차순 정렬: ', a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print('인덱스 2에 3 추가: '.a)

# 특정 값인 데이터 개수 세기
print('값이 3인 데이터 개수: ', a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print('값이 1인 데이터 삭제: ', a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_list 에 포함되지 않은 값만을 저장
result = {i for i in a if i not in remove_set]
print(result)

# 큰 따음표를 문자열안에서 사용할때
data = 'Do you know \"Python\"?'

# 문자열 연산
a = 'Hello'
b = "World"
print(a + " " + b)

a = 'Hello'
print(a * 3)

a = "ABCD"
print(a[-1:0])

# 튜플 자료형
# 튜플은 한 번 선언된 값을 변경할수 없습니다
# 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())을 이용합니다
# 튜플은 리스트에 비해 상대적으로 공간 효율적입니다.

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # 튜플은 초기화할때 이처럼 소괄호를 이용해서 초기화한다
print(a[3])
print(a[1:4])

# 튜플을 사용하면 좋은 경우
# 서로 다은 성질의 데이터를 묶어서 관리해야 할때
# *최단경로 알고리즘에서는(비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용합니다.

# 리스트보다 메모리를 효율적으로 사용해야 할때

# 사전 자료형
# 사전 자료형은 키(key)와 값(Value)의 쌍을 데이터로 가지는 자료형입니다.
# 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는것과는 대비됩니다.
# 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한(Immutable) 자료형'을 키로 사용할수있습니다.
# 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.
# 키(key)값으로 접근 가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
if '사과' in data:
    print("사과'를 키로 가지는 데이터가 존재합니다")

# 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원
# 키 데이터만 뽑아서 리스트로 이용할때는 keys() 함수를 이용
# 값 데이터만을 뽑아서 리스트로 이용할때는 values()함수를 이용

# 키 데티터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

# 집합 자료형
# 집합은 다음과 같은 특징이 있음
# 1. 중복을 허용하지 않음
# 2. 순서가 없음

# 집합은 리스트 혹은 문자열을 이용해서 초기화할수있음
# 이때 set()함수를 이용
# 혹은 중괄호({}) 안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있음
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능

# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)  # 중복되는 원소 제거된후 출력됨

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 사전 자료형과 집합 자료형의 특징
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
# 사전 자료형과 집합 자료형은 순서가 없기때문에 인덱싱으로 값을 얻을 수 없음
# 사전의 키(key) 혹은 집합의 원소(element)를 이용해 O(1)의 시간 복잡도로 조회

# 자주 사용되는 표준 입력 방법

# input() 함수는 한 줄의 문자열을 입력 받는 함수입니다.
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용합니다.
# 예시) 공백을 기준으로 구분된 데이터를 입력 받을때는 다음과 같이 사용합니다.

list(map(int, input().split()))

# 예시) 공백을 기준으로 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다.

a, b, c = map(int, input().split())

# 무조건 외워!!
n = int(input())
data = list(map(int, input().split()))

# 빠르게 입력받기
# 사용자로부터 입력을 최대한 빠르게 받아야하는 경우
# 파이썬의 경우 sys 라이브러리에 정의되어있는 sys.stdin.readline() 메서드를 이용합니다.
# 단 입력후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip()메서드를 함께 사용합니다

# 파이썬에서 print()함수를 사용할때 각 변수에 콤마(,)를 이용하면 띄어쓰기로 구분하여 출력할수있습니다.
# print()는 기본적으로 출력 이후에 줄 바꿈을 수행합니다.
# 줄바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있습니다.

a = 1
b = 2
print(a, b)
print(7, end=' ')
print(8, end=' ')

# 출력할 변수
answer = 7
print('정답은' + str(answer) + '입니다')
# str() = 정수형 데이터를 문자형으로 바꾸기

# f- string 예제
# 문자열 앞에 접두사 'f'를 붙여 사용
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을수있습니다.
answer = 7
print(f"정답은 {answer} 입니다.")


# 파이썬의 continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할때 continue를 사용합니다.
# 1 부터 9까지 홀수의 합을 구할때 다음과 같이 작성 할 수 있습니다.
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i
    print(result)

# 학생들의 합격 여부 판단 예제
# 1) 점수가 80 점만 넘으면 합격
scores = [90, 63, 55, 77, 94]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# 2) 특정 번호의 학생은 제외하기
scores = [90, 85, 77, 54, 92]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue  # 다음 인덱스로 넘어감
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# 중첩된 반복문: 구구단 예제
for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i * j)


# 람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]


print(sorted(array, key= lambda x: x[1]))
# x를 x[1]기준으로 sort하라는 뜻

# 람다 표현식 예시: 여러개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

resutl = map(lambda a, b: a + b, list1, list2)
# map(함수, 리스트)
print(list(result))

# 자주 사용되는 내장 함수
# sum
result = sum([1, 2, 3, 4, 5, ])
print(result)

# min(), max()
min_result = min(7, 4, 5, 2)
max_result = max(3, 5, 7, 4)
print(min_result, max_result)

# eval()
result = eval('(3+5)*7')
print(result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reversed=True)
print(result)

# 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는것
# {'A', 'B', 'C'} 에서 두개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))
print(result)

# 조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는것

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# Counter
# 등장 횟수를 세는 기능을 제공
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇번씩 등장했는지 알려줌

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)  # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
#최대 공약수를 구해야 할때는 math 라이브러리의 gcd() 함수를 이용할수 있다
import math

# 최소 공배수 (LCM)를 구하는 함수


def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14
print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산
print(lcm(21, 14))  # 최소 공배수 (LCM) 계산

#탐욕 알고리즘
#현재 상황에서 지금 당장 좋은 것만 고르는 방법 의미
# 알고리즘 문제를 풀기위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 그리디 해법은 그 정당성 분석이 중요
# 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할수 있는지 검토해본다.

# 그리디 알고리즘 문제1: 거스름돈
# 사진 103
coin_list =[500, 100, 50, 10]
coin_list.sort()


# 답안
n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
n = int(input())
k = int(input())
for coin in array:
    count += n // coin
    n %= coin  # 나머지를 n에 다시 담기
    # ex, 1260 % 500 = 260
    print(coin)

    count = 0
    while n == 1:
        count += n // k
        n %= k

