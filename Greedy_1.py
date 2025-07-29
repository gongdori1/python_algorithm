n, m, k = list(map(int, input().split())) # n개의 숫자로 구성된 리스트가 주어지면 총 m번을 더하는데, k번이 최대다. 
data = list(map(int, input().split()))

#주어진 리스트 오름차순 정렬
data.sort()

#정렬된 리스트의 가장 오른쪽에 있는 수를 k번 더해. 
#그 다음, 오른쪽에서 두번째 있는 수가 가장 큰 수랑 똑같을 때는? 그 수를 m-k번 더하면 끝. 
#그게 아닐 떈 오른쪽에서 두번째 있는 수 한 번 더하고, 다시 또 가장 큰 수를 더하고... 하면 됨. (이때 k번을 넘지 말아야 함)

if data[n-1] == data[n-2]:
    result = m*data[n-1]
else:
    quotient = m // (k+1) #몫의 값 * (k*data[n-1] + data[n-2]) 해주면 됨
    remainder = m % (k+1) #위의 식에다가 data[n-1] * remainder 더해주면 됨
    result = quotient * (k*data[n-1] + data[n-2]) + data[n-1] * remainder

print(result)
  
