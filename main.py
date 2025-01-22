import sys


def parse_arguments():
    args = sys.argv
    if len(args) != 3:
        d_type = 'word'
    else:
        d_type = args[2]
    return d_type


def take_input():
    list_of_data = []
    while True:
        try:
            data = input()
            list_of_data.append(data)
        except EOFError:
            break
    return list_of_data


def determine_input_data_type(raw_data):
    integers_list = []
    words_list = []
    for i in raw_data:
        for j in i.split():
            try:
                converted_integer = int(j)
                integers_list.append(converted_integer)
            except ValueError:
                if j != '':
                    words_list.append(j)
    if len(integers_list) != 0:
        return integers_list
    if len(words_list) != 0:
        return words_list


def calculate_count_percentage(x, y, list_of_raw_data):
    count = 0
    for i in list_of_raw_data:
        if i == y:
            count += 1
    z = count
    percentage = int((count / x) * 100)
    return z, percentage


def process_words(list_of_raw_data):
    longest = list_of_raw_data[0]
    for i in list_of_raw_data:
        if len(i) > len(longest):
            longest = i
        if len(i) == len(longest) and i > longest:
            longest = i
        if len(i) == len(longest) and i < longest:
            longest = longest
    return longest


def process_lines(lines_input):
    lines_dictionary = {}
    for i in lines_input:
        lines_dictionary.update({i: len(i)})
    return max(lines_dictionary, key=lines_dictionary.get)


argument_data_type = parse_arguments()
nested_list_of_data = take_input()
if argument_data_type == 'long':
    data = determine_input_data_type(nested_list_of_data)
    x = len(data)
    y = sorted(data)[-1]
    calculations = calculate_count_percentage(x, y, data)
    z = calculations[0]
    percentage = calculations[1]
    print("Total numbers: {}. \nThe greatest number: {} ({} time(s)), {}%.".format(x, y, z, percentage))
if argument_data_type == 'line':
    x = len(nested_list_of_data)
    y = process_lines(nested_list_of_data)
    calculations = calculate_count_percentage(x, y, nested_list_of_data)
    z = calculations[0]
    percentage = calculations[1]
    print("Total lines: {}.\nThe longest line:\n{}\n({} time(s), {}%).".format(x, y, z, percentage))
if argument_data_type == 'word':
    data = determine_input_data_type(nested_list_of_data)
    if type(data[0]) is int:
        y = sorted(data)[-1]
    else:
        y = process_words(data)
    x = len(data)
    calculations = calculate_count_percentage(x, y, data)
    z = calculations[0]
    percentage = calculations[1]
    print("Total words: {}.\nThe longest word: {} ({} time(s), {}%).".format(x, y, z, percentage))
