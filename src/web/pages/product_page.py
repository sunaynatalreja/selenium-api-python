from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class ProductPage(PageFactory):

    locators = {
        "womenCategories": ("XPATH","//*[@title='Women' and @class='sf-with-ul']"),
        "filters":("XPATH","//div[@class='layered_filter']/ul"),
        "products":("XPATH","//div[@itemprop='offers']"),
        "proceedToCheckout":("XPATH","//*[@title='Proceed to checkout']"),
        "proceedToCheckoutPage":("XPATH","(//*[contains(text(),'Proceed to checkout')])[2]"),
        "email":("ID", "email"),
        "password":("ID","passwd"),
        "submitLogin":("ID", "SubmitLogin"),
        "terms":("ID","uniform-cgv"),
        "bankwire":("XPATH", "//*[@class='bankwire']"),
        "confirmOrder":("XPATH","//*[contains(text(),'I confirm my order')]"),
        "orderDetails":("XPATH","//*[@class='box']"),
    }
        
    def __init__(self, driver):
        self.driver = driver
    
    def 