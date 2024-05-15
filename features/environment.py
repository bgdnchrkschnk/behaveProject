from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.firefox.launch(
        headless=False, slow_mo=500)
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    context.page.close()
    context.playwright.stop()


# def before_feature(context, feature):
#     context.playwright = sync_playwright().start()
#     context.browser = context.playwright.firefox.launch(
#         headless=False, slow_mo=500)
#     context.page = context.browser.new_page()
#
#
# def after_feature(context, feature):
#     context.page.close()
#     context.playwright.stop()