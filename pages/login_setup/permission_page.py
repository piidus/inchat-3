from flet import (Page, Container,Text, ListView, border, border_radius, ElevatedButton,
                  colors, padding, Row, Switch, PermissionType, PermissionStatus, PermissionHandler)

class PermissionPage:
    
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.permission_handler = PermissionHandler()
        self.page.overlay.append(self.permission_handler)

    def did_mount(self):
        # self.disable_button.disabled = False
        pass
    



    def request_permission(self, e):
        o = self.permission_handler.request_permission(e.control.data)
        
        self.page.add(Text(f"Requested {e.control.data.name}: {o}"))
    def storage_click(self, e):
        print("storage_click")
        print(e.control.value)
        if e.control.value:
            self.request_permission(e)
    def heading(self):
        return Text("Permission Page", text_align="center")
    def storage_permission(self):
        switch = Switch(value=False, scale=0.8,
                        data = PermissionType.STORAGE,
                         on_change=self.storage_click)

        row = Row(controls=[Text("Storage Permission"), switch])
        container = Container(
            bgcolor=colors.BLUE_GREY_100,
            border=border.all(2, colors.BLACK),
            border_radius=border_radius.all(10),
            padding=padding.all(10),
            content=row,
        )
        return container
    def build(self):
        return ListView(controls=[self.heading(), self.storage_permission()])