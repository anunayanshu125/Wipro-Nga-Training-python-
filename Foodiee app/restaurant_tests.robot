*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    OperatingSystem
Library    SeleniumLibrary

Suite Setup    Setup Environment
Suite Teardown    Finalize Execution

*** Variables ***
${restaurant_id}    0
${user_id}          0
${order_id}         0
${dish_id}          0

*** Test Cases ***

Register Restaurant
    ${images}=    Create List    img1.jpg
    ${body}=    Create Dictionary    name=Food junction    category=Non Veg    location=Bihar   images=${images}    contact=9999999999
    ${res}=    POST On Session    foodie    /restaurants    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads($res.text)
    Set Suite Variable    ${restaurant_id}    ${json["id"]}
    Log Result    Register Restaurant

Duplicate Restaurant
    ${images}=    Create List    img1.jpg
    ${body}=    Create Dictionary    name=Food junction    category=Non Veg    location=Bihar    images=${images}    contact=9999999999
    ${res}=    POST On Session    foodie    /restaurants    json=${body}    expected_status=409
    Status Should Be    409    ${res}
    Log Result    Duplicate Restaurant

View Restaurant
    ${res}=    GET On Session    foodie    /restaurants/${restaurant_id}
    Status Should Be    200    ${res}
    Log Result    View Restaurant

Update Restaurant
    ${body}=    Create Dictionary    location=Kolkata
    ${res}=    PUT On Session    foodie    /restaurants/${restaurant_id}    json=${body}
    Status Should Be    200    ${res}
    Log Result    Update Restaurant

Disable Restaurant
    ${res}=    PUT On Session    foodie    /restaurants/${restaurant_id}/disable
    Status Should Be    200    ${res}
    Log Result    Disable Restaurant

Add Dish
    ${body}=    Create Dictionary    name=chicken    type=Non Veg    price=300    available_time=10AM-10PM    image=chicken.jpg
    ${res}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads($res.text)
    Set Suite Variable    ${dish_id}    ${json["id"]}
    Log Result    Add Dish

Update Dish
    ${body}=    Create Dictionary    price=300
    ${res}=    PUT On Session    foodie    /dishes/${dish_id}    json=${body}
    Status Should Be    200    ${res}
    Log Result    Update Dish

Toggle Dish Status
    ${body}=    Create Dictionary    enabled=False
    ${res}=    PUT On Session    foodie    /dishes/${dish_id}/status    json=${body}
    Status Should Be    200    ${res}
    Log Result    Toggle Dish Status

Delete Dish
    ${res}=    DELETE On Session    foodie    /dishes/${dish_id}
    Status Should Be    200    ${res}
    Log Result    Delete Dish

Register User
    ${body}=    Create Dictionary    name=Anunay    email=anunay@test.com    password=123456
    ${res}=    POST On Session    foodie    /users/register    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads($res.text)
    Set Suite Variable    ${user_id}    ${json["id"]}
    Log Result    Register User

Duplicate User
    ${body}=    Create Dictionary    name=Anunay    email=anunay@test.com    password=123456
    ${res}=    POST On Session    foodie    /users/register    json=${body}    expected_status=409
    Status Should Be    409    ${res}
    Log Result    Duplicate User

Place Order
    ${body}=    Create Dictionary    user_id=${user_id}    restaurant_id=${restaurant_id}    dishes=[]
    ${res}=    POST On Session    foodie    /orders    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads($res.text)
    Set Suite Variable    ${order_id}    ${json["id"]}
    Log Result    Place Order

View Orders By User
    ${res}=    GET On Session    foodie    /users/${user_id}/orders
    Status Should Be    200    ${res}
    Log Result    View Orders By User

View Orders By Restaurant
    ${res}=    GET On Session    foodie    /restaurants/${restaurant_id}/orders
    Status Should Be    200    ${res}
    Log Result    View Orders By Restaurant

Give Rating
    ${body}=    Create Dictionary    order_id=${order_id}    rating=5    comment=Excellent
    ${res}=    POST On Session    foodie    /ratings    json=${body}
    Status Should Be    201    ${res}
    Log Result    Give Rating

Admin Approve Restaurant
    ${res}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${res}
    Log Result    Admin Approve Restaurant

Admin Disable Restaurant
    ${res}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/disable
    Status Should Be    200    ${res}
    Log Result    Admin Disable Restaurant

Admin View Orders
    ${res}=    GET On Session    foodie    /admin/orders
    Status Should Be    200    ${res}
    Log Result    Admin View Orders

*** Keywords ***

Log Result
    [Arguments]    ${name}
    Append To File    final_test_summary.txt    ${name} : PASSED\n

Finalize Execution
    Open Browser    http://127.0.0.1:5000/api/v1/admin/orders    chrome
    Capture Page Screenshot    final_screenshot_robot.png
    Close Browser
    ${html}=    Set Variable    <html><head><title>Robot Report</title><style>body{font-family:Arial;background:#f4f6f9;padding:20px;}h1{text-align:center;color:#2c3e50;}img{display:block;margin:30px auto;width:70%;border-radius:10px;}</style></head><body><h1>Foodie App Robot Automation Report</h1><h2 style="text-align:center;">Final Screenshot</h2><img src="final_screenshot_robot.png"></body></html>
    Create File    robot_final_report.html    ${html}
Setup Environment
    Create Session    foodie    http://127.0.0.1:5000/api/v1
    POST On Session    foodie    /reset
