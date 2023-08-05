# -*- coding: utf-8 -*-

import string
import math
from collections import namedtuple
from sheetfu.exceptions import SizeNotMatchingRangeException


RangeCoordinates = namedtuple('RangeCoordinates', 'row column number_of_rows number_of_columns sheet_name')


def check_size(f):
    """Decorator to check length of the 2D matrix to be set. Raise an error is lengths are not matching with Range
    object coordinates.
    """
    def wrapper(range_object, data):
        if len(data) != range_object.coordinates.number_of_rows:
            raise SizeNotMatchingRangeException("Wrong number of rows. {} instead of {}".format(
                len(data), range_object.coordinates.number_of_rows
            ))
        for i, row in enumerate(data):
            if len(row) != range_object.coordinates.number_of_columns:
                context = {"i": i, "columns": len(row), "expected": range_object.coordinates.number_of_columns}
                raise SizeNotMatchingRangeException("Wrong number of column in row {i}. {columns} instead of {expected}"
                                                    .format(**context))
        else:
            return f(range_object, data)
    return wrapper


def convert_coordinates_to_a1(row, column, number_of_row=1, number_of_column=1, sheet_name=None):
    notation = convert_column_to_letter(column) + str(row)
    if number_of_row > 1 or number_of_column > 1:
        last_column_index = column + number_of_column - 1
        last_row_index = row + number_of_row - 1    # row 3 with 3 rows is from row 3 to row 5 and not 6
        last_cell_range = convert_column_to_letter(last_column_index) + str(last_row_index)
        notation += ":" + last_cell_range
    if sheet_name:
        return sheet_name + "!" + notation
    return notation


def convert_a1_to_coordinates(a1_string):
    sheet_name = None
    # in case the sheet name is in A1
    if '!' in a1_string:
        sheet_name, a1_string = a1_string.split('!')
    first_cell = a1_string.split(':')[0]
    column, row = split_letters_numbers(first_cell)
    number_of_rows = 1
    number_of_columns = 1
    # in case the range is more than one cell (matrix)
    if ":" in a1_string:
        last_cell = a1_string.split(':')[1]
        last_column, last_row = split_letters_numbers(last_cell)
        number_of_rows = last_row - row + 1
        number_of_columns = last_column - column + 1
    return RangeCoordinates(
        row=row,
        column=column,
        number_of_rows=number_of_rows,
        number_of_columns=number_of_columns,
        sheet_name=sheet_name
    )


def split_letters_numbers(a1_fragment):
    for i, character in enumerate(a1_fragment):
        if character in '123456789':
            letter = a1_fragment[0:i]
            number = int(a1_fragment[i:])
            return convert_letter_to_column(letter), number
    else:
        return a1_fragment      # only letters = a whole column range


def convert_column_to_letter(column_index):
    column_index = column_index - 1
    letters = string.ascii_uppercase
    if column_index < len(letters):
        return letters[column_index]
    first_letter_index = column_index / len(letters) - 1
    second_letter_index = column_index % len(letters)
    return letters[int(first_letter_index)] + letters[int(second_letter_index)]


def convert_letter_to_column(letters_string):
    index_to_row_offset = 1
    if len(letters_string) == 1:
        return string.ascii_uppercase.index(letters_string.capitalize()) + index_to_row_offset
    column_number = 0
    for i, letter in enumerate(letters_string):
        letter_index = string.ascii_uppercase.index(letter.capitalize()) + index_to_row_offset
        power = len(letters_string) - (i + 1)
        number_of_columns = letter_index * math.pow(len(string.ascii_uppercase), power)
        column_number += number_of_columns
    return column_number

