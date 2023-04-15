# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep


class MessengerBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://messenger.com')

        sleep(2)

        #fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        #fb_btn.click()

        # switch to login popup
        #base_window = self.driver.window_handles[0]
        #self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('vic969696@gmail.com')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('Victor8-')

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
    def ecrire(self):    
        sleep(2)
        
        zone_txt = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div')
        zone_txt.send_keys('Je viens de t\'écrire ce message avec un bot python !'+'\r')
        
        
        envoyer = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a')
        envoyer.click()
    
    #     self.driver.switch_to_window(base_window)

    #     popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_1.click()

    #     popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_2.click()



    # def dislike(self):
    #     dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
    #     dislike_btn.click()

    # def auto_swipe(self):
    #     while True:
    #         sleep(0.5)
    #         try:
    #             self.like()
    #         except Exception:
    #             try:
    #                 self.close_popup()
    #             except Exception:
    #                 self.close_match()

    # def close_popup(self):
    #     popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    #     popup_3.click()

    # def close_match(self):
    #     match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #     match_popup.click()

bot = MessengerBot()
bot.login()
#bot.ecrire()


 