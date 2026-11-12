from time import sleep

from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

def test_form_fill(page: Page):
    page.goto("https://demoqa.com/")
# Переходим к формам
    page.locator("h5", has_text="Forms").click()
    expect(page).to_have_url(
        "https://demoqa.com/forms", )

# Нажимаем на элемент, который приведет нас к форме для заполнения
    page.locator("li", has_text="Practice Form").click()
    expect(page).to_have_url("https://demoqa.com/automation-practice-form")

# Проверяем, что форма открылась и видима
    form_header = page.locator(".text-center", has_text="Practice Form")
    form_subtitle = page.locator("h5", has_text="Student Registration Form")

    expect(form_header).to_be_visible()
    expect(form_subtitle).to_be_visible()
    expect(form_header).to_have_text("Practice Form")
    expect(form_subtitle).to_have_text("Student Registration Form")

# Генерим данные для пользователя

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    mobile_number = fake.numerify("##########")
    current_address = fake.address()

# Заполняем анкету
# Поля
    first_name_field = page.get_by_placeholder("First Name")
    last_name_field = page.get_by_placeholder("Last Name")
    email_field = page.get_by_placeholder("name@example.com")
    mobile_number_field = page.get_by_placeholder("Mobile Number")
    current_address_field = page.get_by_placeholder("Current Address")

    first_name_field.click()
    first_name_field.press_sequentially(first_name, delay=50)

    last_name_field.click()
    last_name_field.press_sequentially(last_name, delay=50)

    email_field.click()
    email_field.press_sequentially(email, delay=50)

    mobile_number_field.click()
    mobile_number_field.press_sequentially(mobile_number, delay=50)

    current_address_field.click()
    current_address_field.press_sequentially(current_address, delay=50)

    form_header.click()
    expect(current_address_field).to_have_value(current_address)
    expect(mobile_number_field).to_have_value(mobile_number)
    expect(email_field).to_have_value(email)
    expect(last_name_field).to_have_value(last_name)
    expect(first_name_field).to_have_value(first_name)

# Выбор пола
    page.get_by_role("radio", name="Male", exact=True).check()

    expect(page.get_by_role("radio", name="Male", exact=True)).to_be_checked()
    expect(page.get_by_role("radio", name="Female", exact=True)).not_to_be_checked()
    expect(page.get_by_role("radio", name="Other", exact=True)).not_to_be_checked()

# Выбираем хобби
    page.get_by_role("checkbox", name="Sports", exact=True).check()
    page.get_by_role("checkbox", name="Reading", exact=True).check()

    expect(page.get_by_role("checkbox", name="Sports", exact=True)).to_be_checked()
    expect(page.get_by_role("checkbox", name="Reading", exact=True)).to_be_checked()
    expect(page.get_by_role("checkbox", name="Music", exact=True)).not_to_be_checked()

# Выбор города и штата
    select_city = page.locator("#city")
    select_state = page.locator("#state")

    select_state.click()
    page.get_by_role("option", name="NCR", exact=True).click()
    expect(page.locator("#state")).to_contain_text("NCR")

    select_city.click()
    page.get_by_role("option", name="Noida", exact=True).click()
    expect(page.locator("#city")).to_contain_text("Noida")

# Выбор предметов
    subject_input = page.locator("#subjectsContainer")

    subject_input.click()
    subject_input.press_sequentially("ma", delay=50)
    page.get_by_role("option", name="Maths", exact=True).click()

    subject_input.click()
    subject_input.press_sequentially("en", delay=50)
    page.get_by_role("option", name="English", exact=True).click()

    expect(page.locator("#subjectsContainer")).to_contain_text("Maths")
    expect(page.locator("#subjectsContainer")).to_contain_text("English")

# Кликаем на кнопку отправки
    submit_button = page.get_by_role("button", name="Submit")
    modal_table = page.locator(".modal-content")
    submit_button.click()
    expect(modal_table).to_be_visible()


