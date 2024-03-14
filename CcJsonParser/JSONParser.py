import argparse

class JsonParser():

    def parse(file_name):
        file = open(file_name, "r")
        if not JsonParser.validJson(file):
            print("Invalid JSON")
            return 1

    def validJson(file):
        lines = file.readlines()
        if len(lines) == 0:
            print("Invalid JSON")
            return False
        if JsonParser.start(lines[0]):
            if JsonParser.end(lines[0]):
                return True
            else:
                if JsonParser.end(lines[len(lines)-1]):
                    return True
                return False
        else:
            return False
            
    def start(line):
        if "{" in line:
            print("Begins With {")
            return True

    def end(line):
        if "}" in line:
            print("Ends With }")
            return True




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse JSON files")
    # parser.add_argument("-c", action="store_true", help="Get byte count of file")
    parser.add_argument("file_name", type=str, nargs="?")
    args = parser.parse_args()
    if args.file_name is None or args.file_name == "":
        print("No file specified")
        exit(1)
    file_name = args.file_name
    JsonParser.parse(file_name)