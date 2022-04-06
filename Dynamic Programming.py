# 동적 계획법

# 연산이 반복되는 결점을 보완하기 위해서 동적 계획법(Dynamic Programing, DP)이 고안됨.
# 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘
# 상향식 접근법으로, 가장 최하위 해답을 구한 후, 이를 저장하고, 해당 결과값을 이용해서 상위 문제를 풀어가는 방식
# Memoization 기법을 사용함
# Memoization (메모이제이션) 이란: 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술
# 문제를 잘게 쪼갤 때, 부분 문제는 중복되어, 재활용됨 (예: 피보나치 수열)

# 피보나치 수열 recursive call 활용
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

print(fibo(3))

# 동적 계획법 활용
def fibo_dp(num):
    cache = [ 0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]

    return cache[num]

print(fibo(10))

# cache[2]은 cache[1](=1) + cache[0](=0)이라서 cache[2] = 1이 된다.
# 이걸 재귀적으로 반복하면
# cache[3] = cache[2] + cache[1] = 1 + 1 = 2


