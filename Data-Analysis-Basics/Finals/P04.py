def is_digit(word):
    for w in word:
        if w.isdigit():
            return True
    return False


def handle_list(list_str):
    for i in range(len(list_str)):
        if is_digit(list_str[i]):
            list_str[i] = ''
    return list_str


def print_result(list_str):
    for word in list_str:
        print(word + ' ', end='')


list_str = input('문장을 입력하시오 : ').split()

print_result(handle_list(list_str))
