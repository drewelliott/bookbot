
def read_book(book):
    with open(book) as fh:
        return fh.read()

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


def gen_report(book, num_words, sorted_num):

    print(f"\n--- Begin report of {book} ---")
    print(f"{num_words} words found in the document\n\n")

    for item in sorted_num:
        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times") 

    print("--- End report ---\n")


def main():
    my_book = 'books/frankenstein.txt'
    book_string = read_book(my_book)
    num_words = count_words(book_string)
    num_letters = count_letters(book_string)
    sorted_num = char_sort(num_letters)
    gen_report(my_book, num_words, sorted_num)


if __name__=="__main__":
    main()
