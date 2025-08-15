from stats import count_words, count_characters, sort_char_count, sort_on

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main():
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print(f"------------ Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"------------ Character Count -----")
    for character in sorted_char_count: 
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["count"]}")
    print(f"============ END ============")


book_filepath = "books/frankenstein.txt"
word_count = count_words(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))
list_of_char_count = count_characters(get_book_text("/home/dan/workspace/github.com/daniel-peck/bookbot/books/frankenstein.txt"))
sorted_char_count = sort_char_count(list_of_char_count)

main()
