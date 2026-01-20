# a1p1.py

# Starter code for assignment 1 part 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Arnav Sharma
# arnas15@uci.edu
# 96085978

from pathlib import Path

def output_r(user_path):
    files = []
    directory = []
    for current_path in user_path.iterdir():
        if current_path.is_file():
            files.append(current_path)
        elif current_path.is_dir():
            directory.append(current_path)
    for f in files:
        print(f)
    for d in directory:
        print(d)
        output_r(d)
            
def output_rf(user_path):
    for current_path in user_path.iterdir():
        if current_path.is_file():
            print(current_path)
        elif current_path.is_dir():
            output_rf(current_path)

def output_rs(user_path, user_file):
    for current_path in user_path.iterdir():
        if current_path.is_file() and current_path.name == user_file:
            print(current_path)
        elif current_path.is_dir():
            output_rs(current_path, user_file)

def output_re(user_path, user_format):
    for current_path in user_path.iterdir():
        if current_path.is_file() and current_path.suffix == "." + user_format:
            print(current_path)
        elif current_path.is_dir():
            output_re(current_path, user_format)

def run():
    while True:
        user_input = input().split()
        if len(user_input) == 0:
            continue
        if (len(user_input) == 1) and (user_input[0] == "Q"):
            break
        elif user_input[0] == "L":
            if len(user_input) == 1:
                continue
            elif len(user_input) == 2:
                user_path = Path(user_input[1])
                files = []
                directory = []
                for current_path in user_path.iterdir():
                    if current_path.is_file():
                        files.append(current_path)
                    else:
                        directory.append(current_path)
                for i in files:
                    print(i)
                for j in directory:
                    print(j)
            elif len(user_input) == 3:
                user_path = Path(user_input[1])
                user_option = user_input[2]
                if user_option == "-r":
                    output_r(user_path)
                elif user_option == "-f":
                    for current_path in user_path.iterdir():
                        if current_path.is_file():
                            print(current_path)
                        else:
                            continue
            elif len(user_input) == 4:
                user_path = Path(user_input[1])
                user_option = user_input[2]
                req_file_format = user_input[3]
                if user_option == "-s":
                    for current_path in user_path.iterdir():
                        if current_path.is_file() and current_path.name == req_file_format:
                            print(current_path)
                        else:
                            continue
                elif user_option == "-e":
                    for current_path in user_path.iterdir():
                        if current_path.is_file() and current_path.suffix == "." + req_file_format:
                            print(current_path)
                        else:
                            continue
                elif user_option == "-r" and req_file_format == "-f":
                    output_rf(user_path)
            elif len(user_input) == 5:
                user_path = Path(user_input[1])
                user_option = user_input[2]
                user_option_2 = user_input[3]
                req_file_format = user_input[4]
                if user_option == "-r" and user_option_2 == "-s":
                    output_rs(user_path, req_file_format)
                elif user_option == "-r" and user_option_2 == "-e":
                    output_re(user_path, req_file_format)

if __name__ == "__main__":
    run()
