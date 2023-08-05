CEND = "\u001b[0m"

CBLACK = "\u001b[40m"
CRED = "\u001b[41m"
CGREEN = "\u001b[42m" 
CYELLOW = "\u001b[43m"
CBLUE = "\u001b[44m"
CMAGENTA = "\u001b[45m"
CCYAN = "\u001b[46m"
CWHITE = "\u001b[47m"
CBBLACK = "\u001b[40;1m"
CBRED = "\u001b[41;1m"
CBGREEN = "\u001b[42;1m"
CBYELLOW = "\u001b[43;1m"
CBBLUE = "\u001b[44;1m"
CBMAGENTA = "\u001b[45;1m"
CBCYAN = "\u001b[46;1m"
CBWHITE = "\u001b[47;1m"

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
            if char == "0": out = CBLACK
            elif char == "1": out = CRED
            elif char == "2": out = CGREEN
            elif char == "3": out = CYELLOW
            elif char == "4": out = CBLUE
            elif char == "5": out = CMAGENTA
            elif char == "6": out = CCYAN
            elif char == "7": out = CWHITE
            elif char == "8": out = CBBLACK
            elif char == "9": out = CBRED
            elif char == "A": out = CBGREEN
            elif char == "B": out = CBYELLOW
            elif char == "C": out = CBBLUE
            elif char == "D": out = CBMAGENTA
            elif char == "E": out = CBCYAN
            elif char == "F": out = CBWHITE
            elif char == " ": out = CEND
            else:
                print(f"Invalid char in image file: {char}")
                exit(1)
            char = out + "  " + CEND
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
            if char == "0": out = CBLACK
            elif char == "1": out = CRED
            elif char == "2": out = CGREEN
            elif char == "3": out = CYELLOW
            elif char == "4": out = CBLUE
            elif char == "5": out = CMAGENTA
            elif char == "6": out = CCYAN
            elif char == "7": out = CWHITE
            elif char == "8": out = CBBLACK
            elif char == "9": out = CBRED
            elif char == "A": out = CBGREEN
            elif char == "B": out = CBYELLOW
            elif char == "C": out = CBBLUE
            elif char == "D": out = CBMAGENTA
            elif char == "E": out = CBCYAN
            elif char == "F": out = CBWHITE
            elif char == " ": out = CEND
            else:
                print(f"Invalid char in image file: {char}")
                exit(1)
            char = out + "  " + CEND
            newLine += char
        output.append(newLine)
    for line in output:
        print(line)