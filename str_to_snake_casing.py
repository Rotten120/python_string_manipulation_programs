def str_to_snake_case():
    str_inp = input("Input: ")
    str_arr = str_inp.split()
    str_out = str_arr[0]

    for word in str_arr:
        if word == str_out: continue
        str_out += "_" + word
    
    return str_out

if __name__ == "__main__":
    str_out = str_to_snake_case()
    print("Output:", str_out)
