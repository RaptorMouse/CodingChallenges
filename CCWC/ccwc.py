import argparse
import os


def wc(file_name):
    word = 0
    file = open(file_name, "r")
    lines = file.readlines()
    for line in lines:
        words = line.split()
        word += len(words)
    file.close()
    print(word)
    return word

def lc(file_name):
    file = open(file_name, "r")
    lines = len(file.readlines())
    file.close()
    print(lines)
    return lines

def bc(file_name):
    file_size = os.path.getsize(file_name)
    print(file_size)

def cc(file_name):
    chars = 0
    file = open(file_name, "r")
    lines = file.readlines()
    for line in lines:
        chars += sum(len(word) for word in line)
    file.close()
    print(chars)
    return chars

def main():
    try:
        parser = argparse.ArgumentParser(description="Get statistic counts on file")
        parser.add_argument("-c", action="store_true", help="Get byte count of file")
        parser.add_argument("-l", action="store_true", help="Get line count of file")
        parser.add_argument("-w", action="store_true", help="Get word count of file")
        parser.add_argument("-m", action="store_true", help="Get char count of file")
        parser.add_argument("file_name", type=str, nargs="?")
        args = parser.parse_args()

        if args.file_name is None:
            path = os.path.abspath(os.path.dirname(__file__))
            os.chdir(path)
            for item in os.listdir(path):
                if item.endswith(".txt"):
                    args.file_name = item
                    path = path + "/" + args.file_name
                    break

        if args.file_name is None:
            print("No .txt files in current directory")

        with open(path, 'r') as file:
            var = 0
        file.close()
        
        if args.c:
            return bc(args.file_name)
        if args.l:
            return lc(path)
        if args.w:
            return wc(args.file_name)
        if args.m:
            return cc(args.file_name)
        return bc(args.file_name) + " " + lc(args.file_name) + " " + wc(args.file_name)

    except:
        print("An exception occurred.")

if __name__ == "__main__":
    main()