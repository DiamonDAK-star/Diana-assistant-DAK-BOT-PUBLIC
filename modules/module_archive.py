import sqlite3
import json

def reveal(target: str):
    with open("modules/Archive_module/archive.json", "r", encoding='utf-8') as f:
        keys = json.load(f)
    
    # Определяем уровень маскировки
    # 1 уровень
    if target[0] in ["◆", "◇", "●", "○"]:
        # Декодируем

        key = target[0]
        target = target[1:]

        reverse_key = {v: k for k, v in keys[key].items()}
        result = ""

        for i in list(target):
            if i in reverse_key:
                result += reverse_key[i]
            else:
                result += i
                
        return result

    # 2 уровень
    elif target[0] in ["1", "2", "3"]:
        a = 0
        if target[0] == "1":
            a = 1
        elif target[0] == "2":
            a = 2
        elif target[0] == "3":
            a = 3
        target = target[1:]
        for i in range(a):
            target = reveal(target)
        return target

    # 3 и 4 уровни
    else:
        if target[0] == "s":
            if target[1] in ["◆", "◇", "●", "○"]:
                target = reveal(target[1:])
            else:
                # 4 уровень
                target = reveal(target[1:])
                # target = target[2:]
        
        elif target[0] == "e":
            if target[-1] in ["◆", "◇", "●", "○"]:
                a = target[-1]
                target = target[1:-1]
            else:
                m = (int(target[-1])*-1)-1
                a = target[m:][::-1]
                target = target[1:m]

            target = a + target
            target = reveal(target)
       
        return target   

def show_watched(tables_names: list[str]):
    conn = sqlite3.connect("modules/Archive_module/archive.db")
    cursor = conn.cursor()
    command_placeholder = "SELECT Автор, Название, Прогресс, Статус, Описание, `Отработано в мире два?`, Ссылка FROM "
    command = command_placeholder
    if len(tables_names) > 1:
        for i in range(len(tables_names)-1):
            command += tables_names[i]
            command += " UNION "
            command += command_placeholder
        command += tables_names[-1]
    else:
        command += tables_names[0]

    cursor.execute(command)

    result = []
    # Вывод
    result.append("╔"+"═"*25+"╦"+"═"*30+"╦"+"═"*10+"╦"+"═"*14+"╦"+"═"*65+"╦"+"═"*24+"╦"+"═"*19+"╗")
    result.append(f"‖{'Автор':^25}"+f"‖{'Название':^30}"+f"‖{'Прогресс':^10}"+f"‖{'Статус':^14}"+f"‖{'Описание':^65}"+f"‖{'Отработано в мире два?':^24}"+f"‖{'Ссылка':^19}‖")
    for i in cursor.fetchall():
        result.append(f"‖{i[0]:<25.25}‖{i[1]:<30.30}‖{i[2]:<10.10}‖{i[3]:<14.14}‖{i[4]:<65.65}‖{i[5]:<24.24}‖                   ‖") #i[6]
    result.append("╚"+"═"*25+"╩"+"═"*30+"╩"+"═"*10+"╩"+"═"*80+"╩"+"═"*24+"╩"+"═"*19+"╝")
    conn.close()

    return result

def show_watched_time(tables):
    result = 0
    conn = sqlite3.connect("modules/Archive_module/archive.db")
    cursor = conn.cursor()

    for table in tables:
        cursor.execute(f"SELECT `Время просмотра` FROM '{table}'")
        for item in cursor.fetchall():
            if "+" in item[0]:
                splited = list(item[0].split("+"))
                splited = sum(map(int, splited))
                result += splited 
            elif item[0].isdigit() == False:
                pass
            else:
                result += int(item[0])
    return f"Время просмотра: {result//60} часов {result%60} минут"

def serial_progress():
    with open("modules/Archive_module/archive.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    serials = data["serial_progress"]
    result = []

    for serial in serials:
        result.append(f"{serial['name']}: {serial['season']:0>2} сезон {serial['episode']:0>2} серия {serial['link']}")

    return result

def codes(pas):
    from modules.Archive_module.INSERT_Transformer import hide
    m = hide(pas,1,"○")
    if m == "○о86эd0zвu":
        with open("modules/Archive_module/archive.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        codes = data["pass"]

        result = []
        for i in codes:
            n = i["target"]
            if len(n) > 0: n = reveal(n)
            m = i["log"]
            if len(m) > 0: m = reveal(m)
            l = i["pass"]
            if len(l) > 0: l = reveal(l)
        
            result.append(" ")
            result.append("Цель: "+n)
            result.append("Логин: "+m)
            result.append("Пароль: "+l)


        return result
    
    else:
        return "Пароль не принят"

def help(language):
    helping = {}
    if language == "ru":
        helping = {
            "помощь":"для показа этого текста",
            "просмотренно": "Показыват данные из таблиц просмотренных видео (она не полностью доставерна но что есть)",  
            "сериалы": "Показывает прогресс по просмотру сериалов",
            "пароли":"Показывает пароли от бесплатных сервисов",
            "цели":"цели на жизнь",
            "выход": "выход из модуля"
        }
    elif language == "en":
        helping = {
            "help": "to display this text",
            "watched": "Shows data from tables of watched videos (it's not completely reliable, but it's what it is)",
            "series": "Shows your progress in watching series",
            "passwords": "Shows passwords for free services",
            "goals": "shows goals for life of author",
            "exit": "exit the module"
        }
    elif language == "pl":
        helping = {
            "pomoc": "aby wyświetlić ten tekst",
            "ogladane": "Pokazuje dane z tabeli obejrzanych filmów (nie są one w pełni wiarygodne, ale takie już są)",
            "serialy": "Pokazuje postępy w oglądaniu seriali",
            "hasla": "Pokazuje hasła do bezpłatnych usług",
            "cele": "Pokazuje cele życiowe autora",
            "wyjscie": "aby wyjść z modułu"
        }             
    return helping

# show_watched(["Бесконечные"])
# show_watched("Просмотренно до переезда в польшу")
# show_watched("Архивация 1")
# show_watched("Просмотренно майнкрафт")

# show_watched_time(["Бесконечные", "Просмотренно до переезда в польшу", "Архивация 1", "Просмотренно майнкрафт"])