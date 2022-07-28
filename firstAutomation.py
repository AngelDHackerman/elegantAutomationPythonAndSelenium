from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class firstTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.get('https://techstepacademy.com/training-ground')
    # driver.find_element(By.CSS_SELECTOR, '#ipt1')

  def test_one(self):
    driver = self.driver

    write_something = driver.find_element(By.CSS_SELECTOR, '#ipt1')
    write_something.send_keys('Hola como estas???')

    sleep(6)


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)


