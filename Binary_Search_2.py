n, m = map(int, input().split()) # 떡의 개수 n, 요청한 떡의 길이 m
array = list(map(int, input().split()))

start = 0 
end = max(array)

#이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0 # 절단기로 자른 후 남은 떡 양의 합
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양(total) 계산
        if x > mid: 
            total += x - mid # total = total + (x - mid) 
    if total < m: # total이 m보다 작은 경우
        end = mid - 1 # 끝점을 중간점보다 하나 작은 수로 만들면 됨 (책 step 3의 case)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 일단 result에 기록. 다른 값이 정답일 수도 있음 
        start = mid + 1

print(result)
