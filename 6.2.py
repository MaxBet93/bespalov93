def main():
    try:
        user_input = int(input("Введіть кількість секунд (0 - 8640000): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return
    if user_input < 0 or user_input >= 8640000:
        print("Число має бути більше або дорівнює 0 і менше ніж 8640000.")
        return

    SEC_IN_MIN = 60
    SEC_IN_HOUR = 60 * 60
    SEC_IN_DAY = 24 * 60 * 60


    days, remaining_seconds = divmod(user_input, SEC_IN_DAY)
    hours, remaining_seconds = divmod(remaining_seconds, SEC_IN_HOUR)
    minutes, seconds = divmod(remaining_seconds, SEC_IN_MIN)

    day_word = ""
    last_digit = days % 10
    last_two_digits = days % 100

    if 11 <= last_two_digits <= 14:
        day_word = "днів"
    elif last_digit == 1:
        day_word = "день"
    elif 2 <= last_digit <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    h_str = str(hours).zfill(2)
    m_str = str(minutes).zfill(2)
    s_str = str(seconds).zfill(2)

    print(f"{days} {day_word}, {h_str}:{m_str}:{s_str}")


if __name__ == "__main__":
    main()