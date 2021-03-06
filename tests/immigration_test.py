import unittest

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

####
from fixtures.params import CHROME_EXECUTABLE_PATH, DOMAIN


class ContactDetailsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_34_add_immigration_passport(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-21-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 12-32-2020")
        driver.find_element_by_id('btnSave').click()


        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                           'Successfully Saved'))

        self.driver.find_element_by_css_selector('#immigrationCheckAll').click()
        self.driver.find_element_by_id('btnDelete').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_35_add_immigration_visa(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_type_flag_2').click()

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)
        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-24-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 08-11-2020")
        driver.find_element_by_id('btnSave').click()

        sleep(1)

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        sleep(1)

        self.driver.find_element_by_css_selector('#immigrationCheckAll').click()
        self.driver.find_element_by_id('btnDelete').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_36_add_multiple_immigrations(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-21-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 12-32-2020")
        driver.find_element_by_id('btnSave').click()

        sleep(2)
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                           'Successfully Saved'))

        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-21-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 12-32-2020")
        driver.find_element_by_id('btnSave').click()

        sleep(2)
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                           'Successfully Saved'))


    def test_37_delete_immigration(self):

        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-21-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 12-32-2020")
        driver.find_element_by_id('btnSave').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        self.driver.find_element_by_css_selector('#immigrationCheckAll').click()
        self.driver.find_element_by_id('btnDelete').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))


    def test_38_add_attachment_immigration(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/Orange-HRM-Test_Plan.pdf')

        driver.find_element_by_id('btnSaveAttachment').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()

        self.driver.find_element_by_id("btnDeleteAttachment").click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_39_delete_attachment_immigration(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/Orange-HRM-Test_Plan.pdf')

        driver.find_element_by_id('btnSaveAttachment').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()

        self.driver.find_element_by_id("btnDeleteAttachment").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_40_add_attachment_large_size(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/jpg_2mb.jpg')

        driver.find_element_by_id('btnSaveAttachment').click()

        sleep(1)

        crash_message = driver.find_element_by_xpath('/html/body/center[1]/h1').text

        self.assertEqual('413 Request Entity Too Large', crash_message)


if __name__ == '__main__':
    unittest.main()
