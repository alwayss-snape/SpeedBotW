from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#constants
PROMISED_DOWN = 100
PROMISED_UP = 20
CHROME_DRIVER_PATH = "/Users/kshitijchaubey/Desktop/PythonProjects/TwitterBot/chromedriver"
TWITTER_EMAIL = "michaelis2509@gmail.com"
TWITTER_PASSWORD = "TaggyMichael@30"
Phone_number = "9365844564"

class InternetSpeedTwitterBot:
    
    def __init__(self, driver_path):
        """creates a selenium driver and 2 properties namely up and down for up&down
    internet speeds"""
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Gets internet speed of your internet provider from speedtest.com"""
        
        self.driver.get("https://www.speedtest.net/")
       
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        """Logs in to the twitter account, creates a tweet with info:
        up and down internet speed and tweets it"""
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
        next_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]'
        password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        next2_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
        login_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]'
        
        time.sleep(1)
        self.driver.find_element_by_xpath(email_xpath).send_keys(TWITTER_EMAIL)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(next_xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(phone_xpath).send_keys(Phone_number)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(next2_xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(password_xpath).send_keys(TWITTER_PASSWORD)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(login_xpath).click()
        
       
        tweet = f"Hey fella, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        
        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        post_tweet_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
        time.sleep(5)

        self.driver.find_element_by_xpath(tweet_xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(message_xpath).send_keys(tweet)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(post_tweet_xpath).click()
        time.sleep(2)

        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


#created with passion and love for automation by Kshitij Chaubey
