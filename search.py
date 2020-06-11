import zomato_login
from time import sleep


class Search(zomato_login.ZomatoLogin):
    def __init__(self, item, email_id, pw):
        all_items = {}
        self.item = item
        super().__init__(email_id, pw)
        self.driver.find_element_by_id('keywords_input').send_keys(item)
        self.driver.find_element_by_id('search_button').click()
        all_items[self.driver.find_element_by_xpath('/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/'
                                                    'div[1]/section/div[1]/div[3]/div[1]/div[1]/'
                                                    'div/article/div[1]/'
                                                    'div/div[2]/div[1]/div[1]/a[1]')] = 
