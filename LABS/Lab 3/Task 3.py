try:
    f_list = input("Enter the elements of the first list, separated by commas: ")
    f_list = f_list.split(',')
    sec_list = input("Enter the elements of the second list, separated by commas: ")
    sec_list = sec_list.split(',')
    if len(f_list) != len(sec_list):
        raise ValueError("The two lists must have the same number of elements.")
    my_dict = {}
    for key, value in zip(f_list, sec_list):
        my_dict[key.strip()] = value.strip()
    dict_str = str(my_dict)
    file_path = 'C:/Users/student24/Desktop/Dictionary.txt'
    with open(file_path, 'w') as file:
        file.write(dict_str)
    print(f"Dictionary has been successfully saved to '{file_path}'.")
except ValueError as ve:
    print(f"Error: {ve}")
except IOError:
    print("Error: An I/O error occurred while writing to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
