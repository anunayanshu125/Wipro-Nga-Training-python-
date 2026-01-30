*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    ${CURDIR}/test.xlsx    sheet_name=Sheet1    dialect=Excel
Library    String
Suite Setup       Open TutorialsNinja
Suite Teardown    Close All Browsers

*** Variables ***
${URL}        https://tutorialsninja.com/demo/
${BROWSER}    chrome
${DELAY}      3s

*** Test Cases ***
Register users from Excel
    [Tags]    REGISTER
    [Template]    Register User

Login users from Excel
    [Tags]    LOGIN
    [Template]    Login User

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    ${DELAY}

Go To Home
    Go To    ${URL}
    Sleep    ${DELAY}

Generate Unique Email
    ${rand}    Generate Random String    6    [NUMBERS]
    ${email}   Set Variable    user${rand}@gmail.com
    [Return]   ${email}

Safe Logout
    Click Element    xpath=//span[text()='My Account']
    Sleep    ${DELAY}
    Run Keyword And Ignore Error    Click Link    Logout
    Sleep    ${DELAY}

Register User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

    Go To Home

    ${generated_email}    Generate Unique Email
    Set Test Variable     ${TEST_EMAIL}    ${generated_email}

    Click Element    xpath=//span[text()='My Account']
    Sleep    ${DELAY}
    Click Link       Register
    Sleep    ${DELAY}

    Input Text    id=input-firstname    ${firstname}
    Sleep    ${DELAY}
    Input Text    id=input-lastname     ${lastname}
    Sleep    ${DELAY}
    Input Text    id=input-email        ${TEST_EMAIL}
    Sleep    ${DELAY}
    Input Text    id=input-telephone    ${telephone}
    Sleep    ${DELAY}
    Input Password    id=input-password     ${password}
    Sleep    ${DELAY}
    Input Password    id=input-confirm      ${password}
    Sleep    ${DELAY}

    Click Element    xpath=//input[@name='newsletter' and @value='1']
    Sleep    ${DELAY}
    Click Element    name=agree
    Sleep    ${DELAY}

    Click Button    xpath=//input[@value='Continue']
    Sleep    ${DELAY}

    Safe Logout

Login User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

    Go To Home

    Click Element    xpath=//span[text()='My Account']
    Sleep    ${DELAY}
    Click Link       Login
    Sleep    ${DELAY}

    Input Text       id=input-email       ${TEST_EMAIL}
    Sleep    ${DELAY}
    Input Password   id=input-password    ${password}
    Sleep    ${DELAY}
    Click Button     xpath=//input[@value='Login']
    Sleep    ${DELAY}

    Safe Logout
