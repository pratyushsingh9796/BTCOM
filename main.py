import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class BtComTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the WebDriver (Chrome in this example)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all test cases
        cls.driver.quit()

    def test_bt_com(self):
        driver = self.driver
        driver.get("https://www.bt.com/")

        # Add a delay after opening the URL
        time.sleep(2)

        # Wait for the cookie popup to appear
        cookie_popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="dialog"][aria-modal="true"]'))
        )

        # Switch to the cookie popup iframe
        try:
            iframe = cookie_popup.find_element(By.TAG_NAME, 'iframe')
            driver.switch_to.frame(iframe)
        except NoSuchElementException:
            pass

        # Locate the "Accept all cookies" button within the cookie popup
        accept_all_cookies_button = driver.find_element(By.CSS_SELECTOR, 'a.call')
        accept_all_cookies_button.click()

        # Add a delay after accepting cookies
        time.sleep(2)

        driver.switch_to.default_content()

        # Find the "Mobile" option
        mobile_option = driver.find_element("xpath", "//li[@class='bt-navbar-screen-sm-main']/a/span[contains(text(), 'Mobile')]")

        # Create an ActionChains object and perform the hover action
        actions = ActionChains(driver)
        actions.move_to_element(mobile_option).perform()

        # Wait for the element to be clickable with a polling mechanism
        wait = WebDriverWait(driver, 10)
        mobile_phones_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Mobile phones']")))

        mobile_phones_link.click()

        # Add a delay after clicking on Mobile phones
        time.sleep(2)

        # Scroll down until the target element is found
        target_element = driver.find_element("xpath",
                                             "//h3[text()='iPhone 15 Pro']/parent::div[@class='flexpay-card_text_container__KQznu']")
        driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        while not target_element.is_displayed():
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

        # Find all banner elements using a common class name which starts with flexpay-card_text_container
        banner_elements = driver.find_elements("css selector", '[class^="flexpay-card_text_container"]')

        # Check if there are at least 3 banner elements
        if len(banner_elements) >= 3:
            print("PASSED: TestCase 1- There are at least 3 banners present which are: ")
            for banner in banner_elements:
                print(f"'{banner.text.splitlines()[1]}' ")
        else:
            print("FAILED: TestCase 1- There are less than 3 banners present.")
            assert False, "FAILED: TestCase 1: There are less than 3 banners present."

        # Find the "View SIM only deals" link and scroll it into view
        sim_deals_link = driver.find_element("xpath", "//a[text()='View SIM only deals']")
        sim_deals_link.location_once_scrolled_into_view

        # Wait for the element to be clickable with a polling mechanism
        wait = WebDriverWait(driver, 10)
        sim_deals_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View SIM only deals']")))

        # Click on the "View SIM only deals" link
        sim_deals_link.click()
        time.sleep(2)

        # Validate the title for the new page
        expected_title = "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
        if driver.title == expected_title:
            print(f"PASSED: TestCase 2- The title for the new page matches i.e '{driver.title}'.")
        else:
            print(f"FAILED: TestCase 2- The title for the new page does not match: Expected - '{expected_title}', "
                  f"Actual - '{driver.title}'")
            assert False, "FAILED: TestCase 2- The title for the new page does not match."

        # Find all plan elements using a common class name
        target_elements = driver.find_elements("css selector", '[class^="simo-card-ee_product_card_wrapper"]')

        # Validating if “30% off and double data” was 125GB 250GB Essential Plan, was £27 £18.90 per month
        # plan is available or not
        found = False
        for plans in target_elements:
            plan_lines = plans.text.splitlines()
            if plan_lines[0] == '30% off and double data' and \
                plan_lines[1] == 'was 125GB' and \
                plan_lines[2] == '250GB' and \
                plan_lines[3] == 'Essential Plan' and \
                plan_lines[4] == 'was £27' and \
                plan_lines[5] == '£18.90' and \
                plan_lines[6] == 'Per month':
                print("PASSED: TestCase 3- The Required Plan is present in the Option List")
                found = True
                break

        self.assertTrue(found, "FAILED: TestCase 3- The Required Plan is NOT present in the Option List.")

if __name__ == "__main__":
    unittest.main()
