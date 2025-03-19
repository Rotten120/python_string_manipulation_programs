def str_to_proper_capital():
    str_inp = input("Input: ")
    str_out = ""
    
    str_arr = str_inp.split()
    for word in str_arr:
        str_out += " " + word.capitalize()
    
    return str_out

if __name__ == "__main__":
    str_out = str_to_proper_capital()
    print("Output:", str_out)
