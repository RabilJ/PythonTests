*** Settings ***
Documentation     This is a tryout test suite for Robot Framework.
Library    OperatingSystem
Library    RequestsLibrary
Library    urllib3

Suite Setup    Disable TLS Warnings

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com
${ENDPOINT}    /todos/1

*** Test Cases ***
Create Session Test
    Create Session Keyword


*** Keywords ***
Create Session Keyword
    [Documentation]    Test sprawdza, czy endpoint zwraca poprawne dane.
    Create Session    jsonapi    ${BASE_URL}
    ${response}=    GET On Session    jsonapi    ${BASE_URL}${ENDPOINT}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    Otrzymana odpowiedź: ${response.content}

Disable TLS Warnings
    #Wyłaczenie TLS warning
    Evaluate    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)