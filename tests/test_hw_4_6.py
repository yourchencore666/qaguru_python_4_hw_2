from datetime import time

def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    current_time = time(hour=23)
    is_dark_theme = None

    if current_time.hour >= 22 or current_time.hour <= 6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True

    current_time = time(hour=16)
    dark_theme_enabled = True

    is_dark_theme = None

    if current_time.hour >= 22 or current_time.hour <= 6 or dark_theme_enabled:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suiable_user = None
    for user in users:
        if user["name"] == "Olga":
            suiable_user = user
            break

    assert suiable_user == {"name": "Olga", "age": 45}

    suiable_users = None
    suiable_users = []
    for user in users:
        if user["age"] < 20:
            suiable_users.append(user)

    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    #find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = None
    func_name = open_browser.__name__
    func_name_list = func_name.split("_")
    func_name_formatted = ' '.join(func_name_list).title()
    actual_result = f"{func_name_formatted} [{browser_name}]"
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = None
    func_name = go_to_companyname_homepage.__name__
    func_name_list = func_name.split("_")
    func_name_formatted = ' '.join(func_name_list).title()
    actual_result = f"{func_name_formatted} [{page_url}]"
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    func_name = find_registration_button_on_login_page.__name__
    func_name_list = func_name.split("_")
    func_name_formatted = ' '.join(func_name_list).title()
    actual_result = f"{func_name_formatted} [{page_url}, {button_text}]"
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"