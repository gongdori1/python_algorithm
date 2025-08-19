s = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(s) -1):
    if s[i] != s[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
#참고로, 위의 반복문에서 s[i] == s[i+1]인 경우엔 아무 일도 일어나지 않음! 
#즉, count0와 count1의 값은 변하지 않음. 숫자가 바뀔 때에만 카운트가 늘어나지. 

print(min(count0, count1))
