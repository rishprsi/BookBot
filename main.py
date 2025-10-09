from stats import count_words,count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    words = get_book_text("books/frankenstein.txt")
    num_words = count_words(words)
    char_dict = count_characters(words)
    print(f"Found {num_words} total words")
    print(char_dict)
    
main()
