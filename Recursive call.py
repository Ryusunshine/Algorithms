# 재귀 용법 (recursive call)

# 함수안에서 자기 자신을 다시 호출하는 함수
# 재귀 호출은 스택의 전형적은 예
# 함수는 내부적으로 스택처럼 관리한다.


# 연습-1
# 반복적으로 구현한 n!
def factorial(num):
    return_value = 1
    for i in range(1, num + 1):
        return_value = return_value * i
    return return_value

# print(factorial(5))

# 재귀적으로 구현한 n!
def factorial2(num):
    if num < 1:
        return 1
    else:
        return num * factorial2(num - 1)

# print(factorial2(5))


# 연습-2
# 최대공약수 계산(유클리드 호제법)예제
# 두 개의 자연수에 대한 최대공약수를 구하는 대표즉인 알고리즘으로는 유클리드 호제법이 있다.
# 유클리드 호제법
# 두 자연수 A, B 에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성 할 수 있다.

def gcd(a, b):
    if a % b == 0:  # a가 b의 배수라면
        return b
    else:
        return gcd(b, a % b)  # b가 재귀함수로 a자리에 들어가서 반복

# print(gcd(192,162))


# 연습-3
# 숫자가 들어있는 리스트가 주어졌을때, 리스트의 합을 리턴하는 함수를 만드세요(재귀함수를 써보세요)

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


data = [1, 2, 3, 4, 5]
# print(sum_list(data))


# 연습-4
# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함(ex. eye, level)
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요.
# 참고 - 리스트 슬라이싱
# string = 'Dave'
# string[-1] --> e
# string[0] --> D
# string[1:-1] --> av
# string[:-1] --> Dav

def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


string = 'eye'
#print(palindrome(string))


# 연습-5
# 정수 n이 홀수이면 3 X n + 1 을 하고, 짝수이면 n 을 2로 나눕니다.
# 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.

def test5(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return test5(n + 1)
    else:
        return test5(int(n / 2))

#test5(3)


# 연습-6
# 문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1

# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
# (힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면, f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 !패턴! 찾기)

def func(data):
    if data == 1:
        return 1
    if data == 2:
        return 2
    if data == 3:
        return 4
    else:
        return func(data - 1) + func(data - 2) + func(data - 3)

#print(func(5))

# 재귀 호출이 중요한 이유
# 변수 사용 을 줄일 수 있다.
# 변수 사용을 줄여준다는 것은 mutable state(변경 가능한 상태) 를 제거하여 프로그램 오류가 발생할 수 있는 가능성을 줄여준다.
# mutable state 를 최대한 피하는 것은 변수의 수를 줄이는 것과 변수가 가질 수 잇는 값의 종류 또는 범위를 정확히 제한하는것