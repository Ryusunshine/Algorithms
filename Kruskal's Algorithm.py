# 크루스칼 알고리즘 (Kruskal's algorithm)

# 모든 정점을 독립적인 집합으로 만든다.
# 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
# 두 정점의 루트노드가 동일한지 확인하고, 동일하다면 싸이클이 생기는거니깐 안되고, 서로 다를 경우에만 두 정점을 연결한다.
# 최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임

# Union-Find 알고리즘
# 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 (합칠 때) 사용
# Disjoint Set
# 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
# 공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
# Disjoint Set = 서로소 집합 자료구조

# 1. 초기화
# n 개의 원소가 개별 집합으로 이뤄지도록 초기화

# 2. Union
# 두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬

# 3. Find
# 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소 (즉, 루트 노드)를 확인

# Union-Find 알고리즘의 고려할 점
# Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수 있음.
# 이 때는 Find/Union 시 계산량이 O(N) 이 될 수 있으므로, 해당 문제를 해결하기 위해, union-by-rank, path compression 기법을 사용함

# union-by-rank 기법
# 각 트리에 대해 높이(rank)를 기억해 두고,
# 1. Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임 (즉, 높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 함)
# 2. 높이가 h - 1 인 두 개의 트리를 합칠 때는 한 쪽의 트리 높이를 1 증가시켜주고, 다른 쪽의 트리를 해당 트리에 붙여줌

# path compression
# Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
# Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음

# 크루스칼 알고리즘 (Kruskal's algorithm) 코드

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 노드를 뜻함
    'edges': [  # 간선
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

# 두개의 트리 만들기
parent = dict()
rank = dict()


# 어떤 노드들간에 부모노드가 있는데 그게 자기 자신이라면 해당 노드가 루트노드라는것이고 자식노드들의 key값으로 부모노드를 넣어주면
# 전체적으로 트리가 하나 완성된다.
# rank는 트리의 높이를 알수있고 두개의 트리를 합칠때 트리의 높이를 고려하기때문에 해당 노드마다 rank가 몇인지 알 필요가 잇음.
# 그래서 rank변수를 만들어준다

def find(node):
    # path compression 기법
    if parent[node] != node:  # 부모노드가 자기가 아니다 라는뜻은 rank노드라는 뜻
        parent[node] = find(parent[node])  # 결과적으로 find함수는 루트 노드를 return하게 되어있음.
        # 각각의 노드를 재귀함수를 통해 parent노드를 찾으면 그 노드를 parent node라고 붙인다
    return parent[node]  # 결과적으로 부모노드는 root node가 된다


def union(node_v, node_u):  # 두 트리를 합치는 함수
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법    # 두가지 경우가 있는데
    if rank[root1] > rank[root2]:  # 한가지는 두개의 rank값이 다를때, rank[root1]이 크다면 root1를 root2에다가 연결
        parent[root2] = root1  # root2의 루트노드(부모노드)를 root1 자식노드로 대입
    else:
        parent[root1] = root2  # rank[root2]가 더 클경우
        if rank[root1] == rank[root2]:
            rank[root2] += 1  # rank의 root2값을 1 더해준다


# 초기화 함수를 만들어준다.
def make_set(node):  # 초기화는 모든 노드를 각각의 집합으로 만들어야한다. 즉 자식노드없고 부모노드가 자기자신임.
    parent[node] = node  # 부모노드는 자기자신
    rank[node] = 0  # parent node 하나밖에 없기때문에 rank노드는 없다


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']  # weight가 작은순서대로 정렬
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:  # 이미 정렬이 되었기때문에 반복문돌리면 작은순서대로 나옴
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):  # find함수를 만들어서 node_v의 루트노드와 node_u의 루트노드가 다른지 보고(같으면 안됨, 동일한 사이클이 생김)
            union(node_v, node_u)
            mst.append(edge)

    return mst


print(kruskal(mygraph))

# 시간 복잡도
# 크루스컬 알고리즘의 시간 복잡도는 O(E log E)
