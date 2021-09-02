import csv
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_testcase(driver, test_name):
    # title
    driver.find_element_by_id("DOM_307").send_keys(test_name)

    # level
    try:
        driver.find_element_by_id("DOM_339").click()
    except WebDriverException:
        driver.find_element_by_id("DOM_232").click()

    driver.implicitly_wait(6)
    driver.find_element_by_xpath(".//td[contains(text(), 'Component')]").click()

    # component
    try:
        driver.find_element_by_id("DOM_348").click()
    except WebDriverException:
        driver.find_element_by_id("DOM_241").click()

    driver.implicitly_wait(6)
    driver.find_element_by_xpath(".//td[contains(@title, 'V2V')]").click()

    # importance
    driver.find_element_by_id("DOM_428").click()
    driver.implicitly_wait(6)
    driver.find_element_by_xpath(".//td[contains(@title, 'High')]").click()

    # subcomp
    driver.find_element_by_id("DOM_357").click()
    driver.implicitly_wait(6)
    driver.find_element_by_xpath(".//td[contains(@title, 'OSP')]").click()

    # assignee
    driver.find_element_by_id("DOM_323").click()
    driver.implicitly_wait(9)
    driver.find_element_by_xpath(".//td[contains(@title, 'ytale')]").click()

    # start version
    driver.find_element_by_id("DOM_400").click()
    driver.implicitly_wait(6)
    driver.find_element_by_xpath(".//td[contains(@title, '5.10')]").click()

    # estimates
    driver.find_element_by_id("DOM_328").send_keys("1/8h")

    # requirement
    driver.find_element_by_id("DOM_569").click()
    driver.find_element_by_xpath(".//td[contains(text(), 'verifies')]").click()
    driver.find_element_by_id("DOM_572").send_keys("RHCF3-50251")
    driver.find_element_by_id("DOM_619").send_keys("")

    # save
    driver.find_element_by_xpath(".//td[contains(@title, '(CTRL + S)')]").click()

    time.sleep(5)
    print "** {} Added {} **".format(driver.current_url.split("id=")[1], test_name)


def get_testcase(filename):
    with open(filename) as f:
        for row in f:
            driver = webdriver.Chrome()
            driver.get(
                "https://polarion.hostname.com/polarion/#/project/RHCF3/workitem?form_mode=create&form_field_type=testcase"
            )
            driver.find_element_by_id("j_username").send_keys("#######")
            driver.find_element_by_id("j_password").send_keys("#######")
            driver.find_element_by_id("submitButton").send_keys(Keys.ENTER)
            try:
                element = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.ID, "DOM_455"))
                )
            finally:
                pass

            test_name = "OSP: {}".format(row.replace("\n", "").replace('"', ""))
            time.sleep(7)

            # polarion gives five types of DOM patterns, so instead of checking all DOM ids
            # we are waiting till DOM_307 pattern to appears, no other way :(
            try:
                driver.find_element_by_id("DOM_307").send_keys("")
            except WebDriverException:
                driver.refresh()
                time.sleep(10)
                # for first random DOM selection
                try:
                    driver.find_element_by_id("DOM_307").send_keys("")
                except WebDriverException:
                    driver.refresh()
                    time.sleep(10)
                    # for second random DOM selection
                    try:
                        driver.find_element_by_id("DOM_307").send_keys("")
                    except WebDriverException:
                        driver.refresh()
                        time.sleep(10)
                        # for third random DOM selection
                        try:
                            driver.find_element_by_id("DOM_307").send_keys("")
                        except WebDriverException:
                            driver.refresh()
                            time.sleep(10)
                            # for forth random DOM selection
                            try:
                                driver.find_element_by_id("DOM_307").send_keys("")
                            except WebDriverException:
                                driver.refresh()
                                time.sleep(10)
                                # for fifth random DOM selection
                                try:
                                    driver.find_element_by_id("DOM_307").send_keys("")
                                except WebDriverException:
                                    driver.refresh()
                                    time.sleep(10)

            create_testcase(driver, test_name)
            driver.close()


get_testcase("file.csv")
