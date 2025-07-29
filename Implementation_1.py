n = int(input()) # NxN 행렬
move = list(map(str, input().split())) #입력된 문자가 리스트 형태로 move에 저장됨.

x_coordinate = 1 #시작점 x좌표
y_coordinate = 1 #시작점 y좌표

for i in range(len(move)): # move 리스트의 길이만큼 반복
    if move[i] == 'L': # move[i]가 L일 때
        y_coordinate -= 1 # y좌표 -1
        if y_coordinate < 1: # y좌표가 1보다 작아질 때
            y_coordinate += 1 # y좌표 +1(다시 원상복귀)
    
    elif move[i] == 'R':
        y_coordinate += 1
        if y_coordinate > n:
            y_coordinate -= 1 # y좌표 -1(다시 원상복귀)

    elif move[i] == 'U':
        x_coordinate -= 1
        if x_coordinate < 1:
            x_coordinate += 1

    else: # move[i]가 D일 때
        x_coordinate += 1
        if x_coordinate > n:
            x_coordinate -= 1

print(x_coordinate, y_coordinate)
