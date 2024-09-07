def ask_question(question, options):
    print(question)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    choice = int(input("Выберите вариант ответа: "))
    return choice


def main():
    print("Добро пожаловать! Давайте выясним, какая книга Стивена Кинга вам подходит.")

    print("Ваше предпочтение в жанрах?")
    genre_options = ["Ужасы", "Триллер", "Фантастика", "Драма"]
    genre_choice = ask_question("Выберите жанр:", genre_options)

    if genre_choice == 1:
        horror()
    elif genre_choice == 2:
        thriller()
    elif genre_choice == 3:
        fantasy()
    elif genre_choice == 4:
        drama()
    else:
        print("Некорректный ввод.")


def horror():
    horror_options = ["Сверхъестественные", "Реалистичные", "Психологические"]
    horror_choice = ask_question("Какие ужасы вам нравятся больше?", horror_options)

    if horror_choice == 1:
        supernatural_horror()
    elif horror_choice == 2:
        realistic_horror()
    elif horror_choice == 3:
        psychological_horror()
    else:
        print("Некорректный ввод.")


def supernatural_horror():
    mood_options = ["Тревожное и гнетущее", "Мистическое и загадочное"]
    mood_choice = ask_question("Какое настроение вам предпочтительнее?", mood_options)

    if mood_choice == 1:
        print("Вам подойдет книга 'Оно'.")
    elif mood_choice == 2:
        print("Вам подойдет книга 'Сияние'.")
    else:
        print("Некорректный ввод.")


def realistic_horror():
    aspect_options = ["Психологический", "Социальный"]
    aspect_choice = ask_question("Какой аспект реалистичных ужасов вам интересен?", aspect_options)

    if aspect_choice == 1:
        print("Вам подойдет книга 'Мизери'.")
    elif aspect_choice == 2:
        print("Вам подойдет книга 'Кэрри'.")
    else:
        print("Некорректный ввод.")


def psychological_horror():
    subgenre_options = ["Триллер", "Психологическая драма"]
    subgenre_choice = ask_question("Какой поджанр вам интересен?", subgenre_options)

    if subgenre_choice == 1:
        print("Вам подойдет книга 'Мобильник'.")
    elif subgenre_choice == 2:
        print("Вам подойдет книга 'Долорес Клейборн'.")
    else:
        print("Некорректный ввод.")


def thriller():
    thriller_options = ["Мистический", "Криминальный", "Психологический"]
    thriller_choice = ask_question("Какой вид триллера вам нравится?", thriller_options)

    if thriller_choice == 1:
        mystical_thriller_fantasy()
    elif thriller_choice == 2:
        print("Вам подойдет книга 'Мистер Мерседес'.")
    elif thriller_choice == 3:
        print("Вам подойдет книга 'Мертвая зона'.")
    else:
        print("Некорректный ввод.")


def mystical_thriller_fantasy():
    mystical_thriller_options = ["Да", "Нет"]
    mystical_thriller_choice = ask_question("Вы читали 'Сияние'?", mystical_thriller_options)

    if mystical_thriller_choice == 1:
        print("Вам подойдет книга 'Доктор сон'.")
    elif mystical_thriller_choice == 2:
        print("Вам подойдет книга 'Чужак'.")
    else:
        print("Некорректный ввод.")



def fantasy():
    fantasy_options = ["Магия", "Без магии", "Постапокалипсис"]
    fantasy_choice = ask_question("Хотите ли вы, чтобы в книге присутствовала магия?", fantasy_options)

    if fantasy_choice == 1:
        magical_fantasy()
    elif fantasy_choice == 2:
        no_magical_fantasy()
    elif fantasy_choice == 3:
        post_apocalyptic_fantasy()
    else:
        print("Некорректный ввод.")


def magical_fantasy():
    magical_options = ["Элементы мистики", "Чистая магия"]
    magical_choice = ask_question("Вас интересуют книги с элементами мистики и загробного мира?", magical_options)

    if magical_choice == 1:
        mysticism()
    elif magical_choice == 2:
        print("Вам подойдет книга 'Талисман'.")
    else:
        print("Некорректный ввод.")


def mysticism():
    mysticism_options = ["Да", "Нет"]
    mysticism_choice = ask_question("Готовы ли вы прочитать 8 книг, а потом разочароваться в концовке?", mysticism_options)

    if mysticism_choice == 1:
        print("Вам подойдет книжная серия 'Темная башня'.")
    elif mysticism_choice == 2:
        print("Вам подойдет книга 'Глаза Дракона'.")
    else:
        print("Некорректный ввод.")


def no_magical_fantasy():
    character_options = ["Да", "Нет"]
    character_choice = ask_question("Интересен ли вам лор вселенной Стивена Кинга?", character_options)

    if character_choice == 1:
        print("Вам подойдет книга 'Сердца в Атлантиде'.")
    elif character_choice == 2:
        print("Вам подойдет книга 'Под куполом'.")
    else:
        print("Некорректный ввод.")


def post_apocalyptic_fantasy():
    setting_options = ["Романы", "Малая проза"]
    setting_choice = ask_question("Вам интересны романы или малая проза?", setting_options)

    if setting_choice == 1:
        novel_fantasy()
    elif setting_choice == 2:
        print("Вам подойдет книга 'Туман' из сборника 'Команда скелетов'.")
    else:
        print("Некорректный ввод.")


def novel_fantasy():
    novel_options = ["Не связанный с действиями человека", "Связанный с действиями человека"]
    novel_choice = ask_question("Какой вариант апокалипсиса кажется вам более возможным?", novel_options)

    if novel_choice == 1:
        print("Вам подойдет книга 'Противостояние'.")
    elif novel_choice == 2:
        print("Вам подойдет книга 'Мобильник'.")
    else:
        print("Некорректный ввод.")


def drama():
        drama_options = ["Семейные истории", "Социальные драмы", "Психологические драмы"]
        drama_choice = ask_question("Какая тематика драм вам интересна?", drama_options)

        if drama_choice == 1:
            family_drama()
        elif drama_choice == 2:
            social_drama()
        elif drama_choice == 3:
            psychological_drama()
        else:
            print("Некорректный ввод.")


def family_drama():
    family_drama_options = ["Да", "Нет"]
    family_drama_choice = ask_question("Вас нравятся истории, сюжет в которых развивается очень медленно?", family_drama_options)

    if family_drama_choice == 1:
        print("Вам подойдет книга 'Мешок с костями'.")
    elif family_drama_choice == 2:
        print("Вам подойдет книга 'Кладбище домашних животных'.")
    else:
        print("Некорректный ввод.")


def social_drama():
    social_drama_options = ["Да", "Нет"]
    social_drama_choice = ask_question("Вам интересны истории с элементами фантастики?", social_drama_options)

    if social_drama_choice == 1:
        print("Вам подойдет книга 'Зелёная миля'.")
    elif social_drama_choice == 2:
        print("Вам подойдет книга 'Долгая прогулка'.")
    else:
        print("Некорректный ввод.")


def psychological_drama():
    psychological_drama_options = ["Да", "Нет"]
    psychological_drama_choice = ask_question("Вам интересны истории с элементами фантастики?", psychological_drama_options)

    if psychological_drama_choice == 1:
        print("Вам подойдет книга 'История Лизи'.")
    elif psychological_drama_choice == 2:
        print("Вам подойдет книга 'Дорожные работы'.")
    else:
        print("Некорректный ввод.")


if __name__ == "__main__":
    main()
