*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8069/web/login/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Sleep   5s
    Input Username    divyavemula1227@gmail.com
    Sleep   5s
    Input Password    Odoo_151
    Submit Credentials
    Sleep   5s
    Welcome Page Should Be Open
    Sleep   5s
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Odoo

Input Username
    [Arguments]    ${username}
    Input Text    login    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Element       //*[contains(text(),'Log in')]

Welcome Page Should Be Open
    Title Should Be    Odoo - Discuss
