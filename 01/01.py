with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

    sum = 0
    for line in lines:
        calibration = []
        for element in line:
            if element.isdigit():
                calibration.append(element)
        calibration_value = calibration[0] + calibration[-1]
        sum += int(calibration_value)

print(sum)
