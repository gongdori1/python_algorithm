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
n, m = map(int, input().split())
parent = [0] * (n + 1)

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
