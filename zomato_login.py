from selenium import webdriver
from time import sleep


class ZomatoLogin:
    def __init__(self, email_id, pw):
        self.email_id = email_id
        self.pw = pw
        self.driver = webdriver.Chrome('C:\\Users\\Dheeraj\\Downloads\\chromedriver.exe')
        self.driver.get('https://www.zomato.com/bangalore')
        self.main_page = self.driver.current_window_handle
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/a[1]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[13]/div/div[2]/div/div[2]/div[1]/div[2]/a').click()
        sleep(3)

        login_page = None
        for handle in self.driver.window_handles:
            if handle != self.main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/'
                                     'div/form/span/section/div/div/div[1]/'
                                     'div/div[1]/div/div[1]/input').send_keys(self.email_id)

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/'
                                      'div/div/div[2]/div/div[2]/div/div[1]/div/span').click()

        sleep(2)
        self.driver.find_element_by_name('password').send_keys(self.pw)

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]'
                                      '/div/div[1]/div/span').click()
        self.driver.switch_to.window(self.main_page)
        sleep(7)

