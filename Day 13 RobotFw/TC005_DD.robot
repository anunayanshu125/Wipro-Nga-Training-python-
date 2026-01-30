*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    15s

OrangeHRM Login
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Capture Page Screenshot    beforelogin.png
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains Element    xpath=//span[@class='oxd-userdropdown-tab']    15s
    Capture Page Screenshot    afterlogin.png
    Close Browser

*** Test Cases ***
TC005_Login_Valid_User
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123