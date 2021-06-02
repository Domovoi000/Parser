import time
from base64_convert import base64_convert

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_screen_shot(url):
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    print(driver.get(url))
    time.sleep(2)

    element = driver.find_element_by_xpath("//body")
    width = 1920
    height = element.size['height'] + 1000
    driver.set_window_size(width, height)
    time.sleep(2)
    driver.save_screenshot('my_screenshot.png')
    driver.quit()

    image = open('my_screenshot.png', 'rb')
    image_read = image.read()
    image_convert = base64_convert(image_read)
    return image_convert
