def send_email(message, recipient, *,  sender = "university.help@gmail.com"):
    variants = (".com", ".ru", ".net")
    if "@" not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com" and recipient.endswith(variants) and sender.endswith(variants):
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес "
            f"{recipient}")
    elif (recipient.endswith(variants) and sender.endswith(variants) and sender != recipient
          and sender == "university.help@gmail.com"):
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else: #recipient.endswith(variants) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')