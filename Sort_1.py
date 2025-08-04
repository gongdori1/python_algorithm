N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

#파이썬의 기본 정렬 라이브러리 sorted() 사용
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
