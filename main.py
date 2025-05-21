from stats import get_book_stats, get_book_chars
import sys

def main(book_path):
    stats = get_book_stats(book_path)
    counts = get_book_chars(book_path)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}")
    print("---------- Word Count ----------")
    print(f"Found {stats} total words")
    print("---------- Character Count ----------")
    for letter, count in counts.items():
        print(f"{letter}: {count}")
    print("========== END ==========")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])


