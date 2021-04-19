#공간 크기를 나타내는 N
n = int(input()) 

#여행자의 현재 위치
x, y = 1, 1

#여행자가 이동할 계획서 내용
plans = input().split()

#왼쪽, 오른쪽, 위, 아래
move_type = [L, R, U, D]

#사용자의 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#이동 계획 확인
for plan in plans:
  for i in range(len(move_type)):
    #여행자가 이동할 계획서의 내용과 이동방향이 같을때 이동
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    #여행자의 위치가 공간을 벗어났을때
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    #여행자가 이동한 위치
    x, y = nx, ny
    
print(x, y)
