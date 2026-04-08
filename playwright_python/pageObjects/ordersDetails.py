from playwright.sync_api import expect


class OrdersDetailsPage:
    def __init__(self, page):
        self.page = page

    def verifyOrderMessage(self):
        expect(self.page.locator("//p[@class='tagline']")).to_have_text('Thank you for Shopping With Us')