from stats import get_num_words
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    s = get_book_text(path)
    num_words = get_num_words(s)
    l = sort_dict(count_characters(s))
    
    #   Print Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in l:
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")
    
main()