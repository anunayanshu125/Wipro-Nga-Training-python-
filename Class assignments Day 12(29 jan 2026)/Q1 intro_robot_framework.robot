*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Robot Framework
${VERSION}     7.4.1
@{COURSES}     Python    Robot    Selenium

*** Test Cases ***
Test Case 1 - Log Basic Information
    Log    Welcome to ${NAME}
    Log To Console    Running tests using ${NAME}
    Log    Current version is ${VERSION}

Test Case 2 - Use List Variables
    Log    Available courses:
    Log To Console    Courses list: ${COURSES}
    ${count}=    Get Length    ${COURSES}
    Log    Total courses count is ${count}