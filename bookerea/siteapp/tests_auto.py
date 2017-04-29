from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from django.test import TestCase
import unittest
#
#
# driver = webdriver.Firefox()
#
# class login(TestCase):
#     def setUp(self):
#         driver.get("http://localhost:8000/login/")
#
#     @unittest.skip("not now")
#     def test_title(self):
#         self.assertEqual(driver.title,"DuckDuckGo")
#
#     @unittest.skip("not now")
#     def test_secure(self):
#         self.assertIn("https://",driver.current_url)
#
#     @unittest.skip("not now")
#     def test_search_input(self):
#         sInp = driver.find_element_by_id("search_form_input_homepage")
#         self.assertEqual(sInp.get_attribute("value"),'')
#         self.assertFalse(bool(sInp.get_attribute("value")))
#
#     @unittest.skip("not now")
#     def test_twitter_link(self):
#         tBtn = driver.find_element_by_css_selector('a.js-side-menu-twitter')
#         self.assertEqual(tBtn.get_attribute('href'),'https://twitter.com/duckduckgo')
#
#     @unittest.skip("not now")
#     def test_search_keyword(self):
#         keywords = ["Spain","Austuralia","Germany","Somalia"]
#         for k in keywords:
#             with self.subTest(i=k):
#                 driver.get("http://www.duckduckgo.com")
#                 sInp = driver.find_element_by_id("search_form_input_homepage")
#                 sInp.send_keys(k)
#                 sInp.send_keys(Keys.RETURN)
#                 self.assertIn("q={}".format(k),driver.current_url)
#
#
#     def login(self):
#         uInp = driver.find_element_by_id("id_username")
#         pInp = driver.find_element_by_id("id_password")
#         sBtn = driver.find_element_by_id("submit")
#         actions = ActionChains(driver)
#         actions.move_to_element(uInp)
#         actions.send_keys("lina")\
#         .move_to_element(pInp)\
#         .send_keys('1qa2ws3ed')\
#         .click_and_hold(sBtn)
#         actions.perform()
#         self.assertIs( driver.current_url,"https://localhost:8000/book")
#
#
#     @unittest.skip("not now")
#     def test_search_results(self):
#         sInp = driver.find_element_by_id("search_form_input_homepage")
#         sInp.send_keys("Spain")
#         sInp.send_keys(Keys.RETURN)
#         wait = WebDriverWait(driver,10)
#         results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'result__a')))
#         # results = driver.find_elements_by_class_name("result__a")
#         self.assertEqual(len(results),30)
#     @classmethod
#     def tearDownClass(cls):
#         driver.quit()
#         # driver.close()
#
# unittest.main()