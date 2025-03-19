def str_to_reverse_capital():
    str_inp = input("Input: ")
    return str_inp.swapcase()

if __name__ == "__main__":
    str_out = str_to_reverse_capital()
    print("Output:", str_out)
