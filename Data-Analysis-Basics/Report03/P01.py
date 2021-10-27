def print_line(fruits_dict, fruit):
    print(fruit+' : ' + str(fruits_dict[fruit]) + '원')


fruits_dict = {'사과': 0, '배': 0, '수박': 0, '귤': 0, '포도': 0}

fruits_list = list(input('사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력 : ').split())

fruits_dict['사과'] = fruits_list[0]
fruits_dict['배'] = fruits_list[1]
fruits_dict['수박'] = fruits_list[2]
fruits_dict['귤'] = fruits_list[3]
fruits_dict['포도'] = fruits_list[4]


print('\n---------- 오늘의 과일 가격 ----------')
print_line(fruits_dict, '사과')
print_line(fruits_dict, '배')
print_line(fruits_dict, '수박')
print_line(fruits_dict, '귤')
print_line(fruits_dict, '포도')
