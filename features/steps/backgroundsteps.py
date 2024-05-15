from behave import *
from playwright.sync_api import expect
from playwright.sync_api import Page

@given('Open a browser')
def launch_browser(context):
    context.browser = context.playwright.firefox.launch(
        headless=False, slow_mo=500
    )
    context.page: Page = context.browser.new_page()


@when('Go to ask.fm')
def go_to_ask_fm(context):
    context.page.goto(url="https://ask.fm/")


@when('Refresh page')
def refresh_page(context):
    context.page.reload()


@then('Assert logo')
def assert_logo(context):
    logo = context.page.locator(".logo>img")
    expect(logo).to_be_visible()


@then('Click to Sign In')
def click_sign_in_button(context):
    sign_in_btn = context.page.locator("a[data-action='ClickTrack']")
    sign_in_btn.click()


@then('Assert username')
def assert_username(context):
    username_field = context.page.locator("input#user_name")
    expect(username_field).to_be_visible()


@then('Assert password')
def assert_password(context):
    password_field = context.page.locator("input#user_password")
    expect(password_field).to_be_visible()