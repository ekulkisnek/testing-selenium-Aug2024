from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def create_webdriver():
    options = Options()
    options.add_argument("--headless")  # Ensures Firefox runs in headless mode
    options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Bypass OS security model, required on many cloud platforms
    driver = webdriver.Firefox(options=options)
    return driver

def test_webdriver():
    driver = create_webdriver()
    try:
        driver.get("https://www.example.com")
        # Perform some actions, e.g., print the title to test if the setup works
        print("Title:", driver.title)
    finally:
        driver.quit()  # Make sure to close the driver

# Run the test
test_webdriver()
