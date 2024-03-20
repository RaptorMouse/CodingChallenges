import argparse
import sys

class JsonParser():

    lineNum = -1
    line = ""
    index = 0
    lines = []
    sym = ""

    def parse(file_name):
        file = open(file_name, "r")
        JsonParser.lines = file.readlines()
        if len(JsonParser.lines) == 0:
            print("Error: Empty File")
            sys.exit(1)
        while JsonParser.lineNum < len(JsonParser.lines):
            JsonParser.getNextLine()
            JsonParser.sym = JsonParser.line[JsonParser.index]
            while JsonParser.index < len(JsonParser.line):
                JsonParser.openCurly()
        sys.exit(0)
    
    def getNextLine():
        if JsonParser.lineNum+1 < len(JsonParser.lines):
            JsonParser.lineNum += 1
            JsonParser.index = 0
            JsonParser.line = JsonParser.lines[JsonParser.lineNum]
            JsonParser.sym = JsonParser.line[JsonParser.index]
        else:
            sys.exit(0)
    
    def getNextSymbol():
        if JsonParser.index+1 < len(JsonParser.line):
            JsonParser.index += 1
            JsonParser.sym = JsonParser.line[JsonParser.index]
            return JsonParser.sym
        JsonParser.getNextLine()
        JsonParser.getNextSymbol()

    def peekNextSymbol():
        if JsonParser.index+1 < len(JsonParser.line):
            JsonParser.sym = JsonParser.line[JsonParser.index+1]
            return JsonParser.sym
        JsonParser.getNextLine()
        JsonParser.peekNextSymbol()

    def openCurly():
        if JsonParser.sym == "{":
            JsonParser.curlyBrace()
        JsonParser.exitWithError()

    def curlyBrace():
        while JsonParser.peekNextSymbol() != "}":
            JsonParser.getNextSymbol()
            if JsonParser.sym.isnumeric():
                JsonParser.number()
            match(JsonParser.sym):
                case "\"":
                    JsonParser.quotation()
                    pass
                case "\n":
                    JsonParser.newLine()
                    pass
                case "\"":
                    JsonParser.quotation()
                    pass
                case ":":
                    JsonParser.colon()
                    pass
                case " ":
                    pass
                case ",":
                    JsonParser.comma()
                    pass
                case "t":
                    JsonParser.trueFalse()
                    pass
                case "f":
                    JsonParser.trueFalse()
                case "n":
                    JsonParser.null()
                case "[":
                    JsonParser.bracket()
                case _:
                    JsonParser.exitWithError()
        JsonParser.getNextSymbol()
        if JsonParser.peekNextSymbol() == ",":
            JsonParser.getNextSymbol()
            JsonParser.curlyBrace()
        return
    
    def bracket():
        JsonParser.getNextSymbol()
        while JsonParser.peekNextSymbol() != "]":
            JsonParser.curlyBrace()
        return
    
    def comma():
        match(JsonParser.peekNextSymbol()):
            case " ":
                JsonParser.getNextSymbol()
                JsonParser.comma()
                pass
            case "\n":
                JsonParser.newLine()
                JsonParser.comma()
                pass
            case "\"":
                JsonParser.getNextSymbol
                pass
            case _:
                JsonParser.getNextSymbol()
                JsonParser.exitWithError()
            
    def colon():
        JsonParser.getNextSymbol()
        while JsonParser.peekNextSymbol() == " ":
            JsonParser.getNextSymbol()
        if JsonParser.peekNextSymbol() == "t" or JsonParser.peekNextSymbol() == "f" or JsonParser.peekNextSymbol() == "n":
            JsonParser.curlyBrace()
        if JsonParser.peekNextSymbol().isnumeric():
            JsonParser.curlyBrace()
        if JsonParser.peekNextSymbol() != "\"":
            JsonParser.getNextSymbol()
            JsonParser.exitWithError()
        JsonParser.getNextSymbol()
        JsonParser.quotation()
        return
    
    def newLine():
        JsonParser.getNextLine()
        return

    def null():
        value = JsonParser.sym
        while JsonParser.getNextSymbol() != "l":
            value += JsonParser.sym
        value += JsonParser.sym + JsonParser.getNextSymbol()
        if value == "null":
            return
        else:
            JsonParser.exitWithError()

    def number():
        value = JsonParser.sym
        while JsonParser.getNextSymbol().isnumeric():
            value += JsonParser.sym
        number = int(value)
        return number

    def quotation():
        value = ""
        while JsonParser.peekNextSymbol() != "\"":
            value += JsonParser.sym
            JsonParser.sym = JsonParser.getNextSymbol()
        JsonParser.getNextSymbol()
        return

    def trueFalse():
        value = JsonParser.sym
        while JsonParser.getNextSymbol() != "e":
            value += JsonParser.sym
        value += JsonParser.sym
        if value == "true" or value == "false":
            return
        else:
            JsonParser.exitWithError()
            
    def exitWithError():
        print(f"Error: Invalid JSON at Line:%d, Col:%d" %(JsonParser.lineNum+1, JsonParser.index))
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse JSON files")
    parser.add_argument("file_name", type=str, nargs="?")
    args = parser.parse_args()
    if args.file_name is None or args.file_name == "":
        print("Error: No file specified")
        sys.exit(1)
    file_name = args.file_name
    JsonParser.parse(file_name)