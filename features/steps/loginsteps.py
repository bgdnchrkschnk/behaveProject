from behave import *
from playwright.sync_api import expect


@given('Login page of Sample App')
def navigate_to_login_page(context):
    context.page.goto(url="http://www.uitestingplayground.com/sampleapp")


@when('Type username "{username}" and password "{password}"')
def fill_username_and_password(context, username, password):
    context.page.get_by_placeholder("User Name").type(username, delay=500)
    context.page.get_by_placeholder("********").type(password, delay=500)


@when('Click Log In button')
def click_login_button(context):
    context.page.locator("#login").click()


@then('Success message is displayed')
def assert_success_message(context):
    login_status_label = context.page.locator("#loginstatus")
    expect(login_status_label).to_have_class("text-success")
