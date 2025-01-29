
import sys


def parse_arguments():
    args = sys.argv
    sorting_types = ['natural', 'byCount']
    data_types = ['long', 'line', 'word']
    sorting_type = ''
    data_type = ''
    if '-sortingType' in args:
        for i in sorting_types:
            if i in args:
                sorting_type = i
    elif '-sortingType' not in args:
        sorting_type = 'natural'
    for i in data_types:
        if i in args:
            data_type = i
    if len(data_type) == 0:
        data_type = 'word'
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


def sort_integers(list_of_integers):
    element = 1
    while element < len(list_of_integers):
        x = list_of_integers[element]
        j = element - 1
        while j >= 0 and list_of_integers[j] > x:
            list_of_integers[j + 1] = list_of_integers[j]
            j = j - 1
        list_of_integers[j + 1] = x
        element = element + 1
    string = ''
    for s in list_of_integers:
        string += str(s)
        string += ' '
    return string


def sort_words(list_of_words):
    element = 1
    while element < len(list_of_words):
        first_index = list_of_words[element]
        second_index = element - 1
        while second_index >= 0 and str(list_of_words[second_index]) > str(first_index):
            list_of_words[second_index + 1] = list_of_words[second_index]
            second_index = second_index - 1
        list_of_words[second_index + 1] = first_index
        element = element + 1
    string = ''
    for s in list_of_words:
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
nested_list_of_data = take_input()
way_to_sort = argument_data_type[0]
type_of_data = argument_data_type[1]
processed_data = determine_input_data_type(nested_list_of_data)
if way_to_sort == 'natural' and type_of_data == 'line':
    process_lines_naturally(nested_list_of_data)
if way_to_sort == 'natural' and type_of_data != 'line':
    print("Total numbers: {}.".format(len(processed_data)))
    print("Sorted data: {}".format(sort_integers(processed_data)))
if way_to_sort == 'byCount' and type_of_data == 'long':
    print("Total numbers: {}.".format(len(processed_data)))
    sorted_data = sort_integers(processed_data)
    sort_by_count(sorted_data, len(processed_data))
if way_to_sort == 'byCount' and type_of_data == 'word':
    print("Total numbers: {}.".format(len(processed_data)))
    sorted_data = sort_words(processed_data)
    sort_by_count(sorted_data, len(processed_data))
if way_to_sort == 'byCount' and type_of_data == 'line':
    process_lines_by_count(nested_list_of_data)
