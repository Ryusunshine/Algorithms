# 문제 푸는 방법
# 1. 이론과 예제 병행 => 70 문제
# 2. 기출문제 => 백준 프로그래머스(레벨 2 3 4)
# 1주일 월화수목금 2문제 * 5일 = 10문제, 토,일은  복습
# 1문제 레벨2 30분 / 레벨3 45분 / 레벨4 1시간
# 레벨2 3문제 / 레벨3 2문제/ 레벨4 2문제 = 7문제, 5시간
# 무조건 시간지키고서 문제 풀어보기

# 알고리즘 문제 풀이 절차
    # 1. 문제 정확하게 읽기
    # 2. 입출력 받기
    # 3. 문제 풀이 방법 생각
      # 1. 문제 해결 방법을 정리한 후 코드를 작성해야한다
      # 2. 문제 상황을 단순화해야한다.
      # 3. 단순해진 상황을 해결하기 위한 방법을 정리한다.
    # 4. 정리한 방법에 특정한 알고리즘이 도구로 필요하다면 활용한다
        # 1. 그리디 : 매 순간마다 선택시 중에서 최선을 선택하면 최종 결과가 최선인 경우
        # 2. 구현: 매 순간마다 모든 선택지를 전부 고려하는 경우
        # 3. dfs bfs: 주어진 그래프에서 특정 노드로부터 나머지 모든 노드까지 방문하면서 어떤 일을 하는 경우
        # 4. 정렬
        # 5. 이진 탐색: 임의의 범위내에서 어떤 값을 빠르게 찾아야 하는 경우
        # 6. 다이나믹 프로그래밍 : 매 순간마다 모든 선택지를 전부 고려해야 하는데 이전 선택의 결과를 활용해 연산을 최소화할수있는 경우
        # 7. 다익스트라 : 주어진 그래프에서 특성 노드로부터 나머지 모든 노드까지의 최단거리를 확인해야 하는 경우
        # 8. 플로이드 위셜: 주어진 그래프에서 모든 노드끼리의 연결성 및 최단거리를 확인해야하는 경우
        # 9. 유니언 파인드
        # 10. 크루스칼: 주어진 그래프에서 최소 신장 트리를 찾아야 하는 경우
        # 11. 위상정렬
    # 5. 도구가 되는 알고리즘을 어떻게 활용할지 결론까지 정확하게 정리한다.

# 1. 그리디 알고리즘

# 문제 - 1
n, m, k = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
#중간중간에 입력한게 제대로 받았는지 확인해야함
print(n, m, k, numbers)

# 0. 정렬
# 1. 최대를 찾는다
# 2. 최대를 k번 더하자
# 3. 최대 바로 직전의 값을 1번
# 4. 1번으로 돌아가서 반복


# 5 8 4
# 2 4 5 4 6
# 46

# 6665666
numbers.sort(reverse=True)

count = 0
numbers_sum = 0
while True:
    # m 번 보다 크면 반복문 종료
    if count >= m:
        break
    max_num = numbers[0]
    numbers_sum += max_num * k
    second_max_num = numbers[-1]
    numbers_sum += second_max_num #여기까지 더하면 k+1번 더한것
    count += (k+1)

# m번보다 더 더했으면 더 더한만큼 빼주면 돼! 어떻게 할지 생각해봐
if count > m:  #만약 m이 8인데 10번 count됐으면 10(count) - 8(m) 하면 초과로 더해진 2번이 나옴
    if count - m == 1:
        print(numbers_sum - numbers[0])
    else:
        print(numbers_sum - numbers[0] - numbers[1] * (count - m - 1))

print(numbers_sum)

# 구현

# 문제 - 2
# 첫번째 방법
n = int(input())
route = input().split()

# (1,1)
# RRRUDD
current_coord = [1,1] #튜플()은 내부값을 변경할 수 없기때문에 리스트 형태로 쓴다.
for i in range(len(route)):
    direction = route[i]
    if direction == 'R':
        if current_coord[1] == n: #오른쪽으로 갈때는 정해진 범위에서 벗어나면 무시
            continue
        current_coord[1] += 1
    elif direction == 'L':
        if current_coord[1] == 1: #만약 이미 current_coord가 [1,1]이면 왼쪽으로 갈시 범위를 벗어나므로 무시
            continue
        current_coord[1] -= 1
    elif direction == 'U':
        if current_coord[0] == 0: #위로 갈때 좌표가 0이 되면 지도에서 벗어나므로 무시
            continue
        current_coord[0] -= 1
    elif direction == 'D':
        if current_coord[0] == n:
            continue
        current_coord[0] += 1
    print(direction, current_coord)

print(current_coord[0], current_coord[1])

# 두번째 방법 - 더 깔끔한 방법
n = int(input())
route = input().split(" ")

# L R U D
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]
moves = ["L", "R", "U", "D"]

current_coord = [1, 1]
for i in range(len(route)):
    direction = route[i] # route 인덱스를 방향으로 잡으면
    index = moves.index(direction) # list.index(인자)는 인자가 몇번째 인덱스인지 찾아준다.
    next_row = current_coord[0] + d_row[index] # current_coord[0] 이 행
    next_col = current_coord[1] + d_col[index] # 다음 좌표는 현재 좌표에다가 row/col 를 더한값
    if next_row < 1 or next_row > n or next_col < 0 or next_col > n: # 예외처리 : 범위를 벗어나면 무시하는 조건문
        continue
    # 범위를 안 벗어난다면 교체
    current_coord[0] = next_row
    current_coord[1] = next_col

#print(current_coord[0], current_coord[1])


# 문제 - 3
# 상하좌우를 순회하면서 0인지 확인해야돼 = dfs, bfs

# n = 행, m = 열
n, m = map(int, input().split(' '))
graph = [list(map(int, input())) for _ in range(n)]
print(graph)
from collections import deque
visited = [[False] * m for _ in range(n)]
# print(graph)
# print(visited)

# graph의 표현방식 = 인접행렬 / 연결 리스트
# 00110
# 00011
# 11111
# 00000

# L R U D
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]

def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = True
    while queue:
        current_node = queue.popleft()
        for i in range(len(d_row)): # current_node가 방문해야할 연결된 리스트는 4개(즉 행 갯수만큼)
            next_row = current_node[0] + d_row[i]
            next_col = current_node[1] + d_col[i]
            if next_row < 0 or next_col < 0 or next_row > n - 1 or next_col > m - 1: # 갈수있는 범위인지 체크
                continue
            if visited[next_row][next_col] == True: # 그 좌표가 이미 방문처리되었으면
                continue
            if graph[next_row][next_col] == 1: #graph에서 좌표로 가봤는데 1이면
                continue
            queue.append([next_row, next_col]) # 좌표를 넣으면 됨
            visited[next_row][next_col] = True

# 0인지 확인하기 위해 2차원 배열 한번씩 돌기(이중 반복문)
for row in range(n):
    for col in range(m):
        if graph[next_row][next_col] == 0: # 0 이면 방문
            bfs(graph, visited, [row, col])
            count += 1

print(count)






















