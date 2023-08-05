def renderImage(image):
    image = open(image, 'r')
    data = []
    for line in image:
        data.append(line.replace("\n", ""))
    image.close()
    output = []
    for line in data:
        newLine = ""
        for char in line:
            out = ""
            if char == "0": out = "\u001b[40m"
            elif char == "1": out = "\u001b[41m"
            elif char == "2": out = "\u001b[42m"
            elif char == "3": out = "\u001b[43m"
            elif char == "4": out = "\u001b[44m"
            elif char == "5": out = "\u001b[45m"
            elif char == "6": out = "\u001b[46m"
            elif char == "7": out = "\u001b[47m"
            elif char == "8": out = "\u001b[40;1m"
            elif char == "9": out = "\u001b[41;1m"
            elif char == "A": out = "\u001b[42;1m"
            elif char == "B": out = "\u001b[43;1m"
            elif char == "C": out = "\u001b[44;1m"
            elif char == "D": out = "\u001b[45;1m"
            elif char == "E": out = "\u001b[46;1m"
            elif char == "F": out = "\u001b[46;1m"
            elif char == " ": out = "\u001b[0m"
            else:
                print(f"Invalid char in image file: {char}")
                exit(1)
            char = out + "  " + "\u001b[0m"
            newLine += char
        output.append(newLine)
    for line in output:
        print(line)
    

def renderData(data):
    output = []
    for line in data:
        newLine = ""
        for char in line:
            out = ""
            if char == "0": out = "\u001b[40m"
            elif char == "1": out = "\u001b[41m"
            elif char == "2": out = "\u001b[42m"
            elif char == "3": out = "\u001b[43m"
            elif char == "4": out = "\u001b[44m"
            elif char == "5": out = "\u001b[45m"
            elif char == "6": out = "\u001b[46m"
            elif char == "7": out = "\u001b[47m"
            elif char == "8": out = "\u001b[40;1m"
            elif char == "9": out = "\u001b[41;1m"
            elif char == "A": out = "\u001b[42;1m"
            elif char == "B": out = "\u001b[43;1m"
            elif char == "C": out = "\u001b[44;1m"
            elif char == "D": out = "\u001b[45;1m"
            elif char == "E": out = "\u001b[46;1m"
            elif char == "F": out = "\u001b[46;1m"
            elif char == " ": out = "\u001b[0m"
            else:
                print(f"Invalid char in image file: {char}")
                exit(1)
            char = out + "  " + "\u001b[0m"
            newLine += char
        output.append(newLine)
    for line in output:
        print(line)