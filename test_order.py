# Магафурова Юлия, когорта 8а - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def test_create_order_and_get_order():

    response = sender_stand_request.post_new_order(data.order_body)

    # Проверка запроса по созданию заказа
    assert response.status_code == 201
    order_info = response.json()
    # print('response::create order_order_info ')
    # print(order_info)
    order_track = order_info.get("track")

    # Выполнить запрос на получение  заказа по треку заказа
    get_order_response = sender_stand_request.get_order_by_track(order_track)
    # print('response::get order by track')
    # print(get_order_response.json())
    assert get_order_response.status_code == 200
