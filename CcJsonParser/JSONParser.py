import argparse

class JsonParser():

    lineNum = -1
    line = ""
    index = 0
    lines = []
    char = ""

    def parse(file_name):
        file = open(file_name, "r")
        JsonParser.lines = file.readlines()
        if len(JsonParser.lines) == 0:
            print("Error: Empty File")
            exit(1)
        while JsonParser.lineNum < len(JsonParser.lines):
            JsonParser.getNextLine()
            JsonParser.char = JsonParser.line[JsonParser.index]
            while JsonParser.index < len(JsonParser.line):
                JsonParser.startSymbol()
    
    def getNextLine():
        if JsonParser.lineNum+1 < len(JsonParser.lines):
            JsonParser.lineNum += 1
            JsonParser.index = 0
            JsonParser.line = JsonParser.lines[JsonParser.lineNum]
        else:
            exit(0)
    
    def getNextSymbol():
        if JsonParser.index+1 < len(JsonParser.line):
            JsonParser.index += 1
            JsonParser.char = JsonParser.line[JsonParser.index]
            return JsonParser.char
        JsonParser.getNextLine()
        JsonParser.getNextSymbol()

    def peekNextSymbol():
        if JsonParser.index+1 < len(JsonParser.line):
            char = JsonParser.line[JsonParser.index+1]
            return char
        JsonParser.getNextLine()
        JsonParser.peekNextSymbol()

    def startSymbol():
        match JsonParser.char:
            case "{":
                JsonParser.getNextSymbol()
                if JsonParser.char == "}":
                    JsonParser.startSymbol(JsonParser.char)
                    return
                elif JsonParser.char == "\n":
                    JsonParser.getNextLine()
                    JsonParser.getNextSymbol()
                    return
                elif JsonParser.char != "\"" or JsonParser.char != "}" or JsonParser.char != "\n":
                    JsonParser.exitWithError()
            case "\"":
                key = ""
                while JsonParser.peekNextSymbol() != "\"":
                    key = key + JsonParser.getNextSymbol()
                JsonParser.getNextSymbol()
                if JsonParser.getNextSymbol() != ":":
                    if JsonParser.peekNextSymbol() != " ":
                        JsonParser.exitWithError()
                    else:
                        if JsonParser.getNextSymbol() != ":":
                            JsonParser.exitWithError()
                if JsonParser.peekNextSymbol() != "\"":
                    if JsonParser.getNextSymbol() != " ":
                        JsonParser.exitWithError()
                    else:
                        if JsonParser.getNextSymbol() != "\"":
                            JsonParser.exitWithError()
                value = ""
                while JsonParser.peekNextSymbol() != "\"":
                    value = value + JsonParser.getNextSymbol()
                JsonParser.getNextSymbol()
                if JsonParser.getNextSymbol() != ",":
                    JsonParser.exitWithError()
                return
            case " ":
                JsonParser.getNextSymbol()
            case "\n":
                JsonParser.getNextSymbol()
        JsonParser.exitWithError()
        #JsonParser.getNextSymbol()
            
    def exitWithError():
        print(f"Error: Invalid JSON at Line:%d, Col:%d" %(JsonParser.lineNum+1, JsonParser.index))
        return exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse JSON files")
    parser.add_argument("file_name", type=str, nargs="?")
    args = parser.parse_args()
    if args.file_name is None or args.file_name == "":
        print("Error: No file specified")
        exit(1)
    file_name = args.file_name
    JsonParser.parse(file_name)