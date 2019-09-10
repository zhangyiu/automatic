from time import sleep

def case1(self):
        
        self.driver.get(self.parameter.cell(0,1).value)
        print(self.driver.title)
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).send_keys(self.parameter.cell(1,2).value)
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).send_keys(self.parameter.cell(2,2).value)
        self.driver.find_element_by_xpath(self.parameter.cell(3,1).value).click()
        sleep(15)
        self.driver.maximize_window()
        name = ""
        try:
            name = self.driver.find_element_by_xpath(self.parameter.cell(6,1).value).text
            self.assertEqual(name, self.parameter.cell(6,2).value)
            # assert name == u'admin'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            self.assertEqual(name, self.parameter.cell(6,2).value)
        sleep(5)
        self.driver.close()


def case2(self):
        
        self.driver.get(self.parameter.cell(0,1).value)
        print(self.driver.title)
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).send_keys(self.parameter.cell(1,2).value)
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).send_keys(self.parameter.cell(2,2).value)
        self.driver.find_element_by_xpath(self.parameter.cell(3,1).value).click()
        sleep(15)
        self.driver.maximize_window()
        name = ""
        try:
            name = self.driver.find_element_by_xpath(self.parameter.cell(6,1).value).text
            self.assertEqual(name, self.parameter.cell(6,2).value)
            # assert name == u'admin'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            self.assertEqual(name, self.parameter.cell(6,2).value)
        sleep(5)
        self.driver.close()

def case3(self):

        self.driver.get(self.parameter.cell(0,1).value)
        print(self.driver.title)
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(1,1).value).send_keys(self.parameter.cell(1,2).value)
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).click()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).clear()
        self.driver.find_element_by_id(self.parameter.cell(2,1).value).send_keys(self.parameter.cell(2,2).value)
        self.driver.find_element_by_xpath(self.parameter.cell(3,1).value).click()
        sleep(15)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.parameter.cell(4,1).value).click()
        name = ""
        try:
            sleep(10)
            name=self.driver.find_element_by_xpath(self.parameter.cell(5,1).value).text
            self.assertEqual(u'检索火灾', self.parameter.cell(5,2).value)
            # assert name == u'admin'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            self.assertEqual(name, self.parameter.cell(5,2).value)
        sleep(5)
        self.driver.close()
