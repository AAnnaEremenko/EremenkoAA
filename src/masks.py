def get_mask_card_number(user_card_number: str, mask_char: str = "*") -> str:
    """Функция маскировки номера банковской карты"""
    card_number = user_card_number[:6] + mask_char * (6) + user_card_number[12:]
    mask_card_number = card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
    return mask_card_number


def get_mask_account(user_account: str, mask_char: str = "*") -> str:
    """Функция маскировки номера банковского счета"""
    mask_user_account = mask_char * 2 + user_account[-4:]
    return mask_user_account


user_card_number = input("Введите номер карты: ")

print(get_mask_card_number(user_card_number))

user_account = input("Введите номер счета: ")

print(get_mask_account(user_account))
