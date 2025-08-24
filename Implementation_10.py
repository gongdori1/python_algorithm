from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집의 좌표. 맨 위 좌측 좌표가 (1,1)임.
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집의 좌표.

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합의 수를 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house: # house의 행, 열 값이 각각 hx, hy에 차례대로 들어감.
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy)) # 지금까지 본 거리들 중 가장 작은 것으로 temp를 갱신.
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최솟값을 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
