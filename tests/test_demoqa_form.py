from selene import browser, by, be, have
import os


def test_fill_form(browser_setup):
    #fill the form
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type('Artem')
    browser.element('[id="lastName"]').should(be.blank).type('Yurchenko')
    browser.element('[id="userEmail"]').should(be.blank).type('yourchencore@yandex.ru')
    browser.element('label[for="gender-radio-1"]').click().should(have.text('Male'))
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('.react-datepicker__month-select option[value="1"]').click()
    browser.element('.react-datepicker__year-select option[value="1996"]').click()
    browser.all('.react-datepicker__day--009')[0].click()
    browser.element('[id="dateOfBirthInput"]').should(have.value('09 Feb 1996'))
    browser.element('[id="subjectsInput"]').should(be.blank).type('Computer Science').press_enter()
    browser.element('.subjects-auto-complete__multi-value__label').should(have.text('Computer Science'))
    browser.element('label[for="hobbies-checkbox-1"]').click().should(have.text('Sports'))
    browser.element(by.id('uploadPicture')).send_keys(os.getcwd() + '/resources/testt.jpg')
    browser.element('[id="currentAddress"]').should(be.blank).type('Ekaterinburg')
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('[id="state"]').should(have.text('NCR'))
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    browser.element('[id="city"]').should(have.text('Delhi'))
    browser.element('[id="submit"]').click()

    #assertion data for for after submit
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive tbody tr').should(have.size(10))
    browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text('Artem Yurchenko'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text('yourchencore@yandex.ru'))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Male'))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text('1234567890'))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('09 February,1996'))
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('Computer Science'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Sports'))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text('Ekaterinburg'))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text('NCR Delhi'))


