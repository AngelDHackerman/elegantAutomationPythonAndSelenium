import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By  # used to select the alerts 


class alets_challenge(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.get('https://techstepacademy.com/training-ground')

      # ? First input field and first 2 buttons with alerts

  def test_first_section(self):
    driver = self.driver

    def button_test(css_selector):  # ! function to test the buttons and apply the "DRY" metodology
      button = driver.find_element(By.CSS_SELECTOR, css_selector).click() 
      alert = driver.switch_to.alert  # move the focus of browser to the alert
      sleep(1)
      alert.accept()  # we accept the alert
      sleep(1)
    

    first_input = driver.find_element(By.CSS_SELECTOR, '#ipt1')
    first_input.send_keys('This is a testing for the input')
    sleep(1)
    first_input.clear()  # we clean the input 
    sleep(1)

    button1 = '#b1'  # this is the css selector 
    button_test(button1)

    button2 = '#b2'
    button_test(button2)

    sleep(1)

      # ? Second section of the web page

    second_input = driver.find_element(By.CSS_SELECTOR, '#ipt2')
    second_input.send_keys('This is a testing for the input')
    sleep(1)
    second_input.clear()  # we clean the input 
    sleep(1)

    button3 = '#b3'
    button_test(button3)

    button4 = '#b4'
    button_test(button4)

    sleep(1)

      # ? Dropdonw section

    def test_dropdonw(self):
      driver = self.driver


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)
