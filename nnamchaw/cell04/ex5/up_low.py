#!/usr/bin/env python3

def main():
    user_input = input("Enter a string: ")
    converted_string = convert_case(user_input)
    print(converted_string)

def convert_case(input_str):
    converted_str = ''
    for char in input_str:
        if char.islower():
            converted_str += char.upper()
        elif char.isupper():
            converted_str += char.lower()
        else:
            converted_str += char  # keep non-alphabetic characters unchanged
    return converted_str

if __name__ == "__main__":
    main()
