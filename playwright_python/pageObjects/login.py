from .dashboard import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client')

    def login(self,user_email,user_password):
        self.page.locator("//input[@id='userEmail']").fill(user_email)
        self.page.locator("//input[@id='userPassword']").fill(user_password)
        self.page.locator("//input[@id='login']").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage