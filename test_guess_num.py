from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]

for option in options:
    chrome_options.add_argument(option)


def test_site():
    print("Starting tests...")
    url = "http://localhost:3000/"
    try:
        se = Service(ChromeDriverManager(
            chrome_type="https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip").install())
    except:
        try:
            se = Service(ChromeDriverManager(
                chrome_type="https://chromedriver.storage.googleapis.com/99.0.4844.35/chromedriver_linux64.zip").install())
        except:
            se = Service(ChromeDriverManager(
                chrome_type="https://chromedriver.storage.googleapis.com/98.0.4758.48/chromedriver_linux64.zip").install())
    driver = webdriver.Chrome(service=se, options=chrome_options)
    print("Browser started successfully")
    driver.get(url)

    print("Page loaded successfully")

    # Find the elements
    game_title = driver.find_element(By.ID, "game_title")
    feedback = driver.find_element(By.ID, "guess_feedback")
    guess_input = driver.find_element(By.CLASS_NAME, "MuiInputBase-input")
    buttons = driver.find_elements(By.CLASS_NAME, "MuiButton-label")
    guess_button = buttons[0]
    guesses = driver.find_element(By.CLASS_NAME, "MuiTypography-root")
    reset_Button = buttons[1]
    how_to_play = buttons[2]
    # --------------------------------------------------------------------------------------------------------------
    # Test 1: Check if the elements exist and are displayed

    assert game_title is not None and game_title.is_displayed(), "Game title is missing"
    assert feedback is not None and feedback.is_displayed(), "Guessing number is missing"
    assert guess_input is not None and guess_input.is_displayed(), "Guess input is missing"
    assert guess_button is not None and guess_button.is_displayed(), "Guess button is missing"
    assert guesses is not None and guesses.is_displayed(), "Guesses are missing"
    assert reset_Button is not None and reset_Button.is_displayed(), "Reset button is missing"
    assert how_to_play is not None and how_to_play.is_displayed(
    ), "How to play button is missing"
    print("test 1- All elements are displayed")
    # --------------------------------------------------------------------------------------------------------------

    # Test 2: Check if the feedback text changes after a guess

    guess_input.clear()  # Clear any pre-filled text in the input field

    initial_feedback = feedback.text

    # Enter the number 40
    guess_input.send_keys('40')
    guess_button.click()

    # Enter the number 60
    guess_input.clear()
    guess_input.send_keys('60')
    guess_button.click()

    listNum = driver.find_elements(
        By.XPATH, "/html/body/div/div/div/div/div[3]/ul/li")

    # Extract the text from each element in the list
    num_list = [num.text for num in listNum]

    # Check if the feedback text has changed
    new_feedback = feedback.text
    assert initial_feedback != new_feedback, f"Feedback text did not change after guessing"

    # Check if the numbers '40' and '60' are both in the list of guessed numbers
    assert '40' in num_list, f"Guessed number 40 was not added to the list"
    assert '60' in num_list, f"Guessed number 60 was not added to the list"

    guess_input.clear()  # Clear the input field for the next test

    print("test 2- Feedback text changes after guessing a number")
    # --------------------------------------------------------------------------------------------------------------

    # Test 3: Check if the reset button works

    reset_Button.click()  # Click the reset button

    reset_feedback = feedback.text
    listNum_after_reset = driver.find_elements(
        By.XPATH, "/html/body/div/div/div/div/div[3]/ul/li")

    # Check if the feedback text has reset
    assert reset_feedback == initial_feedback, f"Feedback text did not reset after clicking the reset button"

    # Check if the number '40' is no longer in the list of guessed numbers
    assert len(
        listNum_after_reset) == 0, f"List of guessed numbers was not emptied after reset"

    print("test 3- Reset button functionality works correctly")

    # --------------------------------------------------------------------------------------------------------------

    print("All tests passed successfully")

    driver.quit()


# Call the test function
test_site()
