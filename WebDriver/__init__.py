from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# class DriverUtils:
#
#     def fetch_url(path, url, xpath, title):
#         driver = Driver(path)
#         driver.get(url)
#         driver.inputValue(xpath, title)
#
#         html = driver.page_source()
#         driver.quit()


class Driver:

    def __init__(self, driverPath):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=driverPath,
                                       chrome_options=chromeOptions)

        # fireFoxOptions = webdriver.FirefoxOptions()
        # # fireFoxOptions.set_headless()
        #
        # self.driver = webdriver.Firefox(executable_path=driverPath,
        #                                 firefox_options=fireFoxOptions)

    def get(self, url):
        """WebDriver goto URL"""
        self.driver.get(url)

    def input_value(self, xpath, text):
        """Find Xpath, enter text, & press ENTER"""
        elem = self.driver.find_element_by_xpath(xpath)
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)
        sleep(2)  # seconds

    def click(self, xpath):
        """Find Xpath and click"""
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()

    def click_css(self, selector):
        """Find Css selector and click"""
        elem = self.driver.find_element_by_css_selector(selector)
        elem.click()

    def open_tab(self, url):
        """Open new tab"""
        self.driver.execute_script(f"window.open('https://www.google.com/');")

    def page_source(self):
        """return html of current page"""
        return self.driver.page_source

    def quit(self):
        """Exit WebDriver"""
        return self.driver.quit()
