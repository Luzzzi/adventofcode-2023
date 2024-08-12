with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

letters_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
sum = 0

for line in lines:
    calibration = []
    for i in range(len(line)):
        substring = line[i:]
        if substring[0].isdigit():
            calibration.append(substring[0])
        else:
            for element in letters_digits:
                if substring.startswith(element):
                    calibration.append(str(letters_digits.index(element) + 1))

    calibration_value = calibration[0] + calibration[-1]

    sum += int(calibration_value)

print(sum)
