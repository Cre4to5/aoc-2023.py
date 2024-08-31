with open("./1/input.txt") as file:
    lines = file.readlines()

    string_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    numbers = []

    for line in lines:
        line = line.strip()
        print(line)

        for i, string_digit in enumerate(string_digits):#that wont work for overlaping shit like "twone"
            # print(i)
            # print(string_digit)
            line = str.replace(line, string_digit, f"{i + 1}",-1)

        print(line)

        digits = []
        for letter in line:
            if str.isdigit(letter):
                digits.append(letter)
        
        numbers.append(int(digits[0] + digits[-1]))
        print(numbers[-1])

    print(sum(numbers))