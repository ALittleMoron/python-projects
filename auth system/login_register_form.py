"""
Пока что этот кусок кода будет отвечать за непосредственный
логин и регистрацию в абстрактную систему. Происходить все
будет через консоль, потом постараюсь добавить GUI.
"""
# карявый тайпхинтинг, но что поделать...
Username, Password = str, str
Input = (str, str)


def choose_menu() -> Input:
    """ выбор между логином или регистрацией """
    print('Что вы хотите сделать?', '1. Войти в систему',
          '2. Зарегистрироваться', sep = '\n')
    choice = input('Ответ [1/2]: ')
    if choice == '1':
        return input_print()
    elif choice == '2':
        return input_print()
    else:
        print('Что-то пошло не так. Попробуйте ещё раз!\n')


def input_print() -> (Username, Password):
    username = input('\nВведите логин (имя пользователя): ')
    password = input('введите ваш пароль: ')
    return username, password


if __name__ == "__main__":
    a = choose_menu()
    print(a)