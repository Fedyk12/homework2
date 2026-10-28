catalog = [
{"title": "Мастер и Маргарита", "author": "Булгаков",
"year": 1967, "genre": "роман", "on_loan": True},
{"title": "Евгений Онегин", "author": "Пушкин",
"year": 1833, "genre": "роман", "on_loan": False},
{"title": "Евгений Онегин", "author": "Пушкин",
"year": 1833, "genre": "роман", "on_loan": False},
{"title": "Стихотворения", "author": "Есенин",
"year": 1926, "genre": "поэзия", "on_loan": False},
{"title": "Вишнёвый сад", "author": "Чехов",
"year": 1904, "genre": "пьеса", "on_loan": True},
{"title": "Руслан и Людмила", "author": "Пушкин",
"year": 1820, "genre": "поэма", "on_loan": False},
{"title": "Три сестры", "author": "Чехов",
"year": 1901, "genre": "пьеса", "on_loan": False},
{"title": "Три сестры", "author": "Чехов",
"year": 1901, "genre": "пьеса", "on_loan": False},
]

def find_by_author(catalog,author):
    list_of_titles = {}
    for book in catalog:
        if book['author'] not in list_of_titles:
            list_of_titles[book['author']] = list_of_titles.get(book['author'],book['title'])
        else:
            list_of_titles[book['author']] += ' ,' + book['title']
    return list_of_titles
print(find_by_author(catalog,'Пушкин'))

def available_titles(catalog):
    list_of_titles = []
    for book in catalog:
        if book['on_loan'] == False:
            list_of_titles.append(book['title'])
    return list_of_titles

print(available_titles(catalog))

def books_grouped_by_genre(catalog):
    list_of_genre = {}
    books = []
    for book in catalog:
        if book['genre'] not in list_of_genre and book['on_loan'] == False:
            books.append(book['title'])
            list_of_genre[book['genre']] = list_of_genre.get(book['genre'],book['title'])
        elif book['genre'] in list_of_genre and book['on_loan'] == False:
            books.append(book['title'])
            list_of_genre[book['genre']] += ' ,' + book['title']
        elif book['genre'] in list_of_genre and book['on_loan'] == True:
            continue
        elif book['genre'] not in list_of_genre and book['on_loan'] == True:
            continue
    return list_of_genre
print(books_grouped_by_genre(catalog))
# {'title': 'Мастер и Маргарита', 'author': 'Булгаков', 'year': 1967, 'genre': 'роман', 'on_loan': True}














