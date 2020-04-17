"""XML-формат предназначен для хранения и передачи данных. В этом формате представлены данные о книгах в файле books.xml.
Предлагается изучить способы работы Python с форматом XML и получить словарь с информацией о книгах.
Разработанная программа должна решать следующие задачи:
1. Вывести полную информацию по id книги.
2. Вывести полную информацию о книге по ISBN.
3. Подсчитать количество книг по заданному году издания.
4. Подсчитать среднюю стоимость книг по каждому издательству.
5. Вывести информацию о самой дорогой книге(ах) по заданным издательству и году издания."""

import xml.etree.cElementTree as ET

from pprint import pprint



class Storage:
    '''Imported data by reading from xml-file'''
    def __init__(self):
        self.tree = ET.parse('books.xml')
    def tree_root(self):
        self.root = self.tree.getroot()
        return  self.root


def get_book_id(id):
    '''Finding information about book by id'''

    book_list = Storage().tree_root()
    for book in book_list:

        if int(book.get('id')) == id:

            book_information = dict()

            for parameter in book:
                book_information[parameter.tag] = parameter.text
            return book_information


def get_id_ISBN(ISBN):
    '''Finding id by ISBN'''

    book_list = Storage().tree_root()
    for book in book_list:
        for parameter in book:
            if parameter.text == ISBN:
                return int(book.get('id'))


def count_books(year):
    '''Counting number of books by year'''

    book_list = Storage().tree_root()
    year_books = [child for child in book_list if child.find('Year_of_publishing').text == year]
    return len(year_books)


def average_price():
    '''Counting an average price of book by publisher'''
    Dict_publisher = dict()
    Dict_price = dict()

    for child in Storage().tree_root():
        for girl in child:
            if girl.tag == 'Publisher':
                Dict_publisher[girl.text] = 0

    for child in Storage().tree_root():
        for girl in child:
            if girl.text in Dict_publisher:
                Dict_publisher[girl.text] += 1

    for child in Storage().tree_root():
        for girl in child:
            if girl.tag == 'Price':
                Dict_price[child.find('Publisher').text] = 0

    for child in Storage().tree_root():
        for girl in child:
            if girl.text in Dict_price:
                Dict_price[child.find('Publisher').text] += float(child.find('Price').text)

    Dict_average_price = dict()

    for i in Dict_price.keys():
        if i in Dict_publisher.keys():
            Dict_average_price[i] = round(Dict_price[i]/Dict_publisher[i], 2)
    return Dict_average_price

    #for i in Dict_average_price.keys():
        #if i == publisher or i == publisher + '.':
            #return Dict_average_price[i]


def find_rich_books(rich_year, rich_publisher):
    '''Finding the most expensive book(s)
       by year and publisher'''

    def parameters_check(child, rich_year, rich_publisher):
        if child.find('Year_of_publishing').text == rich_year:
            if child.find('Publisher').text == rich_publisher or child.find('Publisher').text == (rich_publisher + '.'):
                return True
        else:
            return False

    id_rich_books = dict()

    for child in Storage().tree_root():
        if parameters_check(child, rich_year, rich_publisher) == True:
            id_rich_books[int(child.get('id'))] = float(child.find('Price').text)
    
    rich_books = dict()
    
    for i in id_rich_books.keys():
        if id_rich_books[i] == max(id_rich_books.values()):
            rich_books[i] = id_rich_books[i]

    for i in rich_books.keys():
        return get_book_id(i)


def main():
    header = 'Разработанная программа решает следующие задачи:'

    list_of_tasks = ['Вывести полную информацию по id книги.',
                     'Вывести полную информацию о книге по ISBN.',
                     'Подсчитать количество книг по заданному году издания.',
                     'Подсчитать среднюю стоимость книг по каждому издательству.',
                     'Вывести информацию о самой дорогой книге(ах) по заданным издательству и году издания.']
    

    print(header)

    for number, task in enumerate(list_of_tasks, 1):
        print(f"\t{number}. {task}")



    while True:

        def answer_check(answer):
            if answer.isdigit() == True:
                if int(answer) == 1 or int(answer) == 2:
                    return True
            else:
                return False

        def num_answer(answer):
            if int(answer) == 1:
                return True
            elif int(answer) == 2:
                return False

        while True:

            try:
                num_task = int(input('Введите номер задачи:'))
                break
            except Exception:
                print('Попробуйте ещё раз!')

        if num_task == 1:

            while True:
                try:
                    id_input = int(input('Введите id книги:'))
                    break
                except Exception:
                    print('Попробуйте ещё раз!')


            result = get_book_id(id_input)
            if result == None or result == {}:
                print('К сожалению, такой книги нет.')

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break
            else:

                pprint(result)

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break

        elif num_task == 2:
            ISBN_input = input('Введите ISBN:')

            result = get_book_id(get_id_ISBN(ISBN_input))
            if result == None or result == {}:

                print('К сожалению, такой книги нет.')

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break
            else:
                pprint(result)

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break


        elif num_task == 3:
            year_input = input('Введите год:')
            result = count_books(year_input)
            if result == 0:

                print(result)
                print('К сожалению, по заданному году издания книг нет.')

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break
            else:

                print(result)

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break

        elif num_task == 4:

            #publisher_input = input('Введите издательство:')
            result = average_price()
            pprint(result)

            while True:
                answer = input('1 - Продолжить, 2 - Выход:')
                if answer_check(answer) == True:
                    break
                else:
                    print('Попробуйте ещё раз!')

            if num_answer(answer) == True:
                continue
            elif num_answer(answer) == False:
                break

        elif num_task == 5:
            rich_year_input = input('Введите год издания:')
            rich_publisher_input = input('Введите издательство:')
            result = find_rich_books(rich_year_input, rich_publisher_input)

            if result == {} or result == None:
                print('К сожалению, по заданным параметрам книг нет.')

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break
            else:
                pprint(result)

                while True:
                    answer = input('1 - Продолжить, 2 - Выход:')
                    if answer_check(answer) == True:
                        break
                    else:
                        print('Попробуйте ещё раз!')

                if num_answer(answer) == True:
                    continue
                elif num_answer(answer) == False:
                    break

if __name__ == '__main__':
    main()
