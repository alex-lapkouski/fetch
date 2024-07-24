from playwright.sync_api import Playwright, sync_playwright, expect
from main_page import MainPage

def weigh_test(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    page.goto("http://sdetchallenge.fetch.com/")
    group_A = [0, 1, 2]
    group_B = [3, 4, 5]
    group_C = [6, 7, 8]
    left_bowl = main_page.left_bowl.all()
    index = 0
    while index < 3:
        left_bowl[index].fill(str(group_A[index]))
        index += 1
    right_bowl = main_page.right_bowl.all()
    index = 0
    while index < 3:
        right_bowl[index].fill(str(group_B[index]))
        index += 1
    main_page.weigh_button.click()
    expect(main_page.weighings).to_be_visible()
    weighings = main_page.weighings.all()
    if "=" in weighings[0].text_content():
        needed_group = group_C
        needed_number = main_page.check_the_group(page, needed_group, left_bowl, right_bowl, main_page)

    elif ">" in weighings[0].text_content():
        needed_group = group_B
        needed_number = main_page.check_the_group(page, needed_group, left_bowl, right_bowl, main_page)

    elif "<" in weighings[0].text_content():
        needed_group = group_A
        needed_number = main_page.check_the_group(page, needed_group, left_bowl, right_bowl, main_page)

    print(needed_number)
    page.click(f'text="{needed_number}"')
    # For some reason the code below works ONLY if I click it manually, so I've added another verification
    # alert_message = page.wait_for_event("dialog").message
    page.get_by_text("Yay! You find it!", exact=True)

    # Output the result
    print(f"Congratulations! You found the fake gold bar {needed_number}.")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    weigh_test(playwright)
