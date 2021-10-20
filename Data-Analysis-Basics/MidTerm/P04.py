start_num = int(input('1~5 사이의 정수를 입력하시오 : '))
end_num = int(input('1~5 사이의 정수를 입력하시오 : '))

list_a = []
list_b = []

for i in range(1, start_num+1):
    list_a.append(i)

for i in range(1, end_num+1):
    list_b.append(i)

for i in list_a:
    for j in list_b:
        print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
