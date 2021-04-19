data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1 

knight_move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0
for move in knight_move:
  nr = row + step[0]
  nc = column + step[1]
  if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
    result += 1

print(result)
