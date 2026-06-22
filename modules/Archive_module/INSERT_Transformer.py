import random
import json


def hide(target: str, level: int, operation: str | None):
    with open("modules/Archive_module/archive.json", "r", encoding='utf-8') as f:
        keys = json.load(f)    

    if level == 1:
        if operation == None:
            key = random.choice(["◆", "◇", "●", "○"])
        else:
            key = operation

        result = ""
        for i in list(target):
            if i in keys[key].keys():
                result += keys[key][i]
            else:
                result += i

        result = key + result

        return result
        

    elif level == 2:
        b = random.randint(1,3)
        list_of_operations = []
        for i in range(b):
            list_of_operations.append(random.choice(["◆", "◇", "●", "○"]))
        for operation in list_of_operations:
            target = hide(target, 1, operation)
        
        if b == 1:
            target = "1" + target
        elif b == 2:
            target = "2" + target
        else:
            target = "3" + target

    elif level == 3:
        c = random.choice(["s", "e"])
        target = hide(target, 1, None)
        a = target[0]
        target = target[1::]

        if c == "s":
            target = "s" + a + target
        
        elif c == "e":
            target = "e" + target + a[::-1]
    
    else:
        c = random.choice(["s", "e"])
        target = hide(target, 2, None)
        a = target[0]

        if a == "1":
            a = target[0:2]
            target = target[2:]

        elif a == "2":
            a = target[0:3]
            target = target[3:]

        elif a == "3":
            a = target[0:4]
            target = target[4:]

        if c == "s":
            target = "s" + a + target
        
        elif c == "e":
            target = "e" + target + a[::-1]

    return target

# # переменные
# user = "Omega"
# table_name = "Дневник 1"
# columns = ["Дата", "Заметки", "Оценка"]
# for_processing = []
# result = ""

# # Инпут
# while len(user) > 0:
#     user = input("Вводи данные построчно и оставь пустым чтобы закончить: ")
#     for_processing.append(list(user.split("\t")))

# for_processing.pop(-1)

# # Просвет того что на обработку
# # print(for_processing)

# print()
# print()

# # Обработка
# print(f"INSERT INTO `{table_name}` ({columns[0]}, {columns[1]}, {columns[2]})")
# print("VALUES")
# for i in for_processing:
#     # Переводим дату в нужный формат
#     m = i[0].split(".")
#     m.reverse()
#     i[0] = "-".join(m)

#     print(f"('{i[0]}', '{hide(i[1], 2, None)}', '{hide(i[2], 2, None)}'),")


# SELECT Id, Автор, Название, Прогресс, Статус, Описание, `Отработано в мире два?`, Ссылка, `Время просмотра` FROM `Просмтренно до переезда в польшу`
# UNION
# SELECT Id, Автор, Название, Прогресс, Статус, Описание, `Отработано в мире два?`, Ссылка, `Время просмотра` FROM `Архивация 1` 
# Order by Id ASC
# Для вывода (название чтобы не писать)

# CREATE TABLE "Просмтренно до переезда в польшу" (
# 	"Id"	INTEGER UNIQUE,
# 	"Автор"	TEXT,
# 	"Название"	TEXT,
# 	"Прогресс"	TEXT,
# 	"Статус"	TEXT,
# 	"Описание"	TEXT,
# 	"Отработано в мире два?"	TEXT,
# 	"Ссылка"	TEXT,
# 	"Время просмотра"	TEXT,
# 	PRIMARY KEY("Id" AUTOINCREMENT)
# )