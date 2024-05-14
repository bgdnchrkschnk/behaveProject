import string

from behave import *
import random
from playwright.sync_api import expect


@given("Open a Firefox browser")
def open_browser(context):
    assert context.page


@when("Navigate to a google home page")
def navigate_google(context):
    context.page.goto(url="https://google.com.ua/")


@then("Google Home Page url is correct")
def check_home_page_url(context):
    assert context.page.url == "https://www.google.com.ua/"


@given('A google home page')
def home_google_page(context):
    context.page.goto(url="https://google.com.ua/")


@when('Search something in a search bar')
def search_in_search_bar(context):
    search_query = "".join(random.choices(string.ascii_letters, k=random.randint(a=1, b=5)))
    input_field = context.page.locator("textarea.gLFyf")
    input_field.type(search_query, delay=50)
    input_field.press(key="Enter")


@then('Central logo is not visible')
def check_central_logo_is_not_visible(context):
    central_logo = context.page.locator("img.lnXdpd")
    expect(central_logo).not_to_be_visible()


@then('Page url is not as home page')
def check_page_url_is_not_home_page(context):
    assert context.page.url != "https://www.google.com.ua/"
