def word_count(book_text):
        count = len(book_text.split())
        return count


def symbol_frequency(book_text):
	character_count = {}
	for char in book_text:
		char = char.lower()
		if char not in character_count:
			character_count[char] = 1
		else:
			character_count[char] += 1
	return character_count


def sort_symbols(character_count):
	sorted_symbols = []
	for key in character_count:
		sorted_symbols.append({"char": key, "num": character_count[key]})
	sorted_symbols.sort(reverse=True, key=sort_on)
	return sorted_symbols


def sort_on(dict):
    return dict["num"]


