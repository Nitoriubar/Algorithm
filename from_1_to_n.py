#Divide and Conquer를 이용해서 1부터 n까지 더하는 것.
#우리가 작성할 함수 consecutive_sum은 두 개의 정수 인풋 start와 end를 받고, 
#start부터 end까지의 합을 리턴합니다. end는 start보다 크다고 가정합니다.

def consecutive_sum(start, end):
    if start == end:
        return start
    else:
        return consecutive_sum(start,(start+end)//2)+consecutive_sum(((start+end)//2)+1,end)
# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
