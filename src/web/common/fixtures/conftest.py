# from utils.driver_manager import DriverFactory
# import pytest
# import allure
# from allure_commons.types import AttachmentType
#
# @pytest.fixture()
# def setup(request, config):
#     driver = DriverFactory.get_driver(config)
#     driver.implicitly_wait(config["timeout"])
#     request.cls.driver = driver
#     before_failed = request.session.testsfailed
#     if config["browser"] == "firefox":
#         driver.maximize_window()
#     yield
#     if request.session.testsfailed != before_failed:
#         allure.attach(driver.get_screenshot_as_png(),
#                       name="Test failed", attachment_type=AttachmentType.PNG)
#     driver.quit()