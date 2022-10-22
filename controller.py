import logger
import model

while True:
    mode = model.choose_mode()
    if mode == 1:
        logger.write_new(model.get_contact())
    elif mode == 2:
        contact = model.get_request()
        book = logger.get_book()
        print(model.find_contact(book,contact))
    elif mode == 3:
        base = logger.get_book()
        new_base = model.editing(base)
        logger.write_edited(new_base)
    elif mode == 0:
        print('Выход')
        break
    else:
        print('Такого режима нет')