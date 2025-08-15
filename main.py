from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))



print(f"{count_words(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))} words found in the document")
num_each_char = count_characters(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))
print(num_each_char)
#main()


    