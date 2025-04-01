from stats import word_count
from stats import char_count
from stats import char_count_builder
import sys

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars = char_count(book_text)
    sorted_chars = char_count_builder(num_chars.items())
    print("--------- Character Count -------")
    for c in sorted_chars:
        if not c["char"].isalpha():
            continue
        print(f"{c['char']}: {c['count']}")
    print("============= END ===============")

main()
