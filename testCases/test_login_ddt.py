import time

import pytest
from selenium import webdriver

from Utilities import XlUtils
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage



class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path= ".//TestData/LoginData.xlsx"


    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("****Test_002_DDT_Login test****")
        self.logger.info("*********Verify Login test**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        lst_status=[]

        self.rows=XlUtils.getRowCount(self.path,'Sheet1')
        print("number of rows in excel",+self.rows)

        for r in range(2,self.rows+1):
            self.user= XlUtils.readData(self.path,'Sheet1',r,1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title= self.driver.title
            exp_title= "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("Pass")
                    self.lp.clickLogout()
                    time.sleep(5)
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Failed")
                    self.lp.clickLogout()
                    time.sleep(5)
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("Failed")
                    self.lp.clickLogout()
                    time.sleep(5)
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Passed")
                    time.sleep(5)
                    self.lp.clickLogout()
                    time.sleep(5)
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test Failed")
            self.driver.close()
            assert False

        self.logger.info("**** End of login DDT*****")
        self.logger.info("******Completed TC_LoginDDT_002*****")





