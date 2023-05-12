*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8069/web/login/
${BROWSER}        Chrome
${CHROMEDRIVER_PATH}        /opt/odoo15/chromedriver
${LUNCH URL}     http://localhost:8069/web#cids=1&menu_id=119&action=199&model=lunch.product&view_type=kanban

*** Test Cases ***

My login test case
    I want to open odoo login page
    #Sleep    3s
    Input my username    divyavemula1227@gmail.com
   # Sleep    3s
    Input my password    Odoo_151
    #Sleep    3s
    Submit my credentials
    #Sleep    3s
    I should see this page
    Sleep    3s

Order a Pizza Margherita sandwich test case
    Open the lunch page
    Sleep    10s
    I click on Pizza Margherita

    Sleep    4s
    I click Add to Cart
    Sleep    5s
    I click Order Now
    Sleep    4s
    I should see Ordered
    Sleep    6s
    [Teardown]    Close Browser

*** Keywords ***

I want to open odoo login page
    ${chrome_options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --start-maximized
    Open Browser    ${LOGIN URl}    chrome    options=${chrome_options}      executable_path=${CHROMEDRIVER_PATH}
    Title Should Be    Odoo

Input my username
    [Arguments]    ${username}
    Input Text    login    ${username}

Input my password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit my credentials
    Click Element       //*[contains(text(),'Log in')]

I should see this page
    Title Should Be    Odoo

Open the lunch page
    Go To    ${LUNCH URL}

I click on Pizza Margherita
    Click Element       //*[contains(text(),'Tomatoes, Mozzarella')]

I click Add to Cart
    Click Element       //*[contains(text(),'Add To Cart')]

I click Order Now
    Click Element       //*[contains(text(),'Order now')]

I should see Ordered
    Page Should Contain              6.90€