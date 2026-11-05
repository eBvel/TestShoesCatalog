from selenium.webdriver.common.by import By


class MainPageLocators:
	CATALOG = (By.XPATH, "//a[contains(text(),'Каталог')]")
	RUNNING_SHOES = (By.CSS_SELECTOR, "a[href='/catalog/krossovki/']")
	BOOTS = (By.CSS_SELECTOR, "a[href='/catalog/botinki/']")
	SHOES = (By.CSS_SELECTOR, "a[href='/catalog/tufli/']")
	SNEAKERS = (By.CSS_SELECTOR, "a[href='/catalog/kedy/']")
	WINTRY = (By.XPATH, "(//a[@href='/catalog/botinki/zimnie/'])[1]")
