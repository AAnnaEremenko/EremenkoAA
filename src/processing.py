def filter_by_state(data_list: list, x: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    sorted_data_list = []
    for data in data_list:
        if data["state"] == x:
            sorted_data_list.append(data)
        else:
            continue
    return sorted_data_list


data_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(data_list))

# def sort_by_date(client_data: list, direction = True: bool) -> list:
# """Функция сортирует входящий список по дате (date) и возвращает новый отсортированный список."""
