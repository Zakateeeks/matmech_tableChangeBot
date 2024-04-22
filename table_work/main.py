from openpyxl import load_workbook

"""
A - номер
B - ФИО
C - айдишка
D - Скип
E - приоритеты
F - направления
G - фиг пойми что 
H - Институты
I - бюджет или контракт
J - Баллы за ЕГЭ
K - Баллы + допы
L - Комментарий
"""
wb = load_workbook('./test.xlsx')
sheet = wb['Sheet1']
numb = 1
letters = ["B","C","E","F","I","K","L"]
for letter in letters:
    if sheet[f"{letter}{numb}"].value != "":
        print(sheet[f"{letter}{numb}"].value)
        
