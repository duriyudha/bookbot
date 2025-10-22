# Stats module

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters_count(char_count):
    char_count_sorted = []
    for char, num in sorted(char_count.items()):
        char_count_sorted.append({'char': char, 'num': num})
    char_count_sorted.sort(key=lambda x: x['num'], reverse=True)

    return char_count_sorted

        