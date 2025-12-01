*** Settings ***
Documentation     This is a tryout test suite for Robot Framework.

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com
${ENDPOINT}    /todos/1
${NUMBER_ONE}    10
${NUMBER_TWO}    20
*** Test Cases ***
Add Test
        Add Numbers
Compare String Test
    Compare Strings    Hello World    Hello Robot Framework

*** Keywords ***
Add Numbers
    ${result}=    Evaluate    ${NUMBER_ONE} + ${NUMBER_TWO}
    Log To Console    The result of adding ${NUMBER_ONE} and ${NUMBER_TWO} is: ${result}

Compare Strings
    [Arguments]    ${string3}    ${string4}
    ${string1}=    Set Variable    Hello World
    ${string2}=    Set Variable    Hello World
    Should Be Equal    ${string1}    ${string2}    Strings are not equal!
    Should Not Be Equal    ${string3}    ${string4}    Strings should not be equal!