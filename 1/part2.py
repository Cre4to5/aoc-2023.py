with open("./1/input.txt") as file:
    lines = file.readlines()

    string_digits = {
        "one": "1",
        "1": "1",
        "two": "2",
        "2": "2",
        "three": "3",
        "3": "3",
        "four": "4",
        "4": "4",
        "five": "5",
        "5": "5",
        "six": "6",
        "6": "6",
        "seven": "7",
        "7": "7", 
        "eight": "8",
        "8": "8", 
        "nine": "9",
        "9": "9"
    }

    numbers = []

    for line in lines:
        line = line.strip()

        # print(line)

        digits_indexes = {}
        for string_digit in string_digits.keys():
            temp = str.find(line, string_digit)
            if temp != -1:
                digits_indexes[temp] = string_digit
        
        # print(digits_indexes)

        digits_indexes_keys = sorted(digits_indexes.keys())
        
        # print(digits_indexes_keys[0])

        numbers.append(int(string_digits[digits_indexes[digits_indexes_keys[0]]] + string_digits[digits_indexes[digits_indexes_keys[-1]]]))
        # print(numbers[-1])

    print(sum(numbers))