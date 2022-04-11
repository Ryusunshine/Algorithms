# 최단 경로 문제
# 두 노드를 잇는 가장 짧은 경로를 찾는 문제임
# 가중치 그래프 (Weighted Graph) 에서 간선 (Edge)의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적

# 다익스트라 알고리즘
# 하나의 정점에서 다른 모든 정점 간의 각각 가장 짧은 거리를 구하는 문제
# 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사


# 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
# 우선순위 큐는 MinHeap 방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨
# 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 인접 노드 간의 거리부터 먼저 계산한다
# 그리고 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트
# 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
# 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
# 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
# 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음


# 코드 - 느린 코드
graph = [  # 노드의 넘버, 그 노드까지의 거리
    None,
    [[2, 2], [3, 5], [4, 1]],
    [[3, 3], [4, 2]].
    [[2, 3], [6, 5]]
    [[3, 3], [5, 1]],
    [[3, 1], [6, 2]],
    [],
]


def get_smallest_node(min_distances, visited):  # 방문하지않은 노드중 작은 노드 찾기
    min_value = 1e9
    node_number = 1
    for i in range(1, 7):  # 1번부터 도는 이유는 None, 무시할값이라서, 처음은 0임
        if min_distances[i] < min_value and not visited[i]:
            min_value = min_distances[i]
            node_number = i
            return node_number



def dijkastra(graph, visited, min_distances, start_node):
    min_distances[start_node] = 0  # 시작노드는 자기 자신으로 가는거리니깐 0
    visited[start_node] = True  # 그리고 방문처리
    for next_node in graph[start_node]:  # 시작노드와 연결된 다음 노드들이
        min_distances[next_node[0]] = next_node[1]  # 업데이트 해주기.더이상 무한대가 아니라 graph상의 노드와 연결된 거리들을 정보를 업데이트

        for _ in range(len(min_distances) - 2):  # 출발 노드를 제외한 나머지노드들 중에서 반복. _는 쓰지않는변수를 뜻함
            current_node = get_smallest_node(min_distances, visited)  # 방문하지않은 노드중 가장 짧은 노드를 찾아 고르면 방문ㄱ
            visited[current_node] = True  # 그 노드를 방문처리
            for next_node in graph[current_node]:  # 그 노드와 연결된 다른 노드들을 순회를 하면서
                    cost = min_distances[current_node] + next_node[1]  # 지금의 노드까지의 거리와 다음 노드까지의 거리의 합이 cost로 저장하고
                    if cost < min_distances[next_node[0]]: # 만약 다음노드까지의 거리의 합이 기존의 거리보다 작으면 갱신해준다.
                        min_distances[next_node[0]] = cost

INF = 1e9
min_distances = [INF] * 7
visited = [False] *7

# 코드- 2
from collections import deque
import heapq

def dijkstra_fast_ver(graph, visited, min_distances, start_node):
    #출발노드를 처리한다
    q =[] # 이 빈 배열을 priority queue로 쓴다
    heapq.heappush(q,[0, start_node]) #q에다가 push를 할때 priority queue처럼 push를 할건데 우선순위를 처리할 노드를 쓴다. heapq를 이용하면은 값이 작은게 우선순위라서 자동으로 최단이 뽑힌다.
    min_distances[start_node] = 0 #거리 갱신시킨다

    while q: #큐에 텅 빌때까지 반복
        current_node_info = heapq.heappop(q)# q에서 하나빼면 최단거리가 튀어나옴
        if min_distances[current_node_info[1]] < current_node_info[0]:# current_node[0] = 노드, 현재 계산된 노드까지의 거리가 current_node_info[0] 기존의 노드 거리보다 작으면 pass아니면 반복문돌면서 확인
        for next_node in graph[current_node_info[1]]:
            cost = min_distances[current_node_info[1] + next_node[1]]
            if cost< min_distances[next_node[0]]:
                min_distances[next_node[0]] = cost
                heapq.heappush(q, [cost, next_node])

# 코드 - 3 다른방식

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:  # 큐에 더이상 데이터가 없을때까지 반복
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

# 최단 경로 출력하기

import heapq


# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances


# 방향 그래프
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A', 'F'))