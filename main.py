from flet import Page, app
from controllers.page_controller import route_change
import warnings
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

def main(page: Page):
    page.title = "InChat"
    # page.window.width = 300
    page.on_route_change = route_change

    # Start on LoginPage or another default page
    page.go("/login_page")

app(target=main)