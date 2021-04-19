n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

all = []
for i in range(n):
  all.append(list(map(int, input().split())))
  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  #캐릭터가 바라보는 방향 direction변수
  global direction
  directon -= 1
  if direction == -1:
    direction = 3
     
cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and all[nx][ny]==0:
        d[nx][ny]=1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
      
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if all[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)
        
