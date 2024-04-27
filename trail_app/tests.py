from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
class LoginFormTest(LiveServerTestCase):
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('1')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        #time.sleep(10)
        
        assert 'craig' in self.driver.page_source

class LoginFormTestFail(LiveServerTestCase):
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('2')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        user_name.clear()
        #time.sleep(10)
        
        assert 'craig' in self.driver.page_source
class CreateTrailTest(LiveServerTestCase):
    def test_creation(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('1')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        
        self.driver.get('http://127.0.0.1:8000/state/trail_form/1')
        
        trail_name = self.driver.find_element(by="id", value="id_name")
        trail_state = self.driver.find_element(by="id", value="id_state")
        trail_location = self.driver.find_element(by="id", value="id_location")
        trail_temperature = self.driver.find_element(by="id", value="id_temperature")
        trail_weather = self.driver.find_element(by="id", value="id_weather")
        trail_zip = self.driver.find_element(by="id", value="id_zip_code")
        trail_description = self.driver.find_element(by="id", value="id_description")
        trail_image = self.driver.find_element(by="id", value="id_image")
        trail_active = self.driver.find_element(by="id", value="id_is_active")
        
        update = self.driver.find_element(by="id", value="update")
        time.sleep(20)
        trail_active.click()
        trail_image.send_keys(r'C:\Users\Craig Lillemon\cs3300project\trail_app\static\images\cs3300Project.jpg')
        #time.sleep(3)
        trail_name.send_keys("Test 1")
        trail_temperature.send_keys(98)
        select = Select(trail_state)
        time.sleep(3)
        select.select_by_index(2)
        time.sleep(3)
        trail_location.send_keys("Test 1 location")
        #time.sleep(3)
        trail_zip.send_keys(80919)
        #time.sleep(3)
        trail_weather.send_keys("Test 1 weather")
        trail_description.send_keys("Test 1 description")
        
        time.sleep(3)
        
        time.sleep(3)
        update.send_keys(Keys.RETURN)
        time.sleep(10)
        assert 'Trails in Alabama' in self.driver.page_source
class UpdateTrailTest(LiveServerTestCase):
    def test_update(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('1')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        
        self.driver.get('http://127.0.0.1:8000/trail/1/UPDATE/')
        
        trail_name = self.driver.find_element(by="id", value="id_name")
        trail_name.clear()
        trail_name.send_keys("Changed")
        
        update = self.driver.find_element(by="id", value="update")
        
        
        time.sleep(3)
        update.send_keys(Keys.RETURN)
        time.sleep(10)
        assert 'Please click state' in self.driver.page_source
class DeleteTrailTest(LiveServerTestCase):
    def test_delete(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('1')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        self.driver.get ('http://127.0.0.1:8000/trail/3/delete/')
        time.sleep(3)
        delete = self.driver.find_element(by="id", value="delete")
        delete.send_keys(Keys.RETURN)
        time.sleep(8)
        assert 'Please click state' in self.driver.page_source

class ViewUserStateDetail(LiveServerTestCase):
    def test_view(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/accounts/login/' )
        user_name = self.driver.find_element(by="id", value="id_username")
        user_password = self.driver.find_element(by="id", value='id_password')
        submit = self.driver.find_element(by="id", value="submit")
        #time.sleep(5)
        user_name.send_keys('craig')
        #time.sleep(5)
        user_password.send_keys('1')
        #time.sleep(3)
        submit.send_keys(Keys.RETURN)
        
        self.driver.get('http://127.0.0.1:8000/state/user/1')
        assert 'New' in self.driver.page_source


