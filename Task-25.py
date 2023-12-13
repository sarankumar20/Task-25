# using python selenium , Explicit Wait, Expected conditions and chrome webdriver kindly do the following task mentioned below:
# go to https://www.imdb.com/search/name/
# fill the data given in the input boxes, select boxes and drop down menu on the webpage and do a search
# do not use sleep() method over the task
from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

class Imdb:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.action = ActionChains(self.driver)
        # navigate browser to given url
        self.driver.get("https://www.imdb.com/search/name/")
        # webdriverWait class is used to implement explicit wait
        self.wait = WebDriverWait(self.driver, 10)
        
    def Advance_name_search(self):
        try:
            # locate sign_alert_box
            sign_popup = self.driver.find_element(by=By.XPATH, value='//div[contains(@class,"ipc-list-card")]')
            # if sign alert box is visible and do the operation
            if sign_popup.is_displayed():
                close_butt = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="imdbHeader"]/div[2]/div[5]/div/div/div/div/div[1]/button'))).click()
            else:
                print("nothing")
            # try to locate name_dropdown_field using id locator
            # here we using expected condition to wait until the element to be click
            name_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'nameTextAccordion'))).click()
            # try to locate input_name_field using id locator
            # here we using expected condition to wait until the element is present
            name_input_box = self.wait.until(ec.presence_of_element_located((By.NAME, 'name-text-input'))).send_keys("kamal")
            # try to locate Birthdaydate_dropdown_field using id locator
            # here we using expected condition to wait until the element to be click
            birthdayDate_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'birthDateAccordion'))).click()
            date_from = self.wait.until(ec.presence_of_element_located((By.NAME, 'birth-date-start-input'))).send_keys('07-12-2023')
            date_to = self.wait.until(ec.presence_of_element_located((By.NAME, 'birth-date-end-input'))).send_keys('07-12-2023')
            # try to locate Birthday_dropdown_field using id locator
            # here we using expected condition to wait until the element is present
            Birthday_field_open = self.wait.until(ec.element_to_be_clickable((By.ID, 'birthdayAccordion'))).click()
            inputField_birthday = self.wait.until(ec.presence_of_element_located((By.NAME, 'birthday-input'))).send_keys('07-12')
            # try to locate Awards_dropdown_field using id locator
            # here we using expected condition to wait until the element to be click
            Awards_open= self.wait.until(ec.element_to_be_clickable((By.ID, 'awardsAccordion'))).click()
            # locate the best_actor_win button using xpath and click it
            best_actor_win = self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Best Actor-Winning"]')))
            # here to click best_actor_win button using actionChains class to click element
            self.action.move_to_element(best_actor_win).click().perform()
            # try to locate Page_topic_dropdown_field using id locator
            page_topic = self.wait.until(ec.element_to_be_clickable((By.ID, 'pageTopicsAccordion'))).click()
            place_birth = self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Place of birth"]')))
            # here to click place_birth button using actionChains class to click element
            self.action.move_to_element(place_birth).click().perform()
            page_topic_dd= self.wait.until(ec.presence_of_element_located((By.ID, 'within-topic-dropdown-id')))
            # using Select class with select_by_value is used to identify that element
            select=Select(page_topic_dd)
            select.select_by_value('BIRTH_PLACE')
            # another input_text_field we use Name locator to identify that element
            page_text=self.wait.until(ec.presence_of_element_located((By.NAME, 'within-topic-input'))).send_keys("coimbatore")
            # try to locate death_dropdown_field using id locator and clickit
            death_date = self.wait.until(ec.element_to_be_clickable((By.ID, 'deathDateAccordion'))).click()
            death_from = self.wait.until(ec.presence_of_element_located((By.NAME, 'death-date-start-input'))).send_keys('30-10-1966')
            death_to = self.wait.until(ec.presence_of_element_located((By.NAME, 'death-date-end-input'))).send_keys('26-04-2021')
            # try to locate gender_identity_dropdown_field using id locator and clickit
            gender = self.wait.until(ec.element_to_be_clickable((By.ID, 'genderIdentityAccordion'))).click()
            male =self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Male"]')))
            # after dropdown_opens i want click male_button so actionChains are used to hover to male button
            self.action.move_to_element(male).click().perform()
            # try to locate death_dropdown_field using id locator and clickit
            credit = self.wait.until(ec.element_to_be_clickable((By.ID, 'filmographyAccordion'))).click()
            text_credit = self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input'))).send_keys("nill")
            # try to locate nickName_dropdown_field using id locator and clickit
            nick_name = self.wait.until(ec.element_to_be_clickable((By.ID, 'adultNamesAccordion'))).click()
            # here we have radiobutton and if it is already clicked we want use coditional Staments to finish the process
            radio_butt = self.wait.until(ec.element_to_be_clickable((By.ID, 'include-adult-names')))
            if radio_butt.is_selected():
                pass
            else:
                radio_butt.click()
            # to locate see_results button using xpath
            see_result = self.wait.until(ec.presence_of_element_located((By.XPATH, '//button/span[@class="ipc-btn__text"]')))
            # here hover mouse pointer to see_results_button and click it
            # we're using actions_chains method
            self.action.move_to_element(see_result).click().perform()

        except ElementClickInterceptedException as error1:
            print(error1)
        except ElementNotInteractableException as error2:
            print(error2)

source = Imdb()
source.Advance_name_search()