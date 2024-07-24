import re
import time

from playwright.sync_api import Playwright, sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://sdetchallenge.fetch.com/")
        group_A = [0, 1, 2]
        group_B = [3, 4, 5]
        group_C = [6, 7, 8]
        left_bowl = page.locator('css=[data-side="left"]').all()
        index = 0
        while index < 3:
            left_bowl[index].fill(str(group_A[index]))
            index += 1
        right_bowl = page.locator('css=[data-side="right"]').all()
        index = 0
        while index < 3:
            right_bowl[index].fill(str(group_B[index]))
            index += 1
        page.get_by_text('Weigh', exact=True).click()
        page.wait_for_selector('css=li')
        weighings = page.locator('css=li').all()
        if "=" in weighings[0].text_content():
            needed_group = group_C
            needed_number = check_the_group(page, needed_group, left_bowl, right_bowl)

        elif ">" in weighings[0].text_content():
            needed_group = group_B
            needed_number = check_the_group(page, needed_group, left_bowl, right_bowl)

        elif "<" in weighings[0].text_content():
            needed_group = group_A
            needed_number = check_the_group(page, needed_group, left_bowl, right_bowl)

        print(needed_number)
        page.click(f'text="{needed_number}"')
        # For some reason the code below works ONLY if I click it manually, so I've added another verification
        # alert_message = page.wait_for_event("dialog").message
        page.get_by_text("Yay! You find it!", exact=True)

        # Output the result
        print(f"Congratulations! You found the fake gold bar {needed_number}.")

        context.close()
        browser.close()

def check_the_group(page, needed_group, left_bowl, right_bowl):
    page.get_by_text('Reset').click()
    left_bowl[0].fill(str(needed_group[0]))
    right_bowl[0].fill(str(needed_group[1]))
    page.get_by_text('Weigh', exact=True).click()
    page.wait_for_selector('css=li:nth-child(2)')
    weighings = page.locator('css=li').all()
    if "=" in weighings[1].text_content():
        needed_number = needed_group[2]
    elif ">" in weighings[1].text_content():
        needed_number = needed_group[1]
    elif "<" in weighings[1].text_content():
        needed_number = needed_group[0]
    return needed_number

if __name__ == "__main__":
    main()
