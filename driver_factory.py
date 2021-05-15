from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def set_options(): 
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                      "profile.default_content_setting_values.media_stream_camera": 1,
                                      "profile.default_content_setting_values.notifications": 1
                                      })
    return options


def get_driver():
    return webdriver.Chrome(ChromeDriverManager().install() , options = set_options())



