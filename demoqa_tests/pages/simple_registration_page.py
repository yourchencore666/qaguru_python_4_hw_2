from selene import have, command
from selene.support.shared import browser

from demoqa_tests.data.user import User


class SimpleRegistrationPage():
    def open(self):
        browser.open('/automation-practice-form')

    def type_user_initials(self, firstname, lastname):
        browser.element('[id="firstName"]').type(firstname)
        browser.element('[id="lastName"]').type(lastname)

    def chose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_user_phone_number(self, phone_number):
        browser.element('[id="userNumber"]').type(phone_number)

    def submit_form(self):
        browser.element('[id="submit"]').perform(command.js.click)

    def register(self, user: User):
        self.type_user_initials(user.first_name, user.last_name)
        self.chose_gender(user.gender)
        self.type_user_phone_number(user.phone_number)
        self.submit_form()

    def should_simple_registered_user_with(self, full_name, gender, phone_number):
        browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text(full_name))
        browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text(gender))
        browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(phone_number))
        return self
