from flet import (Page, Container, Card, Column, Text, border, border_radius, 
                  colors, alignment, CrossAxisAlignment, MainAxisAlignment)

class LoginPage:
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.page.bgcolor = "#e6f7ff"
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
    
    def size(self, height:int = 100, width:int= 100)->int:
        new_height = self.page.window.height * (height /100)
        new_wight = self.page.window.width * width /100
        # print(self.page.window.width, new_wight)
        return new_height, new_wight

    def main_card(self):
        card_height, card_width = self.size(50, 80)
        # print(card_height, card_width)
        card= Card(content=Text(value='New'),   
                    # align = 'center',
                   height=card_height,
                   width=card_width,
                   elevation=10, shadow_color='5555')
        list_view = Column(
            alignment=MainAxisAlignment.CENTER,
            # horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[card,],
            expand=True)
        
        # def build(self):
        return list_view
    def build(self):
        # _, width = self.size(width=80)
        return Container(
            alignment=alignment.center,
            bgcolor=colors.BLUE_GREY_100,
            border=border.all(2, colors.BLACK),
            border_radius= border_radius.all(10),
            padding= 30,
            margin=30,
            expand_loose=True,
            expand=True,
            content=Column(controls=[ self.main_card()]))