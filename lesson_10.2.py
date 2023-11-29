# with open("lesson_10.2.py") as file:
#     str1 = file.readlines()
# print(str1)
# slovar = {"id":23234, "text":"Hello"}
import json
# file_name = "file.json"
# mid_or_feed = {
#     "fio":"Мажитов",
#     "ocenci":{
#         "matan":4,
#         "russind language":4,
#         "biologi":4,
#     },
#     "hobi":["игры", "питбайки"],
#     "vozrast":13,
#     "frends":{
#         "sana":{
#             "hobi":["рисовать", "ролить"],
#             "vozrast":14
#         },
#         "temur":{
#             "hobi":["дота","фид"],
#             "vozrast":14
#         }
#
#     }
# }
# with open(file_name,"w",encoding="utf-8")as file:
#     file.write(json.dumps(mid_or_feed, ensure_ascii=False, indent=4))
import csv
file_name = "uliana.csv"
shoplist = {"manderin":[2, 100], "яблоки":[4, 250], "клубника":[8, 500]}
with open(file_name, "w", encoding="utf-8", newline="")as file:
    writer = csv.DictWriter(file, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1]))
rows = []
with open(file_name, "r", encoding="utf-8")as file:
    reader = csv.DictReader(file)
    rows = list(reader)
for row in rows:
    print(row)