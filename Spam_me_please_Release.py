from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
print('Мне нужны твои данные для того чтобы залогиниться в ВК')
login = input('Логин')
password = input('Пароль')
print('Как называется беседа в которую влетаем?')
print('ВАЖНО: нужно чтобы эту беседу было видно после нажатия на Мессенджер в вк')
chat_name = input()
URL = "https://vk.com/feed"
print('Как много пользователей в беседе?')
members = input('Введи сюда')
print('Есть 2 способа: Первый(1) - в отдельном сообщении упоминается каждый человек')
print('Второй(2) - все упоминания находятся в одном сообщении. Выбери что тебе нужно')
print('Имей ввиду - за первый(1) способ вк скорее всего будет бить тебя капчей')
print('Пока что это будет все ломать')
spam_type = input('1 или 2')
print('Ну что, мы стартуем')
driver = webdriver.Chrome()
action = webdriver.ActionChains(driver)
driver.maximize_window()
driver.get(URL)
time.sleep(2)
driver.find_element_by_id("email").send_keys(login)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("login_button").click()
try:
    time.sleep(3)
    driver.find_element_by_xpath('//a[@href = "/im"]').click()
    time.sleep(2)
except NoSuchElementException:
    print('Придется пройти капчу')
    logicbar = input('Введи сюда Y - если введ и перешло на твою страницу')
    if logicbar == 'Y' or logicbar == 'y':
        time.sleep(3)
        driver.find_element_by_xpath('//a[@href = "/im"]').click()
        time.sleep(2)
href = '//*[contains(text(), ' + "'" + chat_name + "')]"
chat = driver.find_element_by_xpath(href)
action = ActionChains(driver)
action.move_to_element(chat).click().perform()
time.sleep(1)
if spam_type == '2':
    driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
    for i in range(1, int(members), 1):
        cool_string ='//div[@class = "wddi"]' +'[' + str(i) + "]"
        time.sleep(0.2)
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys('@')
        time.sleep(0.5)
        driver.find_element_by_xpath(cool_string).click()
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys(Keys.SHIFT + Keys.ENTER)
        time.sleep(0.1)
    driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
    driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys(Keys.ENTER)

if spam_type == '1':
    driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
    for i in range(1, int(members), 1):
        cool_string ='//div[@class = "wddi"]' +'[' + str(i) + "]"
        time.sleep(0.5)
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys('@')
        time.sleep(1)
        driver.find_element_by_xpath(cool_string).click()
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
        driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys(Keys.ENTER)
        time.sleep(0.5)

driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys('Простите <3'+Keys.ENTER)
driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').click()
driver.find_element_by_xpath('//div[@class = "im_editable im-chat-input--text _im_text"]').send_keys('https://github.com/Molozey'+Keys.ENTER)


key = input('CLOSE Y/N')
if key == 'Y' or key == 'y':
    driver.close()
else:
    print('OK BOOMER')
