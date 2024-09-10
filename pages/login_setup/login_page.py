from flet import (Page, Container, Card, Column, Text, border, border_radius, 
                  colors, alignment, CrossAxisAlignment, MainAxisAlignment)

class LoginPage:
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.page.bgcolor = "#e6f7ff"
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        # Attempt to get the 'windowheight' value from kwargs or default to 400
        self._page_height = float(self.page._Control__attrs.get('height', ('650', False))[0] or '600')
        self._page_width = float(self.page._Control__attrs.get('width', ('400', False))[0] or '400')
    def did_mount(self):
        print('[LoginPage] __init__ called', self._page_height)
        # self.page_height, self.page_width = 800,500
        print('[windowheight]',self.page._Control__attrs['windowheight'])
        print('[windowwidth]',self.page._Control__attrs['windowwidth'])
        print('[height]',self.page._Control__attrs['height'])
        print('[width]',self.page._Control__attrs['width'])
        # print('[LoginPage] did_mount called', self.page_height, self.page_width)
    def size(self, height:int = 100, width:int= 100)->int:
        new_height = float(self._page_height * (height /100))
        new_wight = self._page_width * width /100
        return new_height, new_wight

    def main_card(self):
        card_height, card_width = self.size(50, 80)
        # print(type(card_height), card_width)
        card= Card(content=Text(value='New'), 
                   height=card_height,  
                   width=card_width,                    
                   elevation=10, 
                   shadow_color='5555')
        list_view = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
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