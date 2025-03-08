def count(words):
    w = words.split()
    return len(w)

def char_frequency(text):
    frequency = {}
    for char in text.lower():  # Convert to lowercase
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_char_frequency(frequency_dict):
    sorted_list = sorted(
        [{"char": char, "count": count} for char, count in frequency_dict.items() if char.isalpha()],
        key=lambda x: x["count"],
        reverse=True
    )
    return sorted_list
