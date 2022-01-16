from selenium import webdriver
import time, os
os.chdir(r"Q:\Learning\Python\stunning-tech")
# print(os.getcwd())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# userinput = input("What to search: ")
# browser = webdriver.Chrome(
#     executable_path="Q:\Learning\Python\stunning-tech\chrome_driver\chromedriver.exe")
# browser.get("https://www.google.com")
# time.sleep(2)
# search_input = browser.find_element_by_name("q")
# search_input.send_keys(str(userinput))
# time.sleep(2)
# search_btn = browser.find_element_by_css_selector('input[type="submit"]')
# search_btn.click()

# #google text input field
# """
# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" 
# name="q" type="text" aria-autocomplete="both" aria-haspopup="false" 
# autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" 
# role="combobox" spellcheck="false" title="Tafuta" value="" 
# aria-label="Tafuta" data-ved="0ahUKEwjGwtravpr1AhVGKBoKHXyPBGYQ39UDCAQ">
# """

# #google search button
# """
# <input class="gNO89b" value="Google Search" aria-label="Google Search" 
# name="btnK" type="submit" data-ved="0ahUKEwjjhrv9v5r1AhXiyIUKHdhOCQUQ4dUDCAs">
# """

# browser = webdriver.Chrome(
#     executable_path=r"Q:\Learning\Python\stunning-tech\chrome_driver\chromedriver.exe")
# # browser.maximize_window()
# browser.get("https://web.whatsapp.com/")
executable_path=r"Q:\Learning\Python\stunning-tech\chrome_driver\chromedriver.exe"
os.opendir(executable_path)
with open("groups.txt", "r", encoding="utf8") as f:
    groups = [group.strip() for group in f.readlines()]

with open("message.txt", "r",encoding="utf8") as f:
    msg = f.read()
# time.sleep(30)

# for group in groups:
#     # pass
#     print("should wait for 500secs")
#     search_xpath = "//div[@contenteditable='true'][@data-tab='3']"
#     # '//*[@id="side"]/div[1]/div/label/div/div[2]'
#     try:
#         search_box = WebDriverWait(browser,500).until(
#             EC.presence_of_element_located((By.XPATH, search_xpath))
#         )
#         print("search box loaded and wait complete")
#         search_box.send_keys(group)
#         print("should search for the first group")
#     except Exception as error:
#         print("Issue: ",error)
        

