import sys
from stats import count_words, count_characters, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]
    word_count = count_words(get_book_text(f"/home/dan/workspace/github.com/daniel-peck/bookbot/{book_filepath}"))
    list_of_char_count = count_characters(get_book_text(f"/home/dan/workspace/github.com/daniel-peck/bookbot/{book_filepath}"))
    sorted_char_count = sort_char_count(list_of_char_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print(f"------------ Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"------------ Character Count -----")
    for character in sorted_char_count: 
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["count"]}")
    print(f"============ END ============")





main()
