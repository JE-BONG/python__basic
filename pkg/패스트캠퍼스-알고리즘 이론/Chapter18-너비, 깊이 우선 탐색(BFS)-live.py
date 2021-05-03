# 너비, 깊이 우선 탐색(Breadth-First Search, Depth-First Search)

 # 1. BFS 와 DFS
 # 대표적인 그래프 탐색 알고리즘
 # 너비 우선 탐색(Breadth First Search) : 정점들과 같은 레벨에 있는 노드들(형제 노드)을 먼저 탐색
 # 깊이 우선 탐색(Depth First Seach) : 정점의 자식들을 먼저 탐색하는 방식

 # 2. BFS/DFS 방식 이해를 위한 예제
 # BFS 방식 : A - B - C - D - G - H - I - E - F - J
 # - 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드(형제 노드)를 먼저 순회

 # DFS 방식 : A - B - E - F - C - G - H - I - J
 # - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회

# DFS
graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

# pop(), extend()
data = [1, 2, 3]
data.pop(0)         # 0번 인덱스를 뺄 경우 queue 처럼 앞으로 인덱스 하나씩 당겨진다.
data.extend([4, 5]) # 맨 뒤 인덱스에 추가 
print(data)

# queue 를 두개 사용 하는 경우
def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count = 0
    while need_visit: # need_visit이 있을 경우에만 while문 실행
        count += 1
        node = need_visit.pop(0) # need_visit에 있는 값을 노드에 넣고
        if node not in visited:  # node의 값이 visited에 존재하지 않는 경우 실행
            visited.append(node) # 해당 node의 값이 없는 경우에는 visited 추가 / node의 값이 visited에 존재한다면 그대로 소멸
            need_visit.extend(graph[node])
    print(count)
    return visited
print(bfs(graph, 'A'))

# DFS
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        # pop()       : 맨 뒤 인덱스를 가져오면서 맨뒤 인덱스를 삭제한다.(스택을 활용 - LIFO)
        # pop(인덱스) : 해당 인덱스를 가져오면서 전체 인덱스가 앞으로 1씩 옮긴다.
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited

print(dfs(graph,'A'))

# 3. 시간 복잡도
# 노드 수 : V
# 간선 수 : E
# - 위 코드에서 while need-visit 은 V + E번 만큼 수행한다.
# O(V + E) : 간선의 수 + 노드의 수 19







