from select import select
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  # * used to select the alerts 
from selenium.webdriver.support.ui import Select  # * used to select the dropdonw menus

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class alets_challenge(unittest.TestCase):

  def setUp(self):
    # self.driver = webdriver.Chrome(executable_path= './chromedriver')
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = self.driver
    driver.get('https://techstepacademy.com/training-ground')

      # ? First input field and first 2 buttons with alerts

  def test_first_section(self):
    driver = self.driver

    def button_check(css_selector):  # ! function to test the buttons and apply the "DRY" metodology
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
    button_check(button1)

    button2 = '#b2'
    button_check(button2)

    sleep(1)

      # ? Second section of the web page

    second_input = driver.find_element(By.CSS_SELECTOR, '#ipt2')
    second_input.send_keys('This is a testing for the input')
    sleep(1)
    second_input.clear()  # we clean the input 
    sleep(1)

    button3 = '#b3'
    button_check(button3)

    button4 = '#b4'
    button_check(button4)

    sleep(1)

    # ? Dropdonw section

    select = Select(driver.find_element(By.ID, 'sel1'))  # selected the dropdown menu
    select.select_by_value('first')
    sleep(1)
    select.select_by_value('second')
    sleep(1)
    select.select_by_value('third')
    sleep(1)



if __name__ == "__main__":
  unittest.main(verbosity= 2)
