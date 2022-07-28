import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class ninja_challange(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.get('https://techstepacademy.com/trial-of-the-stones')  # page to test and complete it's challange

  def test_challange(self):  # here we'll the code to test the page
    driver = self.driver

    riddle_stone = driver.find_element(By.ID, 'r1Input')  
    riddle_stone.send_keys('rock')  # rock is the answer

    answer_button_stone = driver.find_element(By.ID, 'r1Btn')
    answer_button_stone.click()

    sleep(6)


  def tearDown(self):  # we close the web driver in order to save resources. 
    self.driver.close() 


if __name__ == "__main__":  # entry point once we execute the program on the shell
  unittest.main(verbosity= 2)  # verbosity= 2, stands for the level of details you want at moment to finisht the test. 