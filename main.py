def mask_account_card(user_type_and_number: str) -> str:
    """ "Функция маскировки номера банковского счета или карты"""
    if user_type_and_number[0] == "С":
        account_number = user_type_and_number[5:]
        mask_type_and_number = user_type_and_number[:4] + " "

    else:
        account_number = user_type_and_number[-16:]
        mask_type_and_number = user_type_and_number[:-16]
    return mask_type_and_number


def get_date(user_date: str) -> str:
    """Функция корректировки формата даты"""
    correct_date = user_date[8:10] + "." + user_date[5:7] + "." + user_date[:4]
    return correct_date