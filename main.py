from playwright.sync_api import sync_playwright

def describe_website(url = "https://google.com"):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    # Click the first link on the page
    page.click("a")

    # Get and print the current URL
    new_url = page.url
    print(f"New URL: {new_url}")

describe_website("https://google.com")

while True:
    pass

# browser.close()  # Commented out to keep the browser open


