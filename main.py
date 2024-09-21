import sys

def generate_report(file_path, word_count, char_count):
    report = f"""
--- Begin report of {file_path} ---
{word_count} words found in the document\n
"""
    for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        report += f"The '{char}' character was found {count} times \n"
    
    report  += "--- End report ---\n"
    return report
   
def main():
    file_path = "books/frankenstein.txt"   # "books/frankenstein.txt" # github.com/Lifelimit/bookbot/books/frankenstein.txt
    text = get_book_text(file_path)
    char_count = count_characters(text)
    word_count = count_words(text)
    report = generate_report(file_path, word_count, char_count)
    print(text)
    print(report)

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
        if character.isalpha():
            if character in char_counts:
                char_counts[character] += 1 # If the character is already in the dictionary, increment its count 
            else:
                char_counts[character] = 1 # If it's a new character, add it to the dictionary with a count of 1
    return char_counts

main()