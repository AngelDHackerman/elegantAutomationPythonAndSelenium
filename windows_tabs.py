from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # * this make the broser wait (this is to wait the page API)
from selenium.webdriver.support import expected_conditions as EC 

  # this is the new standar in order to setup the web driver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#  We can keep the windows open with the 4 lines below ;)
# driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # this brings the web driver to us
# driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # this brings the web driver to us
# driver1.get('http://yahoo.com')
# driver2.get('http://google.com')


class windows_tabs(unittest.TestCase):

  def setUp(self):
    self.driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # this brings the web driver to us
    self.driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # this brings the web driver to us
    driver1 = self.driver1
    driver2 = self.driver2

    driver1.implicitly_wait(5)
    driver2.implicitly_wait(5)

    driver1.get('http://yahoo.com')
    driver2.get('http://google.com')

      # ? Opening the windows

  def test_windows(self):
    driver1 = self.driver1  # this manipulate the first window
    driver2 = self.driver2  # this manipulate the second window
    sleep(3)

      # ? Opening tabs in the browser 

    driver1.execute_script('window.open("http://google.com","_blank");')
    sleep(10)
    driver1.execute_script('window.open("http://amazon.com","_blank");')
    sleep(10)

    driver2.execute_script('window.open("http://platzi.com","_blank");')
    sleep(2)

      # ? Switiching between tabs 
      # ! I found no way to know which is the order of each tab 

    parent = driver1.window_handles[0]  # select to the first tab
    older = driver1.window_handles[2]  # select to the 5th tab

    driver1.switch_to.window(parent)
    sleep(3)
    driver1.switch_to.window(older)
    sleep(3)


if __name__ == "__main__":
  unittest.main(verbosity= 2)