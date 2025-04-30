from stats import sorted_list  
from stats import count_words  

def main():
    book = "books/frankenstein.txt" 
    text = get_book_text(book)
    #get the report of letters counted, returns list of dictionarys [{"char" : "n", "num": 69}, ...{}]
    report = sorted_list(text)

    #sort the report 
    report.sort(reverse=True, key=sort_on) 
    
    #get_total words for info
    total_words = count_words(text) 

    #add some decoration
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    #output the list of dictionary results, in the sroted order from above 
    for char in report:
    #print(f"{char}")
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    
    #add ending decoration
    print("============= END ===============")

def sort_on(dict):
    return dict["num"]

def get_book_text(book):
    #will open a book and read out all the contents to be returned
    with open(book) as f:
        file_contents = f.read()
    return file_contents


main()
