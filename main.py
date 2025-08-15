def count_words(text_from_book): 
    return(len(text_from_book.split()))

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))



print(f"{count_words(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))} words found in the document")
#main()


    