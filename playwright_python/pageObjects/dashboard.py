from .ordersHistory import OrdersHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def goToOrders(self):
        self.page.locator("//button[contains(text(), 'ORDERS')]").click()
        ordersHistoryPage = OrdersHistoryPage(self.page)
        return ordersHistoryPage
