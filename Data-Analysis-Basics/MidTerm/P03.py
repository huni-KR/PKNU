min = 0
for i in range(1, 5):
    new_value = int(input('number ' + str(i) + ' : '))
    if i == 1:
        min = new_value
    else:
        if min > new_value:
            min = new_value

print('입력한 정수 중 가장 작은 수는 ' + str(min) + '입니다.')
