import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

  # this is the new standar in order to get the URL's address 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# * We can keep the windows open with the 4 lines below ;)
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
    driver1.get('http://yahoo.com')
    driver2.get('http://google.com')

  def test_windows(self):
    driver1 = self.driver1  # this manipulate the first window
    driver2 = self.driver2  # this manipulate the second window
    sleep(5)

      # ? Opening tabs in the browser 
    driver1.execute_script('window.open("http://google.com","_blank");')
    driver2.execute_script('window.open("http://platzi.com","_blank");')
    sleep(5)

if __name__ == "__main__":
  unittest.main(verbosity= 2)