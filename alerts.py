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

  def test_alerts(self):
    driver = self.driver


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)
