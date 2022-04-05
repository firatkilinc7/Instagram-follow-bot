from selenium import webdriver
from selenium.webdriver.common.by import By
import linecache, time

print("*--**--**--* |-HekiR-| *--**--**--*")
print("V0.1")
targetAcc = input("Target Account:")
total_follow = int(input("How much you want to follow: "))
targetLink = "https://www.instagram.com/" + targetAcc
for i in range(1, total_follow + 1):    
    try:    
        engine = webdriver.Chrome()
        accNonProcess = linecache.getline('./acc.txt', i)
        acctest = accNonProcess.split(':')
        username = acctest[0]
        password = acctest[1]
        engine.get("https://www.instagram.com/")
        time.sleep(1)
        engine.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)#send username
        engine.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)#send pass
        time.sleep(4)
        engine.get(targetLink)
        time.sleep(1)
        engine.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF").click()
        time.sleep(4)
        engine.close()
    except:
        print("Error, trying next account")
        engine.close()
