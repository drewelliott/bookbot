def count_words(book_string):
    return len(book_string.split())


def count_letters(book_string):
    letters = {}
    for word in book_string:
        word = word.lower()
        for letter in word:
            if letter in letters.keys():
                letters[letter] += 1
            else: 
                letters[letter] = 1
    return letters


def char_sort(num_letters):
    num = []
    for k,v in num_letters.items():
        num.append({'char' : k, 'num' : v})
    num.sort(reverse=True, key=sort_on_num)
    return num


def sort_on_num(d):
    return d['num']
