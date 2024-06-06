import json
import os
import pytest
from playwright.sync_api import expect,Playwright

# Parameterize the test function for positive or negative cases
@pytest.mark.parametrize(
    "username, password, casetype",
    [
        ("adtestdotnl@gmail.com", "Micky12345$", "Positivecase"),
        ("mishafrancis@gmail.com", "Micky12345$", "Negativecase"),
    ],
    # Custom IDs for each test case
    ids=["Positive-case", "Negative-case"]
)

### Usecase 1
def test_Usecase_1_AD_Login_Page_Check(playwright: Playwright,username, password,casetype) -> None:
        browser = playwright.chromium.launch(headless=False,args=['--disable-blink-features=AutomationControlled'])
        page = browser.new_page()

        ## Open URL
        page.goto('https://www.ad.nl/')

        ## Cookie popup close
        page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Akkoord").click()

        ## Enter details on login page (Positive & Negative)
        page.get_by_role("link", name="Inloggen", exact=True).click()
        page.get_by_text("E-mailadres", exact=True).fill(username)
        page.get_by_role("button", name="Ga verder Arrow right").click()
        page.get_by_test_id("password-input").fill(password)
        page.get_by_test_id("button").click()
        page.wait_for_load_state("networkidle")

        ## Validation
        if casetype == "Positivecase":
        #    expect(page.get_by_text("Inlogpoging geblokkeerd")).to_be_visible()
           expect(page.get_by_title("Micky Mouse").locator("label")).to_be_visible()
                  
           ## Screen capture
           page.wait_for_load_state('load')
           folder_path = 'result_screenshots'
           screenshot_path = os.path.join(folder_path, 'Usecase_1_screenshot_Positive.png')
           page.screenshot(path=screenshot_path)

        else:
           expect(page.get_by_text("Wachtwoord is niet correct.")).to_be_visible()
       
           ## Screen capture
           page.wait_for_load_state('load')
           folder_path = 'result_screenshots'
           screenshot_path = os.path.join(folder_path, 'Usecase_1_screenshot_Negative.png')
           page.screenshot(path=screenshot_path)

        ## Close browser
        browser.close()


### Usecase 2
def test_Usecase_2_Article_Check(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        ## Open URL
        page.goto('https://www.ad.nl/')

        ## Cookie popup close
        page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Akkoord").click()

        ## Navigation to element
        page.get_by_role("link", name="Zoek", exact=True).click()
        page.wait_for_load_state('load')
        page.get_by_placeholder("Zoek op trefwoord, titel of").fill("sport")
        page.get_by_label("zoek", exact=True).click()

        ## Validations
        expect(page.get_by_role("heading", name="Gevonden resultaten voor “")).to_be_visible()

        ## Screen capture
        page.wait_for_load_state('load')
        folder_path = 'result_screenshots'
        screenshot_path = os.path.join(folder_path, 'Usecase_2_screenshot.png')
        page.screenshot(path=screenshot_path)

        ## Close browser
        browser.close()


### Usecase 3
def test_Usecase_3_Sport_Podcast_Check(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        ## Open URL
        page.goto('https://www.ad.nl/podcasts')

        ## Cookie popup close
        page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Akkoord").click()

        ## Navigation to element
        page.get_by_role("link", name="AD Voetbal podcast AD Voetbal").nth(2).click()
        page.get_by_role("link", name="'Er gaan dit EK meer").click()

        ## Validations
        expect(page.frame_locator("#entertainment-root iframe").get_by_text("'Er gaan dit EK meer")).to_be_visible
        expect(page.get_by_role("heading", name="'Er gaan dit EK meer")).to_be_visible

        ## Screen capture
        page.wait_for_load_state("networkidle")
        folder_path = 'result_screenshots'
        screenshot_path = os.path.join(folder_path, 'Usecase_3_screenshot.png')
        page.screenshot(path=screenshot_path)

        ## Close browser
        browser.close()


