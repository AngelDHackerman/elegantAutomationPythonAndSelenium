from importlib.machinery import BYTECODE_SUFFIXES
from operator import truediv
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

      # ? Riddle of Stone

    riddle_stone = driver.find_element(By.ID, 'r1Input')  
    riddle_stone.send_keys('rock')  # rock is the answer

    answer_button_stone = driver.find_element(By.ID, 'r1Btn')
    answer_button_stone.click()

    sleep(1)

    paragraph_to_test = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div/div/div[2]/div/div[1]/h4')
    answer = paragraph_to_test.text  # ? this .text takes the text of the element selected.

      # ? Riddle of Secrets

    riddle_secrets = driver.find_element(By.ID, 'r2Input')
    riddle_secrets.send_keys(answer)

    answer_button_secrets = driver.find_element(By.ID, 'r2Butn')
    answer_button_secrets.click()

    paragraph_to_test = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div/div/div[2]/div/div[1]/h4')

    sleep(1)

      # ? The Two Merchants

    def paragrah_text(xpath):
      text = driver.find_element(By.XPATH, xpath)
      return text.text

    value1 = paragrah_text('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/p')
    value2 = paragrah_text('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/p')
    richest_merchant = ''

    if value1 > value2:
      richest_merchant = paragrah_text('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/span/b')
    else:
      richest_merchant = paragrah_text('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/span/b')

    name_richest = driver.find_element(By.ID, 'r3Input')
    name_richest.send_keys(richest_merchant)

    answer_button_richest = driver.find_element(By.ID, 'r3Butn')
    answer_button_richest.click()

      # check if the answer is correct: 
    passed = paragrah_text('//*[@id="successBanner2"]/h4')
    if passed == 'Success!':
      finish_button = driver.find_element(By.ID, 'checkButn')
      finish_button.click()
    else:
      print('you did wrong')


    sleep(4)



  def tearDown(self):  # we close the web driver in order to save resources. 
    self.driver.close() 


if __name__ == "__main__":  # entry point once we execute the program on the shell
  unittest.main(verbosity= 2)  # verbosity= 2, stands for the level of details you want at moment to finisht the test. 