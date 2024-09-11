from flet import (Page, Container,Text)

class PermissionPage:
    
    def __init__(self, page: Page, **kwargs):
        self.page = page


    def build(self):
        return Container(content=Text("Permission Page"))