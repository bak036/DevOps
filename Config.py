from selenium import webdriver
import unittest

class GetURL(unittest.TestCase):

    def set_up(self):
        self.driver = webdriver.Chrome(executable_path='C:/automation/drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)1


    def get_url(self):
        driver=self.driver
        driver.get("https://buyme.co.il/")
        get_title = driver.title
        if get_title=="ביימי: שוברי מתנה, Gift Card בעיצוב אישי | BuyMe":
            return (driver)
        else:
            print("Title is not exist")

    def Close_browser(self):
        self.driver.quit()



