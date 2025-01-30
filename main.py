import sys


def parse_arguments():
    args = sys.argv[:]
    allowed_args = ['-sortingType', '-dataType', 'natural', 'byCount', 'long', 'line', 'word', '-inputFile',
                    '-outputFile', 'main.py']
    sorting_types = ['natural', 'byCount']
    data_types = ['long', 'line', 'word']
    sorting_type = ''
    data_type = ''
    input_type = 'input'
    input_file_name = ''
    output_file_name = ''
    if '-sortingType' not in args:
        sorting_type = 'natural'
    if '-sortingType' in args:
        try:
            sorting_type = args[args.index('-sortingType') + 1]
            if sorting_type not in sorting_types:
                sorting_type = 'No sorting type defined!'
        except IndexError:
            sorting_type = 'No sorting type defined!'
    if '-dataType' in args:
        try:
            data_type = args[args.index('-dataType') + 1]
            if data_type not in data_types:
                data_type = 'No data type defined!'
        except IndexError:
            data_type = 'No data type defined!'
    for i in args:
        if i not in allowed_args and not i.endswith('.txt') and not i.endswith('.dat'):
            print(i, 'is not a valid parameter. It will be skipped.')
    if '-inputFile' in args:
        input_file_name = args[args.index('-inputFile') + 1]
        input_type = 'file'
    if '-outputFile' in args:
        output_file_name = args[args.index('-outputFile') + 1]
    return input_type, sorting_type, data_type, input_file_name, output_file_name


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
    output = []
    total = len(lines_input)
    lines_dictionary = {}
    for i in lines_input:
        if i not in lines_dictionary:
            lines_dictionary.update({i: 1})
        elif i in lines_dictionary:
            lines_dictionary[i] += 1
    output.append("Total lines: {}.".format(total))
    for key, value in sorted(lines_dictionary.items()):
        percent = (value / total) * 100
        output.append("{}: {} time(s), {}%".format(key, value, int(percent)))
    return output


def process_lines_naturally(lines_input):
    output = []
    sorted_lines = sorted(lines_input)
    output.append("Total lines: {}.".format(len(sorted_lines)))
    output.append("Sorted data:")
    for i in sorted_lines:
        output.append(i)
    return output


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
    output = []
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
        output.append("{}: {} time(s), {}%".format(key, value, int(percent)))
    return output


def create_output_statement(nested_list_of_data, type_of_data, way_to_sort):
    output_statement = []
    if type_of_data == 'line':
        if way_to_sort == 'natural':
            output_statement = process_lines_naturally(nested_list_of_data)
        if way_to_sort == 'byCount':
            output_statement = (process_lines_by_count(nested_list_of_data))
    if type_of_data == 'long':
        processed_data = process_integers(nested_list_of_data)
        output_statement.append("Total numbers: {}.".format(len(processed_data)))
        if way_to_sort == 'natural':
            output_statement.append("Sorted data: {}".format(sort(processed_data)))
        if way_to_sort == 'byCount':
            sorted_data = sort(processed_data)
            output_result = sort_by_count(sorted_data, len(processed_data))
            output_statement.extend(output_result)
    if type_of_data == 'word':
        processed_data = process_words(nested_list_of_data)
        output_statement.append("Total numbers: {}.".format(len(processed_data)))
        if way_to_sort == 'natural':
            output_statement.append("Sorted data: {}".format(sort(processed_data)))
        if way_to_sort == 'byCount':
            sorted_data = sort(processed_data)
            output_result = sort_by_count(sorted_data, len(processed_data))
            output_statement.extend(output_result)
    return output_statement


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    return data.splitlines()


argument_data_type = parse_arguments()
source_of_input = argument_data_type[0]
way_to_sort = argument_data_type[1]
type_of_data = argument_data_type[2]
file_to_read_from = argument_data_type[3]
file_to_write_to = argument_data_type[4]
nested_list_of_data = []

if source_of_input == 'file':
    nested_list_of_data = read_from_file(file_to_read_from)
if source_of_input == 'input':
    nested_list_of_data = take_input()

if way_to_sort == 'No sorting type defined!' and type_of_data == 'No data type defined!':
    print('No sorting type defined!')
elif way_to_sort == 'No sorting type defined!' and type_of_data != 'No data type defined!':
    print('No sorting type defined!')
elif type_of_data == 'No data type defined!' and way_to_sort != 'No sorting type defined!':
    print('No data type defined!')
else:
    print_statement = create_output_statement(nested_list_of_data, type_of_data, way_to_sort)
    if file_to_write_to != '':
        with open(file_to_write_to, 'w') as f:
            for i in print_statement:
                f.write(i + '\n')
            f.close()
    else:
        for i in print_statement:
            print(i)
