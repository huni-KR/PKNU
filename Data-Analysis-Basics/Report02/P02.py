print("IT융합응용공학과 201612009 김태훈\n")

cnt = 0
for i in range(1, 201):
    if i % 3 == 0 or i % 5 == 0:
        cnt += 1
        print(i, end=' ')

print("200이하의 양의 정수 중 3의 배수 또는 5의 배수의 개수는 " + str(cnt) + "개 입니다.")
