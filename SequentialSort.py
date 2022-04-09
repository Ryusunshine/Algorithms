# 순차 탐색 (Sequential Search)

# 순차 탐색은 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미
# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

def sequential_search(data, search_data):
    for index in range(len(data)):
        if data[index] == search_data:
            return data[index]
        else:
            return -1




