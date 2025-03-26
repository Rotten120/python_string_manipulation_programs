def str_to_proper_capital():
    str_inp = input("Input: ")
    str_arr = str_inp.split()
    str_out = str_arr[0].capitalize()
    
    for word in str_arr:
        capitalized = word.capitalize()
        if capitalized == str_out: continue
        str_out += " " + capitalized
    
    return str_out

if __name__ == "__main__":
    str_out = str_to_proper_capital()
    print("Output:", str_out)
