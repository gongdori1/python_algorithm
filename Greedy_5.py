#s = list(map(int, input().split()))
#result = 0

#for i in range(0, len(s)):
#    if s[i]  == 0 or 1:
#        result += s[i]
#        continue
#    else:
#        if s[i-1] == 0 or 1:
#            result += s[i]
#            continue
#        else:
#            result *= s[i]

#print(result)

# << 수정된 코드 >>
# 각 자리 숫자가 공백 없이 들어오는 경우 예: 02984
s = list(map(int, input().strip()))
# 만약 공백으로 구분된 숫자들이라면 위 줄 대신 아래를 쓰세요.
# s = list(map(int, input().split()))

result = s[0]
for num in s[1:]:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
