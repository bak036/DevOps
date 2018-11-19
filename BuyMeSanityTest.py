import Config
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


class SanityTest():

    def RegistrationScreen(self,driver,username,password,email):


        #LOGIN/REGISTRATION PANEL
        driver.find_element_by_css_selector(".seperator-link").click()
        driver.find_element_by_css_selector(".text-btn").click()

        #FILL REGISTRATION FORM
        driver.find_element_by_xpath("//*[@type='text']").send_keys(username+ Keys.ENTER)
        driver.find_element_by_xpath("//*[@type='email']").send_keys(email+ Keys.ENTER)
        driver.find_element_by_xpath("//*[@type='password']").send_keys(password+ Keys.ENTER)
        driver.find_element_by_xpath("//*[@placeholder='אימות סיסמה']").send_keys(password)
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_xpath("//*[@type='submit']").submit()
        driver.implicitly_wait(20)


    def SignInScreen(self,driver,email,password):

         #LOGIN/REGISTRATION PANEL
        driver.find_element_by_css_selector(".seperator-link").click()
        #driver.find_element_by_css_selector(".text-btn").click()

         #SIGN IN SCREEN
        email_field = driver.find_element_by_xpath("//*[@type='email']")
        psw_field = driver.find_element_by_xpath("//*[@type='password']")
        email_field.send_keys(email + Keys.ENTER)
        psw_field.send_keys(password + Keys.ENTER) # Submit Login form

        # error_message = driver.find_element_by_class_name("login-error") #If Login fault - fill the default values
        # if error_message.is_displayed():
        #     email_field.clear()
        #     email_field.send_keys("a@ggllaaalal.com" + Keys.ENTER)
        #
        #     psw_field.clear()
        #     psw_field.send_keys("Oo12345678" + Keys.ENTER)


    def HomePage(self,driver):

        time.sleep(3)

        #Select amount range
        driver.find_element_by_xpath("//div/a/span").click()
        driver.find_element_by_css_selector(".active-result:nth-child(3)").click()# 100-199 range amount

        # Select Area
        driver.find_element_by_xpath("//div[2]/a/span").click()
        driver.find_element_by_css_selector(".active-result:nth-child(2)").click()

        #Select Category
        driver.find_element_by_xpath("//div[3]/a/span").click()
        driver.find_element_by_xpath("//div[3]/div/ul/li[3]").click()


        # Submit selected query
        driver.find_element_by_xpath("//form/a").click()

        time.sleep(2)

        # CHOOSE CLARO REST

        driver.find_element_by_xpath("//a[2]/div").click()


    def BuissnesSelect(self,driver,amount,email):
        time.sleep(3)
        clr_summa_fieald = driver.find_element_by_xpath("//*[@placeholder='מה הסכום?']")
        clr_summa_fieald.clear()
        clr_summa_fieald.send_keys(amount + Keys.ENTER) # Pass down the amount and open a new form
        driver.implicitly_wait(20)


        #SELECT RADIO BOX - למי המתנה
        driver.find_element_by_xpath("//label[2]/span").click()
        driver.find_element_by_xpath("//label/span").click()

        #Fill Receiver person
        clr_receiver_fld = driver.find_element_by_xpath("//div[2]/label/input")
        clr_receiver_fld.clear()
        clr_receiver_fld.send_keys("לאישתי")

         #Fill Sender person
        clr_sender_fld = driver.find_element_by_xpath("//label[2]/input")
        clr_sender_fld.clear()
        clr_sender_fld.send_keys("אלכס")

        #SELECT EVENT DROM LIST

        driver.find_element_by_xpath("//label/div/a/span").click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("//label/div/div/ul/li[2]").click()

        #ADD LOCAL IMAGE

        image_path = 'C:\\123.PNG'
        image_select = driver.find_element_by_xpath("//div[2]/div/label/input")
        image_select.send_keys(image_path)
        time.sleep(10)

        #PICK EMAIL FOR SENDINF GIFT

        # if driver.find_element_by_css_selector(".btn.btn-cancel-send-option").is_displayed():
        #     is_element_close = driver.find_element_by_css_selector(".btn.btn-cancel-send-option")
        #         if is_element_close.is_displayed():
        #             is_element_close.click()

        driver.find_element_by_css_selector(".btn-send-option-inner > .icon-envelope").click()
        driver.find_element_by_xpath("//div[4]/div/div[3]/div/div/div/div/input").clear()
        driver.find_element_by_xpath("//div[4]/div/div[3]/div/div/div/div/input").send_keys(email)
        driver.find_element_by_css_selector(".btn-save").click()
        driver.implicitly_wait(10)

        #SEND FORM TO PAYMENT STAGE
        driver.find_element_by_css_selector(".submit-wrapper > .btn").click()
        time.sleep(3)

def main():
        username = "alex"
        password = "Oll2345678"
        email = "zxzx123@g.com"
        amount = "500"

        login_test = SanityTest() # Create object of Class SanityTest
        configFile = Config.GetURL() # Call external Config Class (SetUp/GetUrl/Close browser functions)
        configFile.set_up()# Call set_up function for Running Chrome driver
        driver = configFile.get_url()# Call get_url function for openning www.buyme.co.il url

        login_test.RegistrationScreen(driver,username,password,email)# Call function for first Registration
        configFile.Close_browser() #Close and quite from a current browser
        configFile.set_up()# Call set_up function for Running Chrome driver
        driver = configFile.get_url()# Call get_url function for openning www.buyme.co.il url

        login_test.SignInScreen(driver,email,password) # Call function for Sign In
        login_test.HomePage(driver)# Call function for selecting parameters
        login_test.BuissnesSelect(driver,amount,email) #Send a wish amount for selected gift
        configFile.Close_browser() #Close and quite from a current browser
        print("Congratulation, You vaucher is send to your wife !!!")

if __name__ == '__main__':

      main()
