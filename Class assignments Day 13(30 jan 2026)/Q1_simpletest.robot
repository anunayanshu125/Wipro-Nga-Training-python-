*** Settings ***
Library    SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome
${TITLE}     OrangeHRM
${SCREENSHOT_PATH}    screenshot.png

*** Test Cases ***
Open Browser, Verify Title and Capture Screenshot
    [Documentation]    Open browser, navigate to URL, verify page title, take screenshot, and close browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s
    Title Should Be    ${TITLE}
    Capture Page Screenshot    ${SCREENSHOT_PATH}
    Sleep    1s