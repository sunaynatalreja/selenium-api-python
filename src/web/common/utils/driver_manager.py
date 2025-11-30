from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.web.base.driver_wrapper import DriverWrapper
from src.web.base.webdriver_listener import WebDriverListener


class DriverManager:
    def get_driver(config):
        options=None
        match config["browser"]:
            case "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                if config["headless_mode"] is True:
                    options.add_argument("--headless")
                driver = DriverWrapper(
                    webdriver.Chrome(ChromeDriverManager().install(), options=options),
                    WebDriverListener(), config
                )
                return driver
            case "firefox":
                options = webdriver.FirefoxOptions()
            case "edge":
                options = webdriver.EdgeOptions()
                options.use_chromium = True