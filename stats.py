
def count_words(book_content):
    words = book_content.split()
    return len(words)

# Creates a dictionary of characters
def count_characters(book_content):
    char_dict = {}
    for character in book_content:
        character = character.lower()
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict
