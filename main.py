def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(booktext):
    return len(booktext.split())

def main():
    s = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(s)
    print(f"{num_words} words found in the document")

main()