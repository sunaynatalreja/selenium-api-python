from selenium.webdriver.support.events import EventFiringDecorator

class DriverWrapper:
    def __init__(self, driver, event_listener, config):
        self.driver = EventFiringDecorator(driver).decorate(event_listener)
        self.base_url = config["base_url"]

    def open(self):
        self.driver.get(self.base_url)

    def __getattr__(self, item):
        return getattr(self.driver, item)