import csv
import random
import xml.etree.ElementTree as ET

def process_csv():
    filename = "books.csv"

    with open(filename, encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=';')
        books = list(reader)

    long_titles = [b for b in books if len(b["Название"]) > 30]
    print("Книг с названием > 30 символов:", len(long_titles))

    author_input = input("\nВведите автора для поиска: ")

    filtered = []

    for b in books:
       price = b["Цена поступления"]

       if price.strip() == "":
        continue

       try:
         price = float(price)
       except:
        continue

       if author_input.lower() in b["Автор"].lower() and price <= 200:
        filtered.append(b)

    print("\nРезультаты поиска (цена <= 200):")
    for b in filtered:
        print(f'{b["Автор"]} | {b["Название"]} | {b["Цена поступления"]}')

    random_books = random.sample(books, 20)

    with open("result.txt", "w", encoding="utf-8") as out:
        for i, b in enumerate(random_books, 1):
            year = b["Дата поступления"][-4:]
            line = f"{i}. {b['Автор']}. {b['Название']} – {year}"
            out.write(line + "\n")

    print("\nФайл result.txt создан.")



def process_xml():
    tree = ET.parse("currency.xml")
    root = tree.getroot()

    currency_dict = {}

    for valute in root.findall("Valute"):
        num_code = valute.find("NumCode").text
        char_code = valute.find("CharCode").text
        currency_dict[num_code] = char_code

    print("\nСловарь NumCode - CharCode:")
    print(currency_dict)


def main():
    process_csv()
    process_xml()


if __name__ == "__main__":
    main()