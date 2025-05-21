
# This is used to get the word count of a book
def get_book_stats(book):
    with open(book) as f:
        book_content = f.read()
        book_content = book_content.lower()
        words = len(book_content.split())
        return words

# This is used to get the character count of a book
# It counts the number of times each character appears in the book
# It ignores spaces and punctuation
def get_book_chars(book):
    with open(book) as f:
        book_content = f.read()
        book_content = book_content.lower()
        char_counts = {}
        for char in book_content:
            if char.isalpha():
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
        sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        return sorted_char_counts