*** Settings ***
Library    BuiltIn
Library    Collections

*** Variables ***
@{COLORS}    Red    Green    Blue
@{USERS}     admin    user
@{PWDS}      admin123    user123

*** Test Cases ***

Print Names using for loop
    FOR    ${Name}    IN    Ram    Ravi    Taj
        Log To Console    ${Name}
    END

Print Numbers using while loop
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=    Evaluate    ${count} + 1
    END

IF Condition Example
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log To Console    Eligible to vote
    END

IF ELSE Example
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END

IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log To Console    Grade A
    ELSE IF    ${marks} >= 75
        Log To Console    Grade B
    ELSE
        Log To Console    Grade C
    END

Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'
        Log To Console    Test Passed
    END

FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log To Console    Item: ${item}
    END

FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log To Console    Color: ${color}
    END

FOR Loop Range
    FOR    ${i}    IN RANGE    1    6
        Log To Console    Number: ${i}
    END

FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2
        Log To Console    Value: ${i}
    END

FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    ${index} = ${value}
    END

FOR Loop Zip (Safe Version)
    FOR    ${i}    IN RANGE    0    2
        ${u}=    Get From List    ${USERS}    ${i}
        ${p}=    Get From List    ${PWDS}     ${i}
        Log To Console    ${u} / ${p}
    END

Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log To Console    i=${i}, j=${j}
        END
    END

FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log To Console    Found 3
        END
    END

BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log To Console    ${i}
    END

CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log To Console    ${i}
    END

WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log To Console    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log To Console    Error handled
    FINALLY
        Log To Console    Always executed
    END

Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log To Console    Test Passed

Run Keyword Unless (Modern Way)
    ${status}=    Set Variable    FAIL
    IF    '${status}' != 'PASS'
        Log To Console    Test Failed
    END