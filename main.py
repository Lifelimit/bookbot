def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    print(text)

    word_count = count_words(text)
    print(f"\nThe book contains {word_count} words.")

def get_book_text(path):
    with open(path) as f:
       return f.read()
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

main()