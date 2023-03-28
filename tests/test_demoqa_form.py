from demoqa_tests.models.pages.registration_page import RegistrationPage


def test_fill_form(browser_setup):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.type_user_initials('Artem', 'Yurchenko')
    registration_page.type_email('yourchencore@yandex.ru')
    registration_page.chose_gender('Male')
    registration_page.type_user_phone_number('1234567890')
    registration_page.type_date_of_birth('1996', 'February', '09')
    registration_page.type_subject('Computer Science')
    registration_page.type_hobbies('Sports')
    registration_page.upload_picture('testt.jpg')
    registration_page.current_address('Ekaterinburg')
    registration_page.type_state('NCR')
    registration_page.type_city('Delhi')
    registration_page.submit_form()

    # THEN
    registration_page.should_registered_user_with(
        full_name='Artem Yurchenko',
        email='yourchencore@yandex.ru',
        gender='Male',
        phone_number='1234567890',
        date_of_birth='09 February,1996',
        subject='Computer Science',
        hobbies='Sports',
        picture='testt.jpg',
        address='Ekaterinburg',
        state_and_city='NCR Delhi'
    )
