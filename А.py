from bs4 import BeautifulSoup

with open("DGVWSDG.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup)

table = soup.find("table", {"id": "orders"})

data = []

print(table)
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    # print(columns)
    # print(' ')
    if len(columns) == 5:
        fio = str(columns[0]).split('<br/><br/>')[0][4:].split(' ')
        print(fio)
        first_name = fio[1]
        last_name = fio[0]


        print(len(fio) )

        # if len( columns[0].text.strip().split(' ')) == 3:
        partonimic  =fio[2]

        registration_date = columns[1].text.strip()
        personal_data = columns[2].text.strip()
        discount = columns[3].text.strip()
        actions = columns[4].text.strip()

        data.append({
            'Имя': first_name,
                'фамилия': last_name,
            "Отчество": partonimic,

            "Дата регистрации": registration_date,
            "Личные данные": personal_data,
            "Скидка": discount,
            "Действия": actions
        })

for item in data:
    print(item)
