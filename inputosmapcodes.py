import selenium
from selenium import webdriver
import time

#os maps login details
username = "email@address.com"
password = "PassWOrD"

# text file with no containing raw codes and no blank lines sed -i '/^$/d' /path/to/file is useful
path_to_codes = "path/to/codes.txt"

#somewhere to store the codes
codes = []
#open file with codes in 
with open(path_to_codes) as f:
    code_lines = f.read().splitlines()

#clean codes of map names and hyphens
for code in code_lines:
    temp_code = code.split(" ")
    codes += [tuple(temp_code[2].split("-"))]

# Using firefox to access web
driver = webdriver.Firefox()

driver.get('https://www.ordnancesurvey.co.uk/shop/customer/account/login/')

# Select the username box
id_box = driver.find_element_by_name('login[username]')
# Send username information
id_box.send_keys(username)

# Find password box
pass_box = driver.find_element_by_name('login[password]')
# Send password
pass_box.send_keys(password)
# Find login button
login_button = driver.find_element_by_name('send')
# Click login
login_button.click()

#wait for website to do its stuff
time.sleep(8)

#redeem a code
driver.get('https://shop.ordnancesurvey.co.uk/redeem.html/')

for code in codes[5:]:#skip the first 5 because I've entered these by hand

    #enter the code in the box
    for num in range(3):
        box = driver.find_element_by_name('vouchercode['+str(num)+']')
        box.send_keys(code[num])

    redeem_code = driver.find_element_by_name('send')
    redeem_code.click()
    time.sleep(8)
    driver.get('https://shop.ordnancesurvey.co.uk/redeem.html/')