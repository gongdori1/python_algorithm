n, m = map(int, input().split()) # 5 3
data = list(map(int, input().split())) # 1 3 2 3 2

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n # 현재 무게의 볼링공 개수 * 나머지 한 명이 선택할 수 있는 볼링공 개수

print(result)
