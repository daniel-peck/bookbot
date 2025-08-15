def count_words(text_from_book): 
    return(len(text_from_book.split()))

def count_characters(text_from_book):
    
    char_dict = {}
    for char in text_from_book.lower(): 
        if char not in char_dict:
            char_dict[char] = 1
        else: 
            char_dict[char] += 1

    return char_dict




