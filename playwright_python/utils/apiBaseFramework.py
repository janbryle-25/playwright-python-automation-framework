from playwright.sync_api import Playwright, expect

ordersPayload = {"orders": [{"country": "Philippines", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
authorization = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWMxNDBmMmY4NmJhNTFhNjUxZjc4NmMiLCJ1c2VyRW1haWwiOiJudXp1bWFraUBnbWFpbC5jb20iLCJ1c2VyTW9iaWxlIjozNDI0MjQyMzQyLCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzc0Mjc1NjI2LCJleHAiOjE4MDU4MzMyMjZ9.2u9CpnPJOcCPgFGv1-gvzCgVRTXSks2zkvuVLFdQ15s"
loginPayload = {"userEmail": "nuzumaki@gmail.com", "userPassword": "Naruto_123"}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        userEmail = user_credentials['userEmail']
        userPassword = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post("/api/ecom/auth/login"
                                            ,data={"userEmail": userEmail, "userPassword": userPassword}
                                            ,headers={"Content-Type": "application/json"}
                                            )
        assert response.ok
        print(response.json())
        responseBody = response.json()
        token = responseBody['token']
        return token

    def createOrder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order"
                                 , data= ordersPayload
                                 , headers= {"Authorization": token,
                                             "Content-Type": "application/json"}
                                )
        print(response.json())
        responseBody = response.json()
        orderID = responseBody['orders']
        return orderID[0]


