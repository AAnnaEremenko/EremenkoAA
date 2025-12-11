def mask_account_card(user_type_and_number: str, mask_char: str = "*") -> str:
    """"Функция маскировки номера банковского счета или карты"""
    if user_type_and_number[0] == "С":
        mask_type_and_number = user_type_and_number[:4] + " " + mask_char * 2 + user_type_and_number[-4:]

    else:
        mask_type_and_number = user_type_and_number[:-12] + " " + user_type_and_number[-12:-10] + mask_char * 2 + " " + mask_char * 4 + " " + user_type_and_number[-4:]
    return mask_type_and_number


user_type_and_number = input("Введите тип и номер карты или счета: ")
print(mask_account_card(user_type_and_number))