list = []

while len(list) != 3:
    value = int(input('1~10 사이 정수를 입력하시오 : '))

    if value >= 1 and value <= 10:
        if list.__contains__(value):
            print('중복 입력하였습니다. 다시 입력하세요.')
        else:
            list.append(value)
    else:
        print('범위를 벗어났습니다. 다시 입력하세요.')

print('입력이 완료되었습니다.')
print('입력된 정수 3개는 다음과 같습니다 : ' + str(list))
