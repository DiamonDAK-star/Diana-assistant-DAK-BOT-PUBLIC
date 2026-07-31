import json

def subject_avg (subject):
    total_sum = 0
    total_weight = 0

    with open("modules/School_module/memory_school.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    grades_test = data["school_rates"][subject]
    if len(grades_test) > 1:
        grades_list = list(data["school_rates"][subject].split("+")) 
        for i in grades_list:
            value, weight = i.split("*")
            total_sum += float(value) * int(weight)
            total_weight += int(weight)

        avg = total_sum / total_weight
        return round(avg, 2) 
    else:
        return 0

def all_avg ():
    global_sum = 0
    global_weight = 0
    with open("modules/School_module/memory_school.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    subjects = data["school_rates"]
    for i in subjects:
        if len(subjects[i]) > 1:
            total_sum = 0
            total_weight = 0
            grades_list = list(data["school_rates"][i].split("+")) 
            for i in grades_list:
                value, weight = i.split("*")
                total_sum += float(value) * int(weight)
                total_weight += int(weight)
                global_sum += total_sum
                global_weight += total_weight

    if global_weight > 0:
        final_avg = global_sum / global_weight
    else:
        final_avg = 0

    result = []

    result.append(("╔════════════════════════════╗"))
    result.append((f"║ Общяя средняя оценка: {final_avg:.2f} ║"))
    result.append(("╚════════════════════════════╝"))
    if final_avg > 4.75:
        result.append(("Очень хорошо, ты молодец!"))
    
    return result

def grades():
    with open("modules/School_module/memory_school.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    result = []

    subjects = data["school_rates"]
    result.append(("╔"+"═"*47+"╦"+"═"*65+"╦"+"═"*12+"╗"))
    result.append(("║"+" "*20+"Предмет"+" "*20+"║"+" "*30+"Оценки"+" "*29+"║"+"  Средняя   "+"║"))
    # показ предмета
    for i in subjects:
        a = subjects[i].replace("+", "  ")
        result.append((f"║ {i:<45} ║ {a:<63} ║ {subject_avg(i):<10} ║"))
    result.append(("╚"+"═"*47+"╩"+"═"*65+"╩"+"═"*12+"╝"))

    return result

def help(language):
    helping = {}
    if language == "ru":
        helping = {
            "помощь":"для показа этого текста",
            "оценки" : "для показа оценок",
            # "статусы" : "для показа статусов по предметам",
            "средний бал" : "для показа среднего бала по всем оценкам",
            "выход":"для выхода из модуля"
        }
    elif language == "en":
        helping = {
            "help": "to show this text",
            "grades": "to show grades",
            "average grade": "to show the average grade for all grades",
            "exit": "to exit the module"
        }
    elif language == "pl":
        helping = {
            "pomoc": "aby wyświetlić ten tekst",
            "wyniki": "aby wyświetlić oceny",
            "średni wynik": "aby wyświetlić średnią ocen ze wszystkich ocen",
            "wyjscie": "aby wyjść z modułu"
        } 

    return helping