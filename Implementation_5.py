# 알파벳 대문자와 숫자(0~9)로 구성된 문자열이 입력으로 주어집니다.
# 모든 알파벳은 오름차순으로 정렬해서 이어서 출력하고,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다. 
# ex) K1KA5CB7 -> ABCKK13
# 08:44~

s = input().strip() # 공백을 제거하고 입력받음.

letters = []
num_sum = 0 # 맨 마지막에 출력되는 부분인 숫자들의 합

for ch in s:
    if ch.isdigit(): # 숫자를 맞닥뜨렸을 때
        num_sum += int(ch)
    else:            # 알파벳을 맞닥뜨렸을 때
        letters.append(ch)

letters.sort()
print(''.join(letters) + str(num_sum))
