from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import time
import os

load_dotenv()
password = os.getenv('PASSWORD')
username = os.getenv('USERNNAME')

global browser
browser = None  # Initialize browser variable to None
# Path to the chromedriver executable
PATH = "C:/Program Files (x86)/chromedriver.exe"
service = Service(PATH, log_path="chromedriver.log", verbose=True)

# Setting Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the service and options
browser = webdriver.Chrome(service=service, options=chrome_options)
try:
    # Step 1: Navigate to the page
    browser.get("https://www.google.com")
    browser.get("https://jibu.africa")
    wait = WebDriverWait(browser, 20)

    wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.loading-scr")))

    # Login
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.header-tools.tools-pos2 a.tool-login"))).click()
    print("Clllllllllllllllllllicked")
    wait.until(EC.element_to_be_clickable((By.ID, "username"))
               ).send_keys(username)
    wait.until(EC.element_to_be_clickable(
        (By.ID, "password"))).send_keys(password)
    wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.loading-scr")))
    # browser.find_element(By.ID, "password").send_keys("1234")
    wait.until(EC.element_to_be_clickable((By.ID, "loginbtn"))).click()

    wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.loading-scr")))

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a.aalink.coursename.mb-1"))).click()
    print("COurrrrrrrrrrseeeeeeeeee")

    wait = WebDriverWait(browser, 30)

    wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.loading-scr")))

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.page-header-right button.manage-link"))).click()

    wait.until(EC.invisibility_of_element(
        (By.CSS_SELECTOR, "div.loading-scr")))

    participant_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//ul[@class='boxlist']//li//a[contains(text(), 'Participants')]")))

    participant_link.click()
    # Scroll into view and click
    # browser.execute_script(
    #     "arguments[0].scrollIntoView(true);", participant_link)

    print("PParrrrrrrrrrrrt")

    # Wait for the table to be present
    table = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "table.table-striped")))

    try:
        # Scroll the entire table into view once
        browser.execute_script("arguments[0].scrollIntoView(true);", table)
        time.sleep(1)  # Optional wait to ensure table is fully visible

        while True:
            rows = browser.find_elements(By.CSS_SELECTOR, "table tbody tr")
            roles_text = [row.find_element(
                        By.CSS_SELECTOR, "td.c3 span.inplaceeditable a.quickeditlink.aalink").text for row in rows]
            count = 0
            # Check if all roles are 'Student'
            if all(role == "Student" for role in roles_text):
                print("All rows contain 'Student'")
            else:
                print("Not all rows contain 'Student'")
                # Proceed with your loop or other processing
                for row in rows:
                    try:

                        # Move to the row and ensure it is interactable
                        ActionChains(browser).move_to_element(row).perform()
                        time.sleep(5)  # Ensures row is fully visible

                        # Scroll each row into view
                        # browser.execute_script("arguments[0].scrollIntoView(true);", row)

                        # Find the roles link
                        # roles_link = wait.until(EC.visibility_of_element_located(
                        #     (By.CSS_SELECTOR, "td.c3 span.inplaceeditable a.quickeditlink.aalink")))

                        # roles_link = wait.until(EC.element_to_be_clickable(
                        #     (By.CSS_SELECTOR, "td.c3 span.inplaceeditable a.quickeditlink.aalink")))
                        roles_link = row.find_element(
                            By.CSS_SELECTOR, "td.c3 span.inplaceeditable a.quickeditlink.aalink")
                        # Get the text of the roles link
                        time.sleep(1)
                        roles_text = roles_link.text
                        print(f'Roles text is {roles_text}')

                        if roles_text == "Student":
                            count += 1
                            print("in my counting errrrra")
                            continue  # Skips to next row
                        print("Just checked role text")

                        # The click to edit the role
                        # ActionChains(browser).move_to_element(roles_link).click().perform()
                        # roles_link.click()
                        # print("Clicked roles link")
                        browser.execute_script("arguments[0].click();", roles_link)
                        print("Clicked roles link using JavaScript")
                        time.sleep(0.5)

                        # wait and interact with the input box and enter 'Student'
                        input_box = wait.until(EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, "input.form-control")))

                        # input_box.send_keys("Student")
                        print("inPppppppput box 🍱")
                        time.sleep(0.2)
                        # input_box.click()
                        # browser.execute_script("arguments[0].dispatchEvent(new Event('focus', { bubbles: true }));", input_box)
                        browser.execute_script(
                            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", input_box)

                        # input_box.clear()
                        # input_box.send_keys("Student")

                        browser.execute_script(
                            "arguments[0].value = 'Student';", input_box)

                        # browser.execute_script("arguments[0].value = 'S';", input_box)
                        print("🐍🐍")

                        # Optional: Wait for the dropdown to populate
                        time.sleep(1)

                        input_box.send_keys(Keys.DOWN)
                        time.sleep(0.1)
                        input_box.send_keys(Keys.RETURN)

                        # Simulate clicking the input box using execute_script
                        # browser.execute_script("arguments[0].click();", input_box)
                        # # This line simulates pressing the Enter key in the input box
                        # browser.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));", input_box)
                        print("🚪🚪🚪")

                        # Wait for change
                        time.sleep(1)

                        # Click the save icon
                        saver = wait.until(EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, "a i.fa-floppy-o")))
                        saver.click()
                        count += 1
                        print("Save icon clicked")
                        time.sleep(0.5)

                    except Exception as e:
                        print(f"Error in row processing: {str(e)}")

            print(f'Student count is {count}')
            try:
                # next_button = wait.until(EC.element_to_be_clickable(
                #     (By.CSS_SELECTOR, "#participantsform > div > div.table-dynamic.position-relative > nav:nth-child(5) > ul > li:nth-child(13)")))

                next_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//li[@class='page-item']//span[contains(@class, 'sr-only') and contains(text(), 'Next page')]/parent::a")
                ))

                # next_button.click()
                browser.execute_script("arguments[0].click();", next_button)
                print("Next page")

                time.sleep(2)  # Wait for the next page to load
            except:
                print("No more pages.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")


except Exception as e:
    print(f"An error occurred: {e}")

# finally:
#     title = browser.title
#     print(title)
#     if browser:  # Only quit if the browser was successfully initialized
#         browser.quit()
