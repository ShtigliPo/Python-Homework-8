def write_new(contact):
    with open('base.txt', 'a', encoding='utf8') as f:
        f.write(contact)

def get_book():
    book = []
    with open('base.txt', 'r', encoding='utf8') as f:
        for line in f:
            book.append(line)
    return book

def write_edited(mass):
    with open('base.txt','w', encoding='utf8') as f:
        for i in mass:
            f.write(i)