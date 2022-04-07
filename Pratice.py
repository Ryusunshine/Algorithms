# 코딩 테스트 학습 팁
# 알고리즘을 익힌 후, 해당 알고리즘과 관련된 문제만 연이어서 쭈욱 풀어보는 방식이 가장 좋습니다
# 처음 알고리즘을 익힐 때는 알고리즘을 익힐 때 풀이한 문제를 중심으로 하되,
# 필요하면 감을 가지기 위해 여기에 최대한 가장 쉬운 한 두 문제를 푸시고, 전체 알고리즘을 다 익힌 후, 가능하면
# 각 알고리즘별로 며칠동안 해당 알고리즘 관련 문제만 묶어서 연이어 풀어보세요!

# 동적계획법의 핵심은 ****점화식****을 빨리 찾는것이다
# 코드 작성 패턴
# 1. 빈리스트 만들기(입력값에 따른)
# 2. 초기값을 설정(1번일때, 2번일때)
# 3. 점화식 기반으로 계산값 적용하기( dp[1] = 1, dp[n] = dp [n - 1] + dp[ n -2 ]
# 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기

# 풀이 전략
# 점화식을 만들자
# 점화식이란, 이웃하는 두개의 항 사이에 성립하는 관계를 나타낸 관계식을 의미
# 예: dp[ n ] = dp [ n - 1 ] + dp [ n - 2 ]

# 연습1
# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 1. 빈리스트 만들기
dp = [0] * 1001

# 2. 초기값 설정
dp[1] = 1  # 경우의 수가 1
dp[2] = 2

# 3. 점화식 기반으로 계산값 적용하기
for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2]

# 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
# print(dp[2])

# 전체 코드
n = int(input('숫자입력'))
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for index in range(3, 1001):
    dp[index] = dp[index - 2] + dp[index - 1]
print(dp[n] % 10007)

# 일반적인 동적 계획법 문제는 통상 코드 자체는 간결하므로, 가장 적은 경우이 수부터 계산을 해본 후, 패턴을 찾아. 식(점화식)을 세우는 것이 핵심이다.

# 연습2
# 문제 : https://www.acmicpc.net/problem/9461


p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1

n = int(input('n입력'))
for index in range(3, n + 1):  # 97 + 3 은 100이라서
    p[index] = p[index - 3] + p[index - 2]

print(p[n])

# 연습3
# 문제: https://www.acmicpc.net/problem/1904

n = 4
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for index in range(3, n + 1):
    dp[index] = ( dp[index - 1] + dp[index - 2] ) % 15746
print(dp[n])

