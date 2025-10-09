import sys

from stats import count_words,count_characters,sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    print(sys.argv)
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = get_book_text(sys.argv[1])
    num_words = count_words(words)
    char_dict = count_characters(words)
    char_list = sorted_dictionary(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()
