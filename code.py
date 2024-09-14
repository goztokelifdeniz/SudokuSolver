import sys


def is_the_cell_empty(cell):
    return cell == 0


def turn_the_string_input_to_an_integer_list_without_spaces(input_file): # this function makes an ordered list of numbers in the input file
    sudoku_numbers = "".join(input_file.read().split())  # order: rows from left to right, columns from up to down
    input_as_a_list_of_integers = []
    for number in sudoku_numbers:
        input_as_a_list_of_integers.append(int(number)) # elements of the returned list are integers for simplicity of code
    return input_as_a_list_of_integers


def make_the_list_of_rows(list_without_spaces): # returned list is head list of rows, index-lists including the numbers in each row
    list_of_rows = [list_without_spaces[number: number+9] for number in range(0, 81, 9)]
    return list_of_rows


def make_the_list_of_columns(list_without_spaces): # returned list is head list of columns, sublists including the numbers in each column
    list_of_columns_ungrouped = [list_without_spaces[number] for times in range(0, 9) for number in range(times, len(list_without_spaces.copy()), 9)]
    list_of_columns = [list_of_columns_ungrouped[number: number+9] for number in range(0, len(list_of_columns_ungrouped), 9)]
    return list_of_columns


def list_of_possible_numbers_after_eliminating_numbers_in_the_same_row_and_column(input_list, row_index, column_index):
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    numbers_in_the_same_row = make_the_list_of_rows(input_list)[row_index]
    possible_numbers = [number for number in possible_numbers if number not in numbers_in_the_same_row if number !=0]

    numbers_in_the_same_column = make_the_list_of_columns(input_list)[column_index]
    possible_numbers = [number for number in possible_numbers if number not in numbers_in_the_same_column if number !=0]

    return possible_numbers


def make_list_of_numbers_in_the_same_3x3_region_with_the_given_number(input_list, row_index, column_index):
    # if the cell is in the:
    if (row_index + 2) % 3 == 0: # middle row of region
        if (column_index + 2) % 3 == 0: # middle column of region
            list_of_the_region = [input_list[row*9 + column] for row in range(row_index-1, row_index+2) for column in range(column_index-1, column_index+2) if input_list[row*9 + column]]
        elif (column_index + 2) % 3 == 1: # rightmost column of region
            list_of_the_region = [input_list[row*9 + column] for row in range(row_index-1, row_index+2) for column in range(column_index-2, column_index+1) if input_list[row*9 + column]]
        else: # leftmost column of region
            list_of_the_region = [input_list[row*9 + column] for row in range(row_index-1, row_index+2) for column in range(column_index, column_index+3) if input_list[row*9 + column]]

    elif (row_index + 2) % 3 == 1: # lower row of region
        if (column_index + 2) % 3 == 0: # middle column of region
            list_of_the_region = [input_list[row*9 + column] for row in range(row_index-2, row_index+1) for column in range(column_index-1, column_index+2) if input_list[row*9 + column]]
        elif (column_index + 2) % 3 == 1: # rightmost column of region
            list_of_the_region = [input_list[row * 9 + column] for row in range(row_index-2, row_index+1) for column in range(column_index-2, column_index+1) if input_list[row*9 + column]]
        else: # leftmost column of region
            list_of_the_region = [input_list[row * 9 + column] for row in range(row_index-2, row_index+1) for column in range(column_index, column_index+3) if input_list[row*9 + column]]

    else: # upper row of region
        if (column_index + 2) % 3 == 0: # middle column of region
            list_of_the_region = [input_list[row*9 + column] for row in range(row_index, row_index+3) for column in range(column_index-1, column_index+2) if input_list[row*9 + column]]
        elif (column_index + 2) % 3 == 1: # rightmost column of region
            list_of_the_region = [input_list[row * 9 + column] for row in range(row_index, row_index+3) for column in range(column_index-2, column_index+1) if input_list[row*9 + column]]
        else: # leftmost column of region
            list_of_the_region = [input_list[row * 9 + column] for row in range(row_index, row_index+3) for column in range(column_index, column_index+3) if input_list[row*9 + column]]
    return list_of_the_region


def fill_the_cells_and_return_the_text_of_output_file(input_list):
    output_text = ""
    sudoku_step_counter = 0
    while 0 in input_list: # while there are empty cells in sudoku
        for index in range(len(input_list)):
            column_index = index % 9
            row_index = index // 9
            if input_list[index] == 0:
                possible_numbers = [number for
                                    number in list_of_possible_numbers_after_eliminating_numbers_in_the_same_row_and_column(input_list, row_index, column_index)
                                    if number != 0
                                    if number not in make_list_of_numbers_in_the_same_3x3_region_with_the_given_number(input_list, row_index, column_index)]
            else:
                continue
            if is_the_cell_empty(input_list[index]) and len(possible_numbers) == 1:
            #if the cell is empty and there is only one number that can be placed in the cell
                sudoku_step_counter += 1
                input_list[index] = possible_numbers[0]
                output_text += "------------------\n"
                output_text += "Step {} - {} @ R{}C{}\n".format(str(sudoku_step_counter), str(input_list[index]), str(row_index + 1), str(column_index + 1))
                output_text += "------------------\n"
                for index_for_inner_for_loop in range(len(input_list)): #adding the latest version of sudoku to the output text after filling head cell
                    if (index_for_inner_for_loop + 1) % 9 == 0:
                        output_text += str(input_list[index_for_inner_for_loop]) + "\n"
                    else:
                        output_text += str(input_list[index_for_inner_for_loop]) + " "
                break # so that the previously checked empty cells are checked again after filling head cell
    output_text += "------------------"
    return output_text


def main():
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    output_file.write(fill_the_cells_and_return_the_text_of_output_file(turn_the_string_input_to_an_integer_list_without_spaces(input_file)))
    input_file.close()
    output_file.flush()
    output_file.close()


if __name__ == "__main__":
    main()
