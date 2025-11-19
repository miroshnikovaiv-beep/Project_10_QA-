from sender_stand_request import post_new_user, post_new_client_kit
import data 

def get_user_body(first_name):
    
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    
    return current_body 

def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    token = get_new_user_token()
    resp = post_new_client_kit(kit_body, token)

    assert resp.status_code == 201
    assert resp.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    resp = post_new_client_kit(kit_body, token)

    assert resp.status_code == 400
    
# Тест 1. Допустимое количество символов (1):
def test_kit_name_1_symbol():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)
    

# Тест 2. Допустимое количество символов (511):
def test_kit_name_511_symbol():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

# Тест 3. Ошибка
# Количество символов меньше допустимого (0):
def test_kit_name_0_symbol():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

 # Тест 4. Ошибка
 # Количество символов больше допустимого (512):   
def test_kit_name_512_symbol():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Тест 5. Разрешены английские буквы (QWErty):   
def test_kit_name_english_letter_symbol():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

# Тест 6. Разрешены русские буквы("Мария"):
def test_kit_name_russian_symbol():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

# Тест 7. Разрешены спецсимволы("№%@"):
def test_kit_name_has_special_symbol_symbol():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

# Тест 8. Разрешены пробелы("Человек и КО"):
def test_kit_name_has_space_symbol():
    kit_body = get_kit_body("Человек и КО")
    positive_assert(kit_body)

# Тест 9. Разрешены цифры:
def test_kit_name_number_symbol():
    kit_body = data.kit_body.copy()
    positive_assert(kit_body)

# Тест 10. Ошибка
# Параметр не передан в запросе:
def test_kit_name_no_symbol():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Тест 11. Ошибка
 # Передан другой тип параметра (число):
def test_kit_name_number_type_symbol():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
    
