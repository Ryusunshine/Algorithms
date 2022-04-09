# 그래프 (Graph) 란?
# 그래프는 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node) 와 간선(Edge)로 표현하기 위해 사용

# BFS 와 DFS
# 대표적인 그래프 탐색 알고리즘
# 너비 우선 탐색 (Breadth First Search): 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식
# 깊이 우선 탐색 (Depth First Search): 정점의 자식들을 먼저 탐색하는 방식

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)


# 깊이 우선 탐색 (Depth-First Search)

# 자료구조 스택과 큐를 활용함
# need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


print('dfs', dfs(graph, 'A'))


# 너비 우선 탐색 (Breadth-First Search)

# BFS 알고리즘 구현¶
# 자료구조 큐를 활용함
# need_visit 큐와 visited 큐, 두 개의 큐를 생성
# BFS 자료구조는 두 개의 큐를 활용하는데 반해, DFS 는 스택과 큐를 활용한다는 차이가 있음을 인지해야 함

def bfs(graph, start_node):
    visited2 = list()
    need_visit2 = list()

    need_visit2.append(start_node)

    while need_visit2:
        node = need_visit2.pop(0)
        if node not in visited2:
            visited2.append(node)
            need_visit2.extend(graph[node])

    return visited2


print('bfs', bfs(graph, 'A'))


