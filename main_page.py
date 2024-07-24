

class MainPage:
    def __init__(self, page):
        self.left_bowl = page.locator('css=[data-side="left"]')
        self.right_bowl = page.locator('css=[data-side="right"]')
        self.weigh_button = page.get_by_text('Weigh', exact=True)
        self.reset_button = page.get_by_text('Reset', exact=True)
        self.weighings = page.locator('css=li')
        self.success_message = page.locator('text=Yay! You find it!')

    def check_the_group(self, page, needed_group, left_bowl, right_bowl, main_page):
        main_page.reset_button.click()
        left_bowl[0].fill(str(needed_group[0]))
        right_bowl[0].fill(str(needed_group[1]))
        main_page.weigh_button.click()
        page.wait_for_selector('css=li:nth-child(2)')
        weighings = main_page.weighings.all()
        if "=" in weighings[1].text_content():
            needed_number = needed_group[2]
        elif ">" in weighings[1].text_content():
            needed_number = needed_group[1]
        elif "<" in weighings[1].text_content():
            needed_number = needed_group[0]
        return needed_number
