import allure
from selene import have, command, by
from selene.support.shared import browser

from demoqa_tests import helpers


class RegistrationPage:
    @allure.step('Открыть главную страницу')
    def open(self, url):
        browser.open(url)
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    @allure.step('Ввести имя и фамилию')
    def type_user_initials(self, firstname, lastname):
        browser.element('[id="firstName"]').type(firstname)
        browser.element('[id="lastName"]').type(lastname)

    @allure.step('Ввести электронную почту')
    def type_email(self, email):
        browser.element('[id="userEmail"]').type(email)

    @allure.step('Выбрать пол')
    def chose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    @allure.step('Ввести номер телефона')
    def type_user_phone_number(self, phone_number):
        browser.element('[id="userNumber"]').type(phone_number)

    @allure.step('Выбрать дату рождения')
    def type_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    @allure.step('Выбрать школьный предмет')
    def type_subject(self, subject):
        browser.element('[id="subjectsInput"]').type(subject).press_enter()

    @allure.step('Выбрать хобби')
    def type_hobbies(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbies)).click()

    @allure.step('Загрузить картинку')
    def upload_picture(self, file_name):
        browser.element(by.id('uploadPicture')).send_keys(helpers.resources_path(file_name))

    @allure.step('Ввести текущий адрес')
    def current_address(self, city):
        browser.element('[id="currentAddress"]').type(city)

    @allure.step('Выбрать государство')
    def type_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        return self

    @allure.step('Выбрать страну')
    def type_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    @allure.step('Подтвердить форму регистрации')
    def submit_form(self):
        browser.element('[id="submit"]').perform(command.js.click)

    @allure.step('Проверить заполненные данные')
    def should_registered_user_with(self,
                                    full_name,
                                    email,
                                    gender,
                                    phone_number,
                                    date_of_birth,
                                    subject,
                                    hobbies,
                                    picture,
                                    address,
                                    state_and_city
                                    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobbies,
                picture,
                address,
                state_and_city,
            )
        )
        return self