from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
from time import sleep

browser = webdriver.Chrome()
browser.implicitly_wait(5)
scheduler = schedule.Scheduler()


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        try:
            # Locate login inputs and buttons
            username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
            password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
            username_input.send_keys(username)
            password_input.send_keys(password)

            login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            # Handle 'Not Now' pop-ups
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']"))
            ).click()

            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']"))
            ).click()

        except NoSuchElementException:
            print("Login elements not found")

        # Navigating to the desired page
        try:
            sleep(5)
            self.browser.get("Enter URL of the page")

            # Attempt to click Follow Back if available
            follow = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Follow Back']"))
            )
            follow.click()

        except NoSuchElementException:
            print("Follow button not found...")

        try:
            # Open the first picture
            picture = browser.find_element(By.XPATH, "//div[@class='_aagw']")
            picture.click()

            # Wait and like the post
            sleep(2)
            like_btn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Like']"))
            )
            like_btn.click()

            # Comment on the post
            sleep(2)
            comment = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']"))
            )
            comment.send_keys("....")

            # Submit the comment
            post = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_am-5']"))
            )
            post.click()

        except NoSuchElementException:
            print("Picture or Like button not found")

        sleep(8)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com')

    def go_to_login_page(self):
        try:
            login_link = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']"))
            )
            login_link.click()
            return LoginPage(self.browser)
        except NoSuchElementException:
            print("Login form not found")


# Schedule task to run every 2 minutes
schedule.every(2).minutes.do(HomePage, browser)

homepage = HomePage(browser)
login_page = homepage.go_to_login_page()
login_page.login("Enter your user name", "Enter your password")

# While loop to continuously run scheduled tasks
while True:
    schedule.run_pending()
    sleep(1)

browser.close()
