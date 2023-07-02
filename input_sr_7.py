from selenium import webdriver
from PIL import Image, ImageEnhance
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import imgCode





driver=webdriver.Chrome()
driver.get("https://www.akxczx.com:8100/login?redirect=%2F")
driver.maximize_window()
driver.implicitly_wait(5)
driver.set_page_load_timeout(5)
time.sleep(3)
username="13891595667"
passwd="xczx@2023"

# 用户名、密码 、验证码
in_usernaem=driver.find_element(By.XPATH,"//*[@id=\"login-from-box\"]/form/div[1]/div/div/input")
in_password=driver.find_element(By.XPATH,"//*[@id=\"login-from-box\"]/form/div[2]/div/div/input")
in_imgcode=driver.find_element(By.XPATH,"//*[@id=\"login-from-box\"]/form/div[3]/div/div[1]/input")

# 验证码截图识别
codeimg=driver.find_element(By.CLASS_NAME,"login-code-img")
save_img=codeimg.screenshot("7.1.png")

#登录
in_usernaem.send_keys(username)
in_password.send_keys(passwd)
in_imgcode.send_keys(imgCode.imgCode.getCode("7.1.png"))
driver.find_element(By.XPATH,"//*[@id=\"login-from-box\"]/form/div[4]/div/button").click()


time.sleep(5)

# 1
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div[1]/div[3]/span").click()

time.sleep(3)
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()


time.sleep(3)

#2
in_idcode=driver.find_element(By.XPATH,"//*[@id=\"income-report\"]/form/div[3]/div/div/input")
seach_clk=driver.find_element(By.XPATH,"//*[@id=\"income-report\"]/form/div[5]/div/button[1]/span")
caiji_cil=driver.find_element(By.XPATH,"//*[@id=\"income-report\"]/div[2]/div[3]/table/tbody/tr/td[6]/div/button")


in_idcode.send_keys("612401197809139556")
#time.sleep(10)
seach_clk.click()
#income-report > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--medium > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(2) > td.el-table_1_column_6.is-center.small-padding.fixed-width.el-table__cell > div > button > span

caiji_cil.click()


#
put_gz=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[2]/div/div/input")
put_jy=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[3]/div/div[1]/input")
put_zy=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[4]/div/div/input")
put_cc=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[5]/div/div/input")
put_zc=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[6]/div/div/input")
submit_clk=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/span/button[2]")



put_gz.send_keys("0")
put_jy.send_keys("0")
put_zy.send_keys("0")
put_cc.send_keys("0")
put_zc.send_keys("0")
time.sleep(5)
submit_clk.click()


#2in

in_idcode.clear()
in_idcode.send_keys("61240119580418955571")
#time.sleep(3)
seach_clk.click()


caiji_cil.click()


#
put_gz=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[2]/div/div/input")
put_jy=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[3]/div/div[1]/input")
put_zy=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[4]/div/div/input")
put_cc=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[5]/div/div/input")
put_zc=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/form/div/div[6]/div/div/input")
submit_clk=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/span/button[2]")



put_gz.send_keys("0")
put_jy.send_keys("0")
put_zy.send_keys("0")
put_cc.send_keys("0")
put_zc.send_keys("0")
time.sleep(3)
submit_clk.click()





time.sleep(15)
driver.quit()