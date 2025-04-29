def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(book):
    #will open a book and read out all the contents to be returned
    with open(book) as f:
        file_contents = f.read()
    return file_contents

main()
