from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Posh:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://poshmark.com/login")
        time.sleep(2)
        email = bot.find_element_by_name("login_form[username_email]")
        password = bot.find_element_by_name("login_form[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def auto_offer(self,link1):
        bot = self.bot
        bot.get(link1)
        try:

            bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div/button").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/button").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/i").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[1]").click()  # 10%off
            #bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[2]").click() #20$off
            #bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[3]").click()  # 30$off
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/button[2]").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/div[1]/div/div[1]").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/ul/li[1]/div").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/button[2]").click()
            time.sleep(1)

            """
            bot.find_element_by_xpath("/html/body/main/div/div[1]/div[2]/div[3]/form/div[2]/div[1]/div[3]/a").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div/div[5]/div[2]/div/div[2]/a/span").click()
            time.sleep(1)
            bot.find_element_by_id("offer_to_likers_calculator").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[1]/div[7]/div[2]/div[2]/div[4]").click()  #10%OFF
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[1]/div[7]/div[3]/button[2]").click()
            time.sleep(1)
            bot.find_element_by_id("shipping-discount-selection").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[2]/form/div[3]/div[2]/div/div/div[3]/div/div[2]/div[1]/div").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[2]/form/div[4]/button[2]").click()
            time.sleep(1)
            """
        except Exception as ex:
            time.sleep(5)


ed = Posh("", "") #id #passowrd
ed.login()
ed.auto_offer("")  # product link 
ed.auto_offer("")
