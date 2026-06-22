import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from Diana_core_V1 import Core
import json

memory_file = "memory_main.json"
core = Core()

with open(memory_file, "r", encoding='utf-8') as f:
    data = json.load(f)
    
name = data["name"]

print(data["name"])

if len(name) == 0:
    name = input("Введи имя: ")
    data["name"] = name
    with open(memory_file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if name == "Мр. ДАК":
    print("Преветствую вас, создатель")
else:
    print(f"Привет {name}")
    

print()
# core.current_date_check(print)

def terminal():
    while core.terminal_running:
        print()
        if core.show_tultip:
            print("Что ты хочешь сделать?")
            print(f"Выбери один из: {core.list_of_options}")
            # print("Оставь пустым для пропуска фильтра")
        user = input(f"Диана: {core.system}, жду команды :> ")

        core.process(user, print)

    print("Хорошего тебе дня!")

terminal()

