from lib2to3.pgen2 import driver
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
    
    first_input = driver.find_element(By.CSS_SELECTOR, '#ipt1')
    first_input.send_keys('This is a testing for the input')
    sleep(1)
    first_input.clear()  # we clean the input 
    sleep(1)

    button1 = driver.find_element(By.CSS_SELECTOR, '#b1').click()
    alert = driver.switch_to.alert  # move the focus of browser to the alert
    sleep(1)
    alert.accept()  # we accept the alert
    sleep(1)

    button2 = driver.find_element(By.CSS_SELECTOR, '#b2').click()
    alert = driver.switch_to.alert  # move the focus of browser to the alert
    sleep(1)
    alert.accept()  # we accept the alert
    sleep(1)

    sleep(2)


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)
