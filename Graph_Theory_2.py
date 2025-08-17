#특정 원소가 속한 집합을 찾기 (찾기 연산)
def find_parent(parent, x): 
    #루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기 (합집합 연산)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함...?
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)
