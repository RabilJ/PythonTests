import pytest
from selenium import webdriver
from playwright.sync_api import sync_playwright

def new_test(a,b):
    assert a + b == 2

# try:
#     new_test(2,3)
# except Exception as e:
#     print(e)

driver = webdriver.Chrome()
driver.get("https://google.com")

try:
    assert "Gogle" in driver.title
except Exception as e:
    print("Title is not correct")

driver.quit()

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://google.com")
        assert "Example" in page.title()
        browser.close()
except Exception as e:
    print("Title is not correct 2")