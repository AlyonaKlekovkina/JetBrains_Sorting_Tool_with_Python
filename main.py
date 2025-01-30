import sys


def parse_arguments():
    args = sys.argv[1:]
    allowed_args = ['-sortingType', '-dataType', 'natural', 'byCount', 'long', 'line', 'word']
    sorting_types = ['natural', 'byCount']
    data_types = ['long', 'line', 'word']
    sorting_type = ''
    data_type = ''
    if '-sortingType' not in args:
        sorting_type = 'natural'
    if '-sortingType' in args:
        for i in sorting_types:
            if i in args:
                sorting_type = i
    if sorting_type == '':
        sorting_type = 'No sorting type defined!'
    for i in data_types:
        if i in args:
            data_type = i
    if len(data_type) == 0:
        data_type = 'No data type defined!'
    for i in args:
        if i not in allowed_args:
            print(i, 'is not a valid parameter. It will be skipped.')
    return sorting_type, data_type


def take_input():
    list_of_data = []
    while True:
        try:
            data = input()
            list_of_data.append(data)
        except EOFError:
            break
    return list_of_data


def process_integers(raw_data):
    list_of_integers = []
    for i in raw_data:
        for j in i.split():
            try:
                list_of_integers.append(int(j))
            except ValueError:
                print(j, 'is not a valid parameter. It will be skipped.')
    return list_of_integers


def process_words(raw_data):
    list_of_words = []
    for i in raw_data:
        for j in i.split():
            if type(j) == str:
                list_of_words.append(j)
            elif type(j) == int:
                print(j, 'is not a valid parameter. It will be skipped.')
    return list_of_words


def process_lines_by_count(lines_input):
    total = len(lines_input)
    lines_dictionary = {}
    for i in lines_input:
        if i not in lines_dictionary:
            lines_dictionary.update({i: 1})
        elif i in lines_dictionary:
            lines_dictionary[i] += 1
    print("Total lines: {}.".format(total))
    for key, value in sorted(lines_dictionary.items()):
        percent = (value / total) * 100
        print("{}: {} time(s), {}%".format(key, value, int(percent)))


def process_lines_naturally(lines_input):
    sorted_lines = sorted(lines_input)
    print("Total lines: {}.".format(len(sorted_lines)))
    print("Sorted data:")
    for i in sorted_lines:
        print(i)


def sort(list_to_sort):
    element = 1
    while element < len(list_to_sort):
        x = list_to_sort[element]
        j = element - 1
        while j >= 0 and list_to_sort[j] > x:
            list_to_sort[j + 1] = list_to_sort[j]
            j = j - 1
        list_to_sort[j + 1] = x
        element = element + 1
    string = ''
    for s in list_to_sort:
        string += str(s)
        string += ' '
    return string


def sort_by_count(list_to_sort, total):
    data_counted = {}
    count = 1
    for i in list_to_sort.split(' '):
        if i not in data_counted and i != '':
            data_counted.update({i: 1})
        elif i in data_counted:
            count += 1
            data_counted.update({i: count})
    for key, value in sorted(data_counted.items(), key=lambda x: x[1]):
        percent = (value / total) * 100
        print("{}: {} time(s), {}%".format(key, value, int(percent)))


argument_data_type = parse_arguments()
way_to_sort = argument_data_type[0]
type_of_data = argument_data_type[1]

if way_to_sort == 'No sorting type defined!' and type_of_data == 'No data type defined!':
    print('No sorting type defined!')
elif way_to_sort == 'No sorting type defined!' and type_of_data != 'No data type defined!':
    print('No sorting type defined!')
elif type_of_data == 'No data type defined!' and way_to_sort != 'No sorting type defined!':
    print('No data type defined!')
else:
    nested_list_of_data = take_input()
    way_to_sort = argument_data_type[0]
    type_of_data = argument_data_type[1]
    if way_to_sort == 'natural' and type_of_data == 'line':
        process_lines_naturally(nested_list_of_data)
    if way_to_sort == 'natural' and type_of_data == 'long':
        processed_data = process_integers(nested_list_of_data)
        print("Total numbers: {}.".format(len(processed_data)))
        print("Sorted data: {}".format(sort(processed_data)))
    if way_to_sort == 'natural' and type_of_data == 'word':
        processed_data = process_words(nested_list_of_data)
        print("Total numbers: {}.".format(len(processed_data)))
        print("Sorted data: {}".format(sort(processed_data)))
    if way_to_sort == 'byCount' and type_of_data == 'long':
        processed_data = process_integers(nested_list_of_data)
        print("Total numbers: {}.".format(len(processed_data)))
        sorted_data = sort(processed_data)
        sort_by_count(sorted_data, len(processed_data))
    if way_to_sort == 'byCount' and type_of_data == 'word':
        processed_data = process_words(nested_list_of_data)
        print("Total numbers: {}.".format(len(processed_data)))
        sorted_data = sort(processed_data)
        sort_by_count(sorted_data, len(processed_data))
    if way_to_sort == 'byCount' and type_of_data == 'line':
        process_lines_by_count(nested_list_of_data)
