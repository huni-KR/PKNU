input = int(input('3자리 정수를 입력하시오 : '))
print('입력한 정수를 거꾸로 출력하면 다음과 같습니다 : ' + str(input %
      10) + str((input//10) % 10) + str(input//100))
