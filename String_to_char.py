#문자열을 입력받아 한 글자씩 출력하기

# Sol_1
input_string = input()
[print(i) for i in input_string]

# Sol_2
input_string = input()
print(*input_string, sep="\n")

