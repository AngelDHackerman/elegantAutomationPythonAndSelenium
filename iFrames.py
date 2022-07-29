from lib2to3.pgen2 import driver
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