import requests


def get_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    return response.json()


def save_to_file(data, date, filename):
    with open(filename, "w") as file:
        file.write(f"[Date for course]: {date}\n")
        for currency in data:
            name = currency["txt"]
            rate = currency["rate"]
            file.write(f"{name} to UAH: {rate}\n")


data = get_exchange_rates()
date = "2023-11-07"
filename = "exchange.txt"
save_to_file(data, date, filename)
