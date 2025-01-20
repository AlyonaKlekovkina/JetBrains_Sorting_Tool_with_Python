def take_input():
    list_of_data = []
    while True:
        try:
            data = input()
            list_of_data += data.split(' ')
        except EOFError:
            break
    return list_of_data


def select_integers(raw_data):
    list_of_ints = []
    for i in raw_data:
        try:
            converted_integer = int(i)
            list_of_ints.append(converted_integer)
        except ValueError:
            pass
    return list_of_ints


def create_output(list_of_integers):
    x = len(list_of_integers)
    sorted_list = sorted(list_of_integers)
    y = sorted_list[-1]
    count = 0
    for i in list_of_integers:
        if i == y:
            count += 1
    z = count
    print("Total numbers: {}. \nThe greatest number: {} ({} time(s)).".format(x, y, z))


raw_data_input = take_input()
integers_list = select_integers(raw_data_input)
create_output(integers_list)
