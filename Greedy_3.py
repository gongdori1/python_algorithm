n, k = map(int, input().split())
count = 0 #카운팅 변수

# n과 k가 같은 경우
if n == k:
    print(1)

# n > k인 경우 
while(n != 1):  # n이 1이 될 때까지 반복
    if n % k != 0:
        n = n - 1
        count += 1
    else: 
        n = n // k
        count += 1

print(count)
