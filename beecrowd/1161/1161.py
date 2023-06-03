# https://www.beecrowd.com.br/judge/pt/problems/view/1161

input = input().split(" ")

if not int(input[0]) == 0:
    for i in range(1, int(input[0])):
        input[0] = int(input[0]) * i
else:
    input[0] = 1

if not int(input[1]) == 0:
    for i in range(1, int(input[1])):
        input[1] = int(input[1]) * i
else:
    input[1] = 1

print(int(input[0]) + int(input[1]))
