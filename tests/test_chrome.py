from selenium import webdriver
import pytest


def test_chrome():
    # create a new Chrome session
    driver = webdriver.Chrome(pytest.chromedriver)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("http://www.google.com")

    # get the search textbox
    #search_field = driver.find_element_by_id("lst-ib")
    #search_field.clear()

    # enter search keyword and submit
    #search_field.send_keys("Selenium WebDriver")
    #search_field.submit()

    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name  method
    #lists = driver.find_elements_by_class_name("_Rm")

    # get the number of elements found
    #print("Found " + str(len(lists)) + " searches:")

    assert "Google" in driver.title

    # close the browser window
    driver.quit()
