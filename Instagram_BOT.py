##Instagram BOT To login by itself and like the first post of your feed


##import Libaries
from selenium import webdriver 
from time import sleep
from pynput.keyboard import Key, Controller


#create Instagram Class
class Instagram:
    def __init__(self,username,password): #constructor
        self.username=username
        self.password=password
        self.driver= webdriver.Chrome("C:/Users/dell/Downloads/chromedriver.exe")

     #for login   
    def login(self):
        driver=self.driver
        driver.get('https://www.instagram.com')
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.username)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        login=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        sleep(1)
        login.click()

    #Get out of some pop up
    def getout_of_extra_css(self):
        driver=self.driver
        sleep(4)
        save_Now_Click=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        save_Now_Click.click()
        sleep(1)
        Turn_on_Notification=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
        Turn_on_Notification.click()

    #like 1st pic of your instagram feed
    def like_the_first_post(self):
        driver=self.driver
        sleep(1)
        like_post=driver.find_element_by_class_name("fr66n")
        like_post.click()
        
         
insta=Instagram('put your email','put your instagram password') #create object
insta.login()
insta.getout_of_extra_css()
insta.like_the_first_post()

## to remove the allow and block css 
keyboard = Controller()
keyboard.press(Key.esc)



