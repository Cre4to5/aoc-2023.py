with open("./1/input.txt") as file:
    lines = file.readlines()

    numbers = []

    for line in lines:

        digits = []

        for letter in line:
            if str.isdigit(letter):
                digits.append(letter)
        numbers.append(int(digits[0] + digits[-1]))
    print(sum(numbers))