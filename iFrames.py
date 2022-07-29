import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

  # this is the new standar in order to setup the web driver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class iFrames(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = self.driver
    driver.get('https://techstepacademy.com/iframe-training')

  def test_iFrame(self):
    driver = self.driver

    iframe_section = driver.find_element(By.CSS_SELECTOR, '#block-yui_3_17_2_1_1564338258424_5429 > div > iframe')
    driver.switch_to.frame(iframe_section)  # ! this is how we switch into an iFrame

    input_iFrame = driver.find_element(By.XPATH, '//*[@id="ipt1"]')
    input_iFrame.send_keys('This is a test')
    sleep(3)

    driver.switch_to.default_content()  # ! this is how we switch back into the main page

    news_button = driver.find_element(By.XPATH, '//*[@id="topNav"]/nav/ul/li[3]/a')
    news_button.click()
    sleep(3)


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)




