from flet import Page, Container, Card, Column, Text
class LoginPage:
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.page.bgcolor = "#e6f7ff"
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
    

    def build(self):
        return Container(content=Column(controls=[Text(value="Hi")]))