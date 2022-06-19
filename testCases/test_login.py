import pytest
from selenium import webdriver

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage



class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):

        self.logger.info("*********Test_001_Login**********")
        self.logger.info("*********Verify Homepage Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        self.logger.info("*********Home page title test passed**********")
        if act_title == "Your store. Login":
            assert True
        else :
            self.driver.save_screenshot(".\\Screenshots"+"test_homePageTitle.png")
            assert  False
            self.logger.error("*********Home page title test passed**********")

    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("*********Verify Login test**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.close()
        actu_title = self.driver.title

        if actu_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********Login test passed**********")
        else :
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            assert  False
            self.logger.error("*********Login test failed**********")