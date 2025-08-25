def snake_case_converter(pascal_or_camel_cased_string):
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         snake_cased_string = '_' + char.lower()
    #         snake_cased_char_list.append(snake_cased_string)
    #     else:
    #         snake_cased_char_list.append(char)
    # return ''.join(snake_cased_char_list).strip('_')

    #Shortcut or modern 
    snake_cased_char_list = ['_' + char.lower() if char.isupper() 
                             else char 
                             for char in pascal_or_camel_cased_string ]
    return ''.join(snake_cased_char_list).strip('_')



def main():
    print(snake_case_converter('IAmAPascalCasedString'))

main()