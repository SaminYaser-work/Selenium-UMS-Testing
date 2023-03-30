import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--start-maximized')


class SQTTestCases(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.url = 'http://localhost/Moshi/view/home.php'
        super().__init__(methodName)

    def setUp(self):
        self.browser = webdriver.Edge(options=options)

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    # Test cases
    def test_auth_check(self):
        self.browser.get(self.url)
        self.assertIn('Login', self.browser.title)

    def test_login(self):
        self.browser.get(self.url)
        username = self.browser.find_element(By.ID, value='id')
        password = self.browser.find_element(By.ID, value='password')
        login_button = self.browser.find_element(By.ID, value='login-button')
        username.send_keys('28905')
        password.send_keys('1111')
        login_button.click()

        p = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'welcome-msg'))
        )
        self.assertIn('Arab', p.text)

    def test_logout(self):
        self.test_login()
        logout_button = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, 'Sign Out')
        logout_button.click()
        self.assertIn('Login', self.browser.title)

    def test_forgot_password(self):
        self.browser.get(self.url)
        forgot_password = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, 'Forget')
        forgot_password.click()
        input_id = self.browser.find_element(By.ID, value='id')
        input_id.send_keys('28905')
        submit_button = self.browser.find_element(By.ID, 'find-password')
        submit_button.click()
        time.sleep(2)
        p_id = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'found'))
        )

        self.assertIn('1111', p_id.text)

    def test_add_notice(self):
        self.browser.get(self.url)
        self.test_login()
        link = self.browser.find_element(By.LINK_TEXT, "Notices")
        link.click()
        time.sleep(1)
        link = self.browser.find_element(By.NAME, "addNotice")
        link.click()
        time.sleep(1)
        title = self.browser.find_element(By.ID, "title")
        description = self.browser.find_element(By.ID, "description")
        add_button = self.browser.find_element(By.ID, "add-notice")
        title.send_keys("Random NOTICE")
        time.sleep(1)
        description.send_keys(
            "It is to notify all concerned that the University would remain closed on Sunday, March 26, 2023, due to Independence Day 2023.")
        time.sleep(1)
        add_button.click()
        time.sleep(1)
        val = self.browser.find_element(By.ID, "found")
        self.assertIn('Published', val.text)

    def test_update_admin_information(self):
        self.browser.get(self.url)
        self.test_login()
        link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Profile")
        link.click()
        time.sleep(1)
        link = self.browser.find_element(By.NAME, "modify")
        link.click()
        time.sleep(1)
        name_input = self.browser.find_element(By.ID, "name")
        update = self.browser.find_element(By.NAME, "save")
        name_input.clear()
        name_input.send_keys("Arab Khan Arif")
        update.click()
        time.sleep(1)
        name = self.browser.find_element(
            By.XPATH, "//td[contains(text(),'Arab Khan Arif')]")

    def test_upload_file(self):
        self.browser.get(self.url)
        self.test_login()
        link = self.browser.find_element(By.LINK_TEXT, "Forms")
        link.click()
        time.sleep(1)
        file_input = self.browser.find_element(By.NAME, "uploadedFile")
        upload = self.browser.find_element(By.NAME, "upload")
        file_input.send_keys(
            "C:\\Users\\samin\\Documents\\Lecture\\Sem 11\\Software Quality & Testing\\Final\\Lab\\test.txt")
        time.sleep(1)
        upload.click()
        time.sleep(1)
        upload_file = self.browser.find_element(
            By.XPATH, "//td[contains(text(),'test.txt')]")

    def test_search(self):
        self.test_login()
        search_a = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Search'))
        )
        search_a.click()
        search_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'id'))
        )
        search_input.send_keys('9999')
        time.sleep(2)

        try:
            search_res = self.browser.find_element(
                By.XPATH, "//td[contains(text(),'AKS MOSHIUR RAHMAN MAZUMDER')]")
        except Exception as e:
            raise Exception("Search result not found")


if __name__ == '__main__':
    unittest.main(verbosity=1)
