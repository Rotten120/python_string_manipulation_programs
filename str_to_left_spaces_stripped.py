def str_to_left_stripped():
    str_inp = input("Input: ")
    return str_inp.lstrip()

if __name__ == "__main__":
    str_out = str_to_left_stripped()
    print("Output:", str_out)
