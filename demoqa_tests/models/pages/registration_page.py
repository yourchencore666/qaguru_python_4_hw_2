from selene import have, command, by
from selene.support.shared import browser

from demoqa_tests import helpers


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def type_user_initials(self, firstname, lastname):
        browser.element('[id="firstName"]').type(firstname)
        browser.element('[id="lastName"]').type(lastname)

    def type_email(self, email):
        browser.element('[id="userEmail"]').type(email)

    def chose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_user_phone_number(self, phone_number):
        browser.element('[id="userNumber"]').type(phone_number)

    def type_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def type_subject(self, subject):
        browser.element('[id="subjectsInput"]').type(subject).press_enter()

    def type_hobbies(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbies)).click()

    def upload_picture(self, file_name):
        browser.element(by.id('uploadPicture')).send_keys(helpers.resources_path(file_name))

    def current_address(self, city):
        browser.element('[id="currentAddress"]').type(city)

    def type_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        return self

    def type_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def submit_form(self):
        browser.element('[id="submit"]').perform(command.js.click)

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
