n, m = map(int,input().split()) # n행 m열


result = 0 #result 값 미리 초기화. 

for i in range(n): # n행만큼 반복.
    data = list(map(int,input().split())) # 한 행씩 입력받음.
    min_value = min(data) # 그 행에서 가장 작은 수를 찾음.
    result = max(result, min_value) # 그 행에서 가장 작은 수와 result를 비교하여 더 큰 수를 result에 저장.
#결국 반복문을 다 실행하면 각 행들의 최솟값중에서 가장 큰 값이 남겠지? 그게 result에 저장된 값이야.
    
print(result)
