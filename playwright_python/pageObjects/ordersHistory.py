from .ordersDetails import OrdersDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def select_orders(self, order_id):
        rowNeeded = self.page.locator(f"//tr[th[contains(text(), '{order_id}')]]")
        rowNeeded.locator("xpath=.//td/button[contains(text(),'View')]").click()
        ordersDetailsPage = OrdersDetailsPage(self.page)
        return ordersDetailsPage
