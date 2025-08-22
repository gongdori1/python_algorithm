n = input()
length = len(n)

result1 = 0
for i in range(length // 2):
    result1 += int(n[i])

result2 = 0
for j in range(length // 2, length):
    result2 += int(n[j])

if result1 == result2:
    print("LUCKY")

else:
    print("READY")
