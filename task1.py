text = 'Идут короче два барана по полю,один говорит :"бе" ,второй говорит:"я тоже самое хотел сказать"'
rus_alphavit = 'йцукенгшщзхъфывапролджэячсмитьбюё'
text_only_bukvi_lowercase = ''
for symbol in text.lower():
    if symbol == ' ':
        text_only_bukvi_lowercase += ' '
    if symbol not in rus_alphavit:
        symbol = ' '
        text_only_bukvi_lowercase += symbol
    if symbol in rus_alphavit:
        text_only_bukvi_lowercase += symbol
unique_words = {}
cnt_words = 0
text_only_bukvi_lowercase.split(' ')
text_only_bukvi_lowercase.split(' ')
text_words = text_only_bukvi_lowercase.split(' ')
for word in text_words:
    if word != ' ' and word != '':
        cnt_words += 1
        if word not in unique_words:
            unique_words[word] = unique_words.get(word,0) + 1
        else:
            unique_words[word] += 1
print(unique_words)
print(f'Всего слов : {cnt_words} ,из них уникальных {len(unique_words)}')
top_words = []
for word in unique_words:
    top_words.append([-unique_words[word],word])
top_words.sort()
top_words = [[word[1],abs(word[0])]   for word in top_words]
top_5_words = []
cnt = 0
if len(top_words) >= 5:
    for word in top_words:
        top_5_words.append(word)
        cnt += 1
        if cnt == 5:
            break
else:
    for word in top_words:
        top_5_words.append(word)

print(f'Топ-5 слов :{top_5_words}')
max_length = max([len(word) for word in text_words])
print(max_length)
for word in text_words:
    if len(word) == max_length:
        print(f'Самое длинное слово : {word}')
        break
length = {}
for word in text_words:
    if word != '':
        length[len(word)] = length.get(len(word),unique_words[word])

print(length)















