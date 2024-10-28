import pandas as pd
from bs4 import BeautifulSoup

with open("DGVWSDG.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup)

table = soup.find("table", {"id": "orders"})

data = []

# print(table)
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    # print(columns)
    # print(' ')
    if len(columns) == 5:
        fio = str(columns[0]).split('<br/><br/>')[0][4:].split(' ')
        # print(fio)
        first_name = fio[1]
        last_name = fio[0]

        # print(len(fio) )
        partonimic = fio[2]

        registration_date = columns[1].text.strip()
        personal_data = columns[2].text.strip()
        discount = columns[3].text.strip()
        actions = columns[4].text.strip()
        # print(first_name)

        data.append({
            'Имя': first_name,
            'фамилия': last_name,
            "Отчество": partonimic,

            "Дата регистрации": registration_date,
            "Личные данные": personal_data,
            "Скидка": discount,
            "Действия": actions
        })

print(data)
name = []
last_name = []
for row in data:
    print(row['Имя'])
    name.append(row['Имя'])
    last_name.append(row['фамилия'])

name = pd.DataFrame({'Name': [*name], 'Last Name': [*last_name]})
salary_sheets = {'Group1': name}
writer = pd.ExcelWriter('./salaries.xlsx', engine='xlsxwriter')

for sheet_name in salary_sheets.keys():
    salary_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

writer._save()

# for item in data:
#     print(item)
