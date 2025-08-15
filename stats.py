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

def sort_on(items):
    return items["count"]

def sort_char_count(dict_of_count_characters): 
    list_of_char_count = []
    for char, num in dict_of_count_characters.items(): 
        list_of_char_count.append({"char": char, "count": num})
    
    list_of_char_count.sort(reverse=True, key=sort_on)

    return list_of_char_count




