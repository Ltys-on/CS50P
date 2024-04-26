def main():

    while True:
        input_date = str(input("Date: "))
        date = output_date(input_date)
        if date:
            print(str(date))
            break


def output_date(input_date):
    valid_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    try:
        if input_date.find(",") != -1:
            text_date = input_date.replace(",", "").split(" ")
            day = int(text_date[1])
            for set_month in valid_months:
                if set_month == text_date[0]:
                    month = valid_months.index(set_month) + 1
                    break
            year = text_date[2]
        elif input_date.find("/") != -1:
            number_date = input_date.split("/")
            month = int(number_date[0])
            day = int(number_date[1])
            year = int(number_date[2])
        else:
            return None
    except (ValueError, IndexError):
        return None

    if month <= 12 and month >= 1 and day <= 31 and day >= 1:
        return f"{year}-{month:02}-{day:02}"


main()
