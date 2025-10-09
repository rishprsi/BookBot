from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    words = get_book_text("books/frankenstein.txt")
    num_words = count_words(words)
    print(f"Found {num_words} total words")

main()
