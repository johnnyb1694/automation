
def commatise(input_list):

    output_string = ''
    for i in range(len(input_list)):
        if i == len(input_list) - 1:
            output_string += 'and ' + input_list[i] + '.'
        else:
            output_string += input_list[i] + ', '

    return(output_string)


input_string = input('Give me a series of strings, separated by a space: ')
input_list = input_string.split()
print('Processing the following list: ', input_list)
print('Output is as follows: ', commatise(input_list))
