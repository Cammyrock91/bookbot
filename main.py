from stats import word_count, symbol_frequency, sort_symbols
import sys


def get_book_text(path):
	with open(path) as f:
		contents = f.read()
		return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_content = get_book_text(filepath)

    count = word_count(book_content)
    print(f"{count} words found in the document")
	
    symbol_count = symbol_frequency(book_content)
    print(symbol_count)
	
    sorted_list = sort_symbols(symbol_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for all_words in sorted_list:
        if all_words["char"].isalpha():
            print(f"{all_words["char"]}: {all_words["num"]}")
    print("============= END ===============")

main()
