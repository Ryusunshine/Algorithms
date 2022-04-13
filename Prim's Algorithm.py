# 프림 알고리즘 (Prim's algorithm)

# 시작 정점을 선택한 후, 정점에 인접한 간선중 최소 간선으로 연결된 정점을 선택하고,
# 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 최소 신장 트리를 확장해가는 방식
# Kruskal's algorithm 과 Prim's algorithm 비교
# 둘다, 탐욕 알고리즘을 기초로 하고 있음 (당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)
# Kruskal's algorithm은 가장 가중치 기준으로 정렬해서 싸이클이 없는 순으로 선택
# Prim's algorithm은 연결된 노드에 붙어있는 간선 리스트들을 별도로 관리해서 해당 가중치중에 가장 작은걸 선택해서 싸이클이 있는지를 보고
# 싸이클이 없으면 해당 간선지 선택하고 해당 간선지와 연결된 노드를 집합에 넣는식으로 동작
# 프림 알고리즘은 선택된 노드를 기준으로 해서 점차 정보를 추가해가면서 한정된 정보하에서 가장 낮은 간선을 선택하는 방식
# 크루스칼은 전체 정보를 다 알고있다는 가정하에 모든 간선 리스트를 한꺼번에 정렬한후 가장 낮은 간선지 값을 가진 간선을 선택하는 방식이다

# 프림 알고리즘 파이썬 코드
# 1. 모든 간선 정보를 저장 (adjacent_edges)
# 2. 임의의 정점을 선택, '연결된 노드 집합(connected_nodes)'에 삽입
# 3. 선택된 정점에 연결된 간선들을 간선 리스트(candidate_edge_list)에 삽입
# 4. 간선 리스트(candidate_edge_list)에서 최소 가중치를 가지는 간선부터 추출해서,
# 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함(cycle 발생을 막기 위함)
# 5. 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리(mst)'에 삽입
# 6. 해당 간선에 연결된 인접 정점의 간선들 중, '연결된 노드 집합(connected_nodes)' 에 없는 노드와 연결된 간선들만 간선 리스트(candidate_edge_list) 에 삽입
# 7. '연결된 노드 집합(connected_nodes)' 에 있는 노드와 연결된 간선들을 간선 리스트에 삽입해도, 해당 간선은 스킵될 것이기 때문임
# 어차피 스킵될 간선을 간선 리스트(candidate_edge_list)에 넣지 않으므로 해서, 간선 리스트(candidate_edge_list)에서 최소 가중치를 가지는
# 간선부터 추출하기 위한 자료구조 유지를 위한 effort를 줄일 수 있음 (예, 최소힙 구조 사용)
# 8.선택된 간선은 간선 리스트에서 제거
# 9. 간선 리스트에 더 이상의 간선이 없을 때까지 3-4번을 반복

#heapq.heapify() 함수를 통해 리스트 데이터를 heap 형태로 한 번에 변환할 수 있음 (0번 인덱스를 우선순위로 인지함)
import heapq

graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

print(graph_data)

# defaultdict 함수를 사용해서, key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화하기
from collections import defaultdict

list_dict = defaultdict(list)
print (list_dict['key1'])

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'), # (가중치, '연결된 노드들 써주기')
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)  # 노드와 연결된 간선들을 관리할 리스트. 사전의 값이 리스트
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))  # 빈 데이터(리스트)에 튜플로 된 정보를 추가
        adjacent_edges[n2].append((weight, n2, n1))  # 방향그래프를 고려해서 어디에서부터 n1, 어디까지인지n2 추가

    connected_nodes = set(start_node)  # 연결된 노드을 관리할 집합 데이터 만든다
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

print(prim ('A', myedges))

# 시간 복잡도
# 최악의 경우, while 구문에서 모든 간선에 대해 반복하고, 최소 힙 구조를 사용하므로 O( 𝐸𝑙𝑜𝑔𝐸 ) 시간 복잡도를 가짐

# 개선된 프림 알고리즘

# 간선이 아닌 노드를 중심으로 우선순위 큐를 적용하는 방식
# 초기화 - 정점:key 구조를 만들어놓고, 특정 정점의 key값은 0, 이외의 정점들의 key값은 무한대로 놓음. 모든 정점:key 값은 우선순위 큐에 넣음
# 가장 key값이 적은 정점:key를 추출한 후(pop 하므로 해당 정점:key 정보는 우선순위 큐에서 삭제됨), (extract min 로직이라고 부름)
# 해당 정점의 인접한 정점들에 대해 key 값과 연결된 가중치 값을 비교하여 key값이 작으면 해당 정점:key 값을 갱신
# 정점:key 값 갱신시, 우선순위 큐는 최소 key값을 가지는 정점:key 를 루트노드로 올려놓도록 재구성함 (decrease key 로직이라고 부름)
# 개선된 프림 알고리즘 구현시 고려 사항
# 우선순위 큐(최소힙) 구조에서, 이미 들어가 있는 데이터의 값 변경시, 최소값을 가지는 데이터를 루트노드로 올려놓도록 재구성하는 기능이 필요함
# 구현 복잡도를 줄이기 위해, heapdict 라이브러리를 통해, 해당 기능을 간단히 구현

from heapdict import heapdict

def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in mygraph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node
    return mst, total_weight

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}
mst, total_weight = prim(mygraph, 'A')
print ('MST:', mst)
print ('Total Weight:', total_weight)

# 개선된 프림 알고리즘의 시간 복잡도:  𝑂(𝐸𝑙𝑜𝑔𝑉)
