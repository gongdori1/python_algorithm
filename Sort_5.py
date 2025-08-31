n = int(input())

house = list(map(int, input().split()))
house.sort()

print(house[(n-1) // 2]) # 리스트에서 중간 위치를 찾는 방법
