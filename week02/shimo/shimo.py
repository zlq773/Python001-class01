from selenium import webdriver


def get_info():
    try:
        global browser
        browser = webdriver.Chrome()
        browser.get("https://shimo.im/welcome")
        browser.implicitly_wait(10)
        btn1 = browser.find_element_by_xpath("//div[@class='entries']//button[@class='login-button btn_hover_style_8']")
        btn1.click()
        browser.find_element_by_xpath("//input[@name ='mobileOrEmail']").send_keys("330173099@qq.com")
        browser.find_element_by_xpath("//input[@name ='password']").send_keys("hyzj127833")
        browser.find_element_by_xpath("//button[@type ='black']").click()





    except Exception as e:
        print(e)

def main():
    get_info()



if __name__ == '__main__':
    main()