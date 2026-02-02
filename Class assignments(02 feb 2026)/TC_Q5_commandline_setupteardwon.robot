* Settings *
Library           BuiltIn
Suite Setup       Suite Initialization
Suite Teardown    Suite Cleanup
Test Setup        Test Initialization
Test Teardown     Test Cleanup

* Keywords *
Suite Initialization
    Log To Console    ===== Suite Setup: Test Suite Started =====

Suite Cleanup
    Log To Console    ===== Suite Teardown: Test Suite Finished =====

Test Initialization
    Log To Console    --- Test Setup: Test Started ---

Test Cleanup
    Log To Console    --- Test Teardown: Test Finished ---

* Test Cases *
Addition Test
    [Tags]    smoke
    ${sum}=    Evaluate    10 + 20
    Log To Console    Sum is ${sum}

Subtraction Test
    [Tags]    regression
    ${result}=    Evaluate    50 - 30
    Log To Console    Result is ${result}

Multiplication Test
    [Tags]    sanity
    ${mul}=    Evaluate    5 * 4
    Log To Console    Multiplication is ${mul}