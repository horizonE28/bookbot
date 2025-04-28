def get_num_words(booktext):
    return len(booktext.split())

def count_characters(booktext):
    lowertext = booktext.lower()
    count = {}

    for char in lowertext:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def sort_on(dict):
    return dict["num"]

def sort_dict(unsorted_dict):
    sorted = []

    for chars in unsorted_dict:
        sorted.append({"char": chars,
                        "num" : unsorted_dict[chars]})
        
    sorted.sort(reverse=True, key=sort_on)

    return sorted

