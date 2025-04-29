from stats import count_chars

def main():
    char_count = count_chars(get_book_text("books/frankenstein.txt"))
    
    for char, count in char_count.items():
        print(f"'{char}': {count}")


def get_book_text(book):
    #will open a book and read out all the contents to be returned
    with open(book) as f:
        file_contents = f.read()
    return file_contents


main()
