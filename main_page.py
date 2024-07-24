

class MainPage:
    def __init__(self, page):
        self.left_bowl = page.locator('css=[data-side="left"]')
        self.right_bowl = page.locator('css=[data-side="right"]')
        self.weigh_button = page.get_by_text('Weigh', exact=True)
        self.reset_button = page.get_by_text('Reset', exact=True)
        self.weighings = page.locator('css=li')
        self.success_message = page.locator('text=Yay! You find it!')
