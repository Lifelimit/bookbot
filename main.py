def main():
    file_path = "books/frankenstein.txt" # github.com/Lifelimit/bookbot/books/frankenstein.txt
    text = get_book_text(file_path)
    print(text)

    word_count = count_words(text)
    print(f"\nThe book contains {word_count} words.")

    char_count = count_characters(text)
    print("\nCharacter counts in alphabetical order:")
    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")


def get_book_text(path):
    with open(path) as f:
       file_contents = f.read()
       return file_contents
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    lowered_characters = text.lower()
    char_counts = {} # Initialize an empty dictionary to store character counts
    for character in lowered_characters:
        if character in char_counts:
            char_counts[character] += 1 # If the character is already in the dictionary, increment its count 
        else:
            char_counts[character] = 1 # If it's a new character, add it to the dictionary with a count of 1
    return char_counts


main()