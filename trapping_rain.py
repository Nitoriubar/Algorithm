def trapping_rain(buildings):
    max = 0
    tmp = 0
    sum = 0
    for i in buildings:
        if i < max:
            tmp += max - i
        else:
            max = i
            sum += tmp
    return sum
  
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
