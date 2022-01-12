######################################
######################################
##                                  ##
##            /\                    ##
##        _  / |         .'         ##
##       (  /  |  . .-..'  .-.      ##
##        `/.__|_.':   ;  ;   :     ##
##    .:' /    |   `:::'`.`:::'-'   ##
##   (__.'     `-'                  ##
##                                  ##
##              Speaker             ##
##                                  ##
######################################
######################################


import Log
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Communicate:

    def __init__(self, WebDriver):
        self.WebDriver = WebDriver
        self.Log = Log.Generate()

    def WriteMessage(self, msg):

        """[summary]
        """

        try:

            if (type(msg) == str):
                msg = [msg]

            msg_box = WebDriverWait(self.WebDriver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
            msg_box.click()

            for i in msg:
                msg_box.send_keys(i + (Keys.SHIFT + Keys.ENTER))
                sleep(0.5)

            return True

        except Exception as e:
            self.Log.Write("communicator.py | error # " + str(e))
            return False

    def SendMessage(self):

        """[summary]
        """

        try:

            ClassButton_Send = "_4sWnG"

            # button = WebDriverWait(self.WebDriver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, ClassButton_Send)))
            button = WebDriverWait(self.WebDriver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))

            button = self.WebDriver.find_element_by_class_name(ClassButton_Send)
            button.click()

            return True

        except Exception as e:
            print("ERROR SendMessage")
            self.Log.Write("communicator.py | error # " + str(e))
            return False