import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5000/api/v1"

restaurant_id = None
user_id = None
order_id = None
dish_id = None

passed_tests = []

def log_test(name):
    passed_tests.append(name)

def generate_summary():
    with open("final_test_summary.txt", "w") as f:
        for test in passed_tests:
            f.write(f"{test} : PASSED\n")

def take_final_screenshot():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"{BASE_URL}/admin/orders")
    driver.save_screenshot("final_screenshot_test.png")
    driver.quit()

def generate_html_report():
    html = """
    <html>
    <head>
    <title>Final Report</title>
    <style>
    body{font-family:Arial;background:#f4f6f9;padding:20px;}
    h1{text-align:center;color:#2c3e50;}
    table{width:80%;margin:auto;border-collapse:collapse;background:white;}
    th,td{padding:10px;border:1px solid #ddd;text-align:center;}
    th{background:#2c3e50;color:white;}
    .pass{color:green;font-weight:bold;}
    img{display:block;margin:30px auto;width:70%;border-radius:10px;}
    </style>
    </head>
    <body>
    <h1>Foodie App Automation Report</h1>
    <table>
    <tr><th>Test Case</th><th>Status</th></tr>
    """
    for test in passed_tests:
        html += f"<tr><td>{test}</td><td class='pass'>PASSED</td></tr>"
    html += """
    </table>
    <h2 style='text-align:center;'>Final Screenshot</h2>
    <img src='final_screenshot_test.png'>
    </body>
    </html>
    """
    with open("final_report.html", "w") as f:
        f.write(html)

def test_01_register_restaurant():
    global restaurant_id
    data = {"name":"Food Hub","category":"Veg","location":"Delhi","images":["img1.jpg"],"contact":"9999999999"}
    r = requests.post(f"{BASE_URL}/restaurants", json=data)
    assert r.status_code == 201
    restaurant_id = r.json()["id"]
    log_test("test_01_register_restaurant")

def test_02_duplicate_restaurant():
    data = {"name":"Food Hub","category":"Veg","location":"Delhi","images":["img1.jpg"],"contact":"9999999999"}
    r = requests.post(f"{BASE_URL}/restaurants", json=data)
    assert r.status_code == 409
    log_test("test_02_duplicate_restaurant")

def test_03_view_restaurant():
    r = requests.get(f"{BASE_URL}/restaurants/{restaurant_id}")
    assert r.status_code == 200
    log_test("test_03_view_restaurant")

def test_04_update_restaurant():
    r = requests.put(f"{BASE_URL}/restaurants/{restaurant_id}", json={"location":"Mumbai"})
    assert r.status_code == 200
    log_test("test_04_update_restaurant")

def test_05_disable_restaurant():
    r = requests.put(f"{BASE_URL}/restaurants/{restaurant_id}/disable")
    assert r.status_code == 200
    log_test("test_05_disable_restaurant")

def test_06_add_dish():
    global dish_id
    data = {"name":"Pizza","type":"Veg","price":250,"available_time":"10AM-10PM","image":"pizza.jpg"}
    r = requests.post(f"{BASE_URL}/restaurants/{restaurant_id}/dishes", json=data)
    assert r.status_code == 201
    dish_id = r.json()["id"]
    log_test("test_06_add_dish")

def test_07_update_dish():
    r = requests.put(f"{BASE_URL}/dishes/{dish_id}", json={"price":300})
    assert r.status_code == 200
    log_test("test_07_update_dish")

def test_08_toggle_dish_status():
    r = requests.put(f"{BASE_URL}/dishes/{dish_id}/status", json={"enabled":False})
    assert r.status_code == 200
    log_test("test_08_toggle_dish_status")

def test_09_delete_dish():
    r = requests.delete(f"{BASE_URL}/dishes/{dish_id}")
    assert r.status_code == 200
    log_test("test_09_delete_dish")

def test_10_user_registration():
    global user_id
    data = {"name":"Harsh","email":"harsh@test.com","password":"123456"}
    r = requests.post(f"{BASE_URL}/users/register", json=data)
    assert r.status_code == 201
    user_id = r.json()["id"]
    log_test("test_10_user_registration")

def test_11_duplicate_user():
    data = {"name":"Harsh","email":"harsh@test.com","password":"123456"}
    r = requests.post(f"{BASE_URL}/users/register", json=data)
    assert r.status_code == 409
    log_test("test_11_duplicate_user")

def test_12_place_order():
    global order_id
    data = {"user_id":user_id,"restaurant_id":restaurant_id,"dishes":[]}
    r = requests.post(f"{BASE_URL}/orders", json=data)
    assert r.status_code == 201
    order_id = r.json()["id"]
    log_test("test_12_place_order")

def test_13_view_user_orders():
    r = requests.get(f"{BASE_URL}/users/{user_id}/orders")
    assert r.status_code == 200
    log_test("test_13_view_user_orders")

def test_14_view_restaurant_orders():
    r = requests.get(f"{BASE_URL}/restaurants/{restaurant_id}/orders")
    assert r.status_code == 200
    log_test("test_14_view_restaurant_orders")

def test_15_give_rating():
    data = {"order_id":order_id,"rating":5,"comment":"Excellent"}
    r = requests.post(f"{BASE_URL}/ratings", json=data)
    assert r.status_code == 201
    log_test("test_15_give_rating")

def test_16_admin_approve_restaurant():
    r = requests.put(f"{BASE_URL}/admin/restaurants/{restaurant_id}/approve")
    assert r.status_code == 200
    log_test("test_16_admin_approve_restaurant")

def test_17_admin_disable_restaurant():
    r = requests.put(f"{BASE_URL}/admin/restaurants/{restaurant_id}/disable")
    assert r.status_code == 200
    log_test("test_17_admin_disable_restaurant")

def test_18_admin_view_orders():
    r = requests.get(f"{BASE_URL}/admin/orders")
    assert r.status_code == 200
    log_test("test_18_admin_view_orders")
    generate_summary()
    take_final_screenshot()
    generate_html_report()