from deep_translator import GoogleTranslator
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

def output(*targets):
    translator = GoogleTranslator(source='ru', target=core.language)
    for target in targets:
        if isinstance(target, str):
            print(translator.translate(target))
        elif isinstance(target, (list, tuple)):
            for line in target:
                if line != None:
                    print(translator.translate(line))
                else:
                    print()
        elif isinstance(target, dict):
            print()

def terminal():
    while core.terminal_running:
        print()
        if core.show_tultip:
            if core.language == "en":
                print("What do you want to do?")
                print(f"Choose one of: {core.trn_list_of_options}")         
            elif core.language == "pl":
                print("Co ty chiecsz zrobic?")
                print(f"Wybierz jedno z {core.trn_list_of_options}")     
            elif core.language == "ru":
                print("Что ты хочешь сделать?")
                print(f"Выбери один из: {core.trn_list_of_options}")

        user = "alfa-state"
        if core.language == "en":
            user = input(f"Diana: {core.system}, waiting for command :> ")
        elif core.language == "pl":
            user = input(f"Diana: {core.system}, czekam na polecenie :> ")
        elif core.language == "ru":
            user = input(f"Диана: {core.system}, жду команды :> ")

        user = GoogleTranslator(source=core.language, target='ru').translate(user)
        print(user)
        core.process(user, output)

    print("Хорошего тебе дня!")

terminal()

