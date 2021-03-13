from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options() 
#opt.add_argument("--headless") //this one for not open browser
#opt.add_argument('--disable-popup-blocking')
opt.binary_location = r'C:\Users\chrome.exe' #path to chrome.exe
path = 'C:/Users/chromedriver.exe' #path to chromedriver.exe
driver = webdriver.Chrome(executable_path= path, options = opt)
driver.get("https://www.nhaccuatui.com/")
print(driver.title)
#wait = WebDriverWait(driver, 30)
#Hover
action = ActionChains(driver)
avatar_button = driver.find_element_by_css_selector('img.avata.new_header')
#avatar_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="showBoxUserProfile"]/div/div/img')))
login_btn = driver.find_element_by_xpath('//*[@id="btnUserUpload"]')
hover_avatar = action.move_to_element(avatar_button).click(login_btn).perform()

#login_btn = driver.find_element_by_xpath('//*[@id="btnUserUpload"]')


username = driver.find_element_by_xpath('//*[@id="uname"]')
username.send_keys('') 
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('')
driver.find_element_by_css_selector('#rememberpass').click() #uncheck remember password
driver.find_element_by_id('_frmLogin').submit() #login
print('done')
