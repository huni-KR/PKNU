print("IT융합응용공학과 201612009 김태훈\n")

a = int(input("첫 번째 숫자를 입력하시오 : "))
b = int(input("두 번째 숫자를 입력하시오 : "))

print("\n1) 덧셈, 2) 뺄셈, 3)곱셈, 4) 나눗셈")
operator = int(input("어떤 연산을 원하는지 번호로 입력하세요 : "))

print("\n결과는 다음과 같습니다 : ", end='')
if operator == 1:
    print(str(a) + " + " + str(b) + " = " + str(a+b))
elif operator == 2:
    print(str(a) + " - " + str(b) + " = " + str(a-b))
elif operator == 3:
    print(str(a) + " * " + str(b) + " = " + str(a*b))
elif operator == 4:
    print(str(a) + " / " + str(b) + " = " + str(a/b))
