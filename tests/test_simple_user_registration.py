from demoqa_tests.pages.simple_registration_page import SimpleRegistrationPage
from demoqa_tests.data.user import artem


def test_simple_user_registration(browser_setup):
    simple_registration_page = SimpleRegistrationPage()

    simple_registration_page.open()
    simple_registration_page.register(user=artem)
    simple_registration_page.should_simple_registered_user_with(full_name='Artem Yurchenko',
                                                                gender='Male',
                                                                phone_number='1234567890')
