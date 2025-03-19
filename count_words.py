def get_word_count():
    str_inp = input("Input: ")
    return len(str_inp.split())

if __name__ == "__main__":
    word_count = get_word_count()
    print("Output:", word_count)
