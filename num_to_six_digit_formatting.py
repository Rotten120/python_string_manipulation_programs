def num_to_six_dig_format():
    format_length = 6
    num_inp = -1

    while not(0 <= num_inp <= 1000):
        try: num_inp = int(input("Input a number (0-1000): "))
        except: print("Input a number")
            
    return str(num_inp).zfill(format_length)

if __name__ == "__main__":
    num_out = num_to_six_dig_format()
    print("Output:", num_out)
