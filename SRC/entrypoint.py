########################################################
########################################################
##                                                    ##
##                                                    ##
## I8,        8        ,8I  88888888ba   88888888ba   ##
## `8b       d8b       d8'  88      "8b  88      "8b  ##
##  "8,     ,8"8,     ,8"   88      ,8P  88      ,8P  ##
##   Y8     8P Y8     8P    88aaaaaa8P'  88aaaaaa8P'  ##
##   `8b   d8' `8b   d8'    88""""""8b,  88""""""8b,  ##
##    `8a a8'   `8a a8'     88      `8b  88      `8b  ##
##     `8a8'     `8a8'      88      a8P  88      a8P  ##
##      `8'       `8'       88888888P"   88888888P"   ##
##                                                    ##
##                 Whatsapp Browser Bot               ##
##                                                    ##
########################################################
########################################################

########################################################
#                    DEBUGGER = True                   #
########################################################
import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=9999, stdoutToServer=True, stderrToServer=True)
########################################################
#                    DEBUGGER = True                   #
########################################################


import Bot
import Log
import Config
from os import getcwd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def InitWebDriver():

    """[summary]

    Returns:
        [type]: [description]
    """
    
    URL = 'https://web.whatsapp.com/'
    
    PathSession = getcwd() + '/Data/Session/'
    
    _Chrome_options = Options()
    _Chrome_options.add_argument('--user-data-dir='+PathSession)
    _Chrome_options.add_argument('--disable-extensions')
    _Chrome_options.add_argument('--disable-dev-shm-usage')
    _Chrome_options.add_argument('--no-sandbox')
    
    # Iniciar sin mostrar la ventana del navegador
    # _Chrome_options.add_argument('headless')
     
    try:
        WebDriver = Chrome(options = _Chrome_options)   

        WebDriver.maximize_window()
        WebDriver.get(URL)
        
        return WebDriver
    except Exception as error:
        Log.Write("entrypoint.py # " + error)
        WebDriver.quit()

if(__name__ == '__main__'):
    
    Log = Log.Generate()
    
    try:

        # Initialize WebDriver connection
        WebDriver = InitWebDriver()

        # Initialize Bot and pass WebDriver to get access to the browser
        Bot = Bot.Bot(WebDriver)
        # Initialize Config and pass WebDriver to get access to the browser
        Config = Config.Config(WebDriver)


        # Start Configurator
        if(Config.Initialize()):
            # Start Bot
            Bot.ReadMessage(WebDriver)
        else:
            print(Config.GetError()) # Get the error to debug
            # if Configurator is not initialized and occurs an error save the error in the log
            Log.Write("Config # " + str(Config.GetError()))

        print("exist error ")
        # is ended the program, close the WebDriver
        WebDriver.quit()

    # if occurs an error save the error in the log
    except UnboundLocalError as error:
        Log.Write("entrypoint.py | UnboundLocalError # "+ str(error))
    except TypeError as error:
        Log.Write("entrypoint.py | TypeError # "+ str(error))
    except KeyboardInterrupt:
        # if the user press Ctrl+C, close the WebDriver
        WebDriver.quit()