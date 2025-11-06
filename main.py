from stats import count_words, count_letters, char_sort
import sys

def read_book(book):
    with open(book) as fh:
        return fh.read()


def gen_report(book, num_words, sorted_num):


    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_num:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}") 

    print("============= END ===============\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    my_book = sys.argv[1]
    book_string = read_book(my_book)
    num_words = count_words(book_string)
    num_letters = count_letters(book_string)
    sorted_num = char_sort(num_letters)
    gen_report(my_book, num_words, sorted_num)


if __name__=="__main__":
    main()
