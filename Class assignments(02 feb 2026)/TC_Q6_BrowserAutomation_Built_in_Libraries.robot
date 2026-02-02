*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

Suite Setup     Open Browser To Form
Suite Teardown  Close Browser

*** Variables ***
${URL}        https://demoqa.com/automation-practice-form
${BROWSER}    chrome

*** Keywords ***
Open Browser To Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s
    ${count}=    Get Element Count    id=fixedban
    Run Keyword If    ${count} > 0    Execute JavaScript    document.getElementById('fixedban').style.display='none'

Fill Form
    Input Text    id=firstName    Anunay
    Sleep    1s
    Input Text    id=lastName     Kumar
    Sleep    1s
    Input Text    id=userEmail    anunay@test.com
    Sleep    1s
    Click Element    xpath=//label[text()='Male']
    Sleep    1s
    Input Text    id=userNumber    9876543210
    Sleep    1s

Select Hobbies
    Scroll Element Into View    xpath=//label[text()='Sports']
    Sleep    1s
    Execute JavaScript    document.querySelector("label[for='hobbies-checkbox-1']").click()
    Sleep    2s

Select State And City
    Scroll Element Into View    id=state
    Sleep    1s
    Input Text    xpath=//input[@id='react-select-3-input']    NCR
    Press Keys    xpath=//input[@id='react-select-3-input']    ENTER
    Sleep    1s
    Input Text    xpath=//input[@id='react-select-4-input']    Delhi
    Press Keys    xpath=//input[@id='react-select-4-input']    ENTER
    Sleep    2s

Submit And Validate
    Scroll Element Into View    id=submit
    Sleep    1s
    Click Button    id=submit
    Sleep    2s
    ${text}=    Get Text    id=example-modal-sizes-title-lg
    Should Be Equal    ${text}    Thanks for submitting the form
    Sleep    1s
    Click Button    id=closeLargeModal
    Sleep    1s

*** Test Cases ***
Form Automation Using Selenium And BuiltIn
    Fill Form
    Select Hobbies
    Select State And City
    Submit And Validate
