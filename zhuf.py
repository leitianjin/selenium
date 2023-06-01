from tkinter import Image

# 住房截图


import pytesseract as pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
import time
import imgCode

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://js.shaanxi.gov.cn:8086/nwf/main/login.aspx")
driver.maximize_window()
time.sleep(3)
username="中原镇"
passwd="Nwf@147852"
#//*[@id="login-from-box"]/form/div[1]/div/div/input
#//*[@id="login-from-box"]/form/div[2]/div/div/inpu

driver.find_element(By.ID,"C_FName").send_keys(username)
driver.find_element(By.ID,"C_FPwd").send_keys(passwd)

#验证码
# 验证码输入框元素
codeElement = driver.find_element(By.Id, "YZM")
# 验证图片元素
imgElement = driver.find_element(By.XPATH, "//*[@id=\"img1\"]")
imgElement.screenshot("1.png")
code=imgCode.imgCode.getCode("1.png")

'''
# 2、截取屏幕内容，保存到本地
imgElement.screenshot("D:\\dev\\1.png")

# 3、打开截图，获取验证码位置，截取保存验证码
#ran = Image.open("D:\\dev\\1.png")
#box = (0, 60, 30, 60)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
#ran.crop(ran.getbbox()).save("D:\\dev\\11.png")


# 4、获取验证码图片，读取验证码
imageCode = Image.open("D:\\dev\\1.png") # 图像增强，二值化
# imageCode.load()
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("D:\\dev\\111.png")
sharp_img.load()  # 对比度增强
time.sleep(5)

code = pytesseract.image_to_string(sharp_img)
# 5、收到验证码，进行输入验证
code1=pytesseract.image_to_string(Image.open('D:\\dev\\111.png'))
print("codd=",code)
print("code1=",code1)
'''

codeElement.send_keys(code)
time.sleep(20)
checkbox=driver.find_element(By.XPATH, "//*[@id=\"login-from-box\"]/form/label/span[1]/span").is_selected()
login=driver.find_element(By.XPATH, "//*[@id=\"login-from-box\"]/form/div[4]/div/button").click()
print("======================================================================================\n")
print("登录成功")
# 跳转首页 //*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]").click()
print("跳转成功")
#//*[@id="app"]/div/div[4]/div/p
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/p").click()
#点击跳转 收支采集
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div[1]/div[3]/span").click()
driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()

#shouru=(gz,zy,jy,jyzc)
# xpath
#//*[@id="tab-0"]/span

'''
#工资性收入
gz=driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()
#转移性收入
zy=driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()
#经营性收入
jy=driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()
#经营性支出
jyzc=driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div[2]/div[1]/div/ul/div[3]/a/li/span").click()


'''








time.sleep(50)
driver.quit()
