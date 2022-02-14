import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager


# constants
EMAIL = ""
PW = ""
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103350119&keywords=python%20developer&location=Italy"


# driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(30)

# use driver to open the page
webpage = driver.get(URL)

# LOGIN
login = driver.find_element(By.LINK_TEXT, "Sign in")
login.click()

username = driver.find_element(By.ID, "username")
pw = driver.find_element(By.ID, "password")

# pass in data
username.send_keys(EMAIL)
pw.send_keys(PW)
button = driver.find_element(By.CLASS_NAME, "btn__primary--large")

time.sleep(4)
button.click()

# LIST OF AVAILABLE JOBS
time.sleep(5)
available_jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")

for job in available_jobs:
    job.click()

    # check if button for easy apply exists
    try:
        time.sleep(2)
        button_easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    except NoSuchElementException:
        # skip iteration and go to the next one if button is not available
        continue

    # if button exists, then apply
    else:
        button_easy_apply.click()

        # submit application
        time.sleep(5)
        submit_application = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
        # check if application is a one-step application
        if submit_application.text == "Submit application":
            submit_application.click()
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-button--circle").click()
        # if not, it's an application with several steps
        else:
            close_modal = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            discard = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar .artdeco-button--primary').click()

driver.close()
