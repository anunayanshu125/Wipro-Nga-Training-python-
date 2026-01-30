work Ve*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    ===== Environment Verification Started =====

    Verify Python Installation
    Verify Robot Framework Installation
    Print Robot Framework Version

    Log To Console    ===== Environment Verification Completed =====

*** Keywords ***
Verify Python Installation
    ${python_version}=    Evaluate    __import__('sys').version
    Run Keyword If    '${python_version}' == ''    Fail    Python is NOT installed
    Log    Python Version: ${python_version}
    Log To Console    Python is installed successfully

Verify Robot Framework Installation
    ${rf_version}=    Evaluate    __import__('robot').__version__
    Run Keyword If    '${rf_version}' == ''    Fail    Robot Framework is NOT installed
    Log    Robot Framework Version: ${rf_version}
    Log To Console    Robot Framework is installed successfully

Print Robot Framework Version
    ${version}=    Evaluate    __import__('robot').__version__
    Log    Robot Framework Version is ${version}
    Log To Console    Robot Framework Version: ${version}
rsion: ${version}