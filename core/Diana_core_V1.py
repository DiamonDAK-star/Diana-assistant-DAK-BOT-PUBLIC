import time
import random
import json
import ctypes 
import importlib
import webbrowser
from datetime import datetime
# Для терминала:
# import sys
# from pathlib import Path
from deep_translator import GoogleTranslator
# Для Insert transformer
# import random
# import json
# Для архива
# import sqlite3
# import json
# Для майнкрафт модуля
# import json
# from PIL import Image
# Для школьного модуля


memory_file = "core/memory_main.json"
with open(memory_file, "r", encoding='utf-8') as f:
    data = json.load(f)

class Core:
    def __init__(self):
        self.language = "en"
        self.autotranslation = True
        with open("core/translations.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.translations = data[self.language]
        self.system = "main"
        # self.core_running = True
        # # Нахрена вообще останавливать ядро?
        self.terminal_running = True
        # Отсановка терминала - закрытие Дианы
        self.GUI_running = False
        # В GUI будет кнопка назад которая поставит это обратно в False
        # И также можно для асиста или голоса сделать

        # Ввод:
        self.input_state = "choise"
        self.show_tultip = True
        self.user_choise = ""
        self.user_sub_choise = ""
        self.user_input = ""
        # input_state может быть "choise" / "sub choise" / "any input"
        # Помощь
        self.helping = self.translations["helping"]
        # "даты":"показывает важные даты",
        # "дела": "для показа списка дел"
        self.list_of_options = list(self.helping.keys())
        self.temp = ["0","1","2","3"]
        self.sub_fill_status = 0
        self.cleaning = True

        # Нужен для очистки всех переменных
        # Если поставить в True то все переменные очистятся и оно снова станет False
        
        
    def back(self):
        self.cleaning = True
        self.sub_fill_status = 0
        self.input_state = "choise"
        self.temp = ["0","1","2","3"]
        try:
            self.list_of_options = list(self.current_module.help(self.language).keys())
        except AttributeError:
            self.list_of_options = list(self.helping.keys())

        
    def load_module(self, module, log, output):
        if log:
            output(self.translations["moduleloading"]["module_loading"])
        try:
            module = importlib.import_module(f"modules.{module}")
            if log:
                output(str(module)+ self.translations["moduleloading"]["module_loaded"])
            return module
        except ModuleNotFoundError:
            # if log:
            output(self.translations["moduleloading"]["module_loading_error"] + str(module))
            return False

    def current_date_check(self, output):
        today = datetime.today()
        dates = data["dates"]
        check = True
        for i in dates:
            if (today.day == i[0]) and (today.month == i[1]):
                output(f"Сегодня {i}")
                check = False

        if check:
            output(self.translations["normal_day"])

    def process(self, user, output):
        user = user.lower()
        if self.input_state in ["choise", "sub choise"]:

            if user in self.list_of_options:

                if self.input_state == "choise":
                    self.user_choise = user

                    if self.cleaning:
                       self.user_sub_choise = "" 
                       self.cleaning = False
                else:
                    self.user_sub_choise = user

                    if self.cleaning:
                       self.user_sub_choise = "" 
                       self.cleaning = False
                
            else:
                output(self.translations["no_such_option"])
                return

        elif self.input_state == "any input" and len(user) > 0:
            self.user_input = user

        elif len(user) == 0:
            user = "any"

        else:
            output(self.translations["input_state_error"])
            self.input_state = "choise"
            return

        if self.system == "main":

            # Входы в модули
            if self.user_choise in ["майнкрафт", "minecraft", "minecraft"]:
                module = self.load_module("module_minectaft", True, output)

                if module != False:
                    self.system = "Minecraft"
                    self.current_module = module
                    self.list_of_options = list(self.current_module.help(self.language).keys())

            elif self.user_choise in ["техникум", "technikum", "technikum"]:
                module = self.load_module("module_school", True, output)

                if module != False:
                    self.system = "School"
                    self.current_module = module
                    self.list_of_options = list(self.current_module.help(self.language).keys())
            
            elif self.user_choise in ["архив", "archive", "archive"]:
                module = self.load_module("module_archive", True, output)

                if module != False:
                    self.system = "Archive"
                    self.current_module = module     
                    self.list_of_options = list(self.current_module.help(self.language).keys())

            # обычные команды
            elif self.user_choise in ["помощь", "help", "pomoc"]:
                output("")
                for i in self.helping:
                    output(f"{i} : {self.helping[i]}")

            elif self.user_choise in ["языки", "languages", "jezyki"]:
                output(self.translations["main_functions"]["translation"]["what_language"])
                if self.input_state == "choise":
                    self.list_of_options = ["en","pl","ru","назад"]
                    self.input_state = "sub choise"
                    return
                else:
                    output("")
                    if self.user_sub_choise == self.language:
                        output(self.translations["main_functions"]["translation"]["language_already_chosen"])
                    elif self.user_sub_choise == "назад":
                        self.back()
                    else:
                        self.language = self.user_sub_choise
                        output(self.translations["main_functions"]["translation"]["language_changed"] + self.language) 
                        self.list_of_options = list(self.helping.keys())
                        self.back()

            elif self.user_choise in ["автоперевод", "autotranslate", "autotlumaczenie"]:
                self.autotranslation = not(self.autotranslation) 
                if self.autotranslation:
                    output(self.translations["main_functions"]["translation"]["autotlanslation_set"] + "Active")
                else:
                    output(self.translations["main_functions"]["translation"]["autotlanslation_set"] + "Inactive")

            elif self.user_choise in ["заметки", "notes", "notatki"]:
                with open("memory_main.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    
                notes = data["notes"]

                output(self.translations["main_functions"]["what_note"])
                if self.input_state == "choise":
                    self.list_of_options = ["заметка 1","заметка 2","заметка 3","назад"]
                    self.input_state = "sub choise"
                    return
                else:
                    output("")
                    if self.user_sub_choise == "заметка 1":
                        
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in notes["note1"]:
                                output(translator.translate(str(i)))
                        else:
                            for i in notes["note1"]:
                                output(i) 
                    elif self.user_sub_choise == "заметка 2":
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in notes["note2"]:
                                output(translator.translate(str(i)))
                        else:
                            for i in notes["note2"]:
                                output(i) 
                    elif self.user_sub_choise == "заметка 3":
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in notes["note3"]:
                                output(translator.translate(str(i)))
                        else:
                            for i in notes["note3"]:
                                output(i) 

                    elif self.user_sub_choise == "назад":
                        self.back()

            elif self.user_choise in ["даты", "dates", "daty"]:
                with open("memory_main.json", "r", encoding="utf-8") as f:
                    data = json.load(f)

                dates = data["dates"]
                for i in dates:
                    output(f"{i}: {dates[i][0]:0>2}.{dates[i][1]:0>2}")

            # elif self.user_input =="список дел":
            #     # with open("memory_main.json", "r", encoding="utf-8") as f:
            #     #     data = json.load(f)

            #     # a = data[""]
            #     # b = data["tasks_for_later"]
            #     list_of_tasks =  data["tasks_for_later"]
            #     for i in list_of_tasks:
            #         output(list_of_tasks[i])

            elif self.user_choise in ["монета", "coin", "moneta"]:
                output("")
                if random.randint(1, 2) == 1:
                    output(self.translations["main_functions"]["head"])
                else:
                    output(self.translations["main_functions"]["tail"])

            elif self.user_choise in ["анекдот", "joke", "zart"]:
                module = self.load_module("module_archive", True, output)

                if module != False:
                    self.system = "Archive"
                    self.current_module = module  
                    
                    with open("memory_main.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    joke = random.choice(data["jokes"])
                    output("")
                    output(self.current_module.reveal(joke))

                    self.system = "main"

                else:
                    output(self.translations["main_functions"]["decode_error"])

            elif self.user_choise in ["курсор", "cursor", "kursor"]:
                # курсоры устанавливаются в порядке: Основной режим, фоновый режим, переместить, выбор ссылки
                if random.randint(1,2) == 1:
                    cursors = ["modules/cursors/Arrow.cur", "modules/cursors/Wait.ani", "modules/cursors/SizeAll.ani", "modules/cursors/Help.ani"]
                else:
                    cursors = ["modules/cursors/standart-Select.cur", "modules/cursors/Working-in-Background.ani", "modules/cursors/Mover.cur", "modules/cursors/Link-Select.ani"]

                # Что мы меняем:
                changing_places = [32512, 32650, 32646, 32649]

                for i in range(len(changing_places)):
                    new_cursor = ctypes.windll.user32.LoadCursorFromFileW(cursors[i]) 
                    ctypes.windll.user32.SetSystemCursor(new_cursor, changing_places[i])

                output(self.translations["main_functions"]["cursor_changed"])
                output("")

            elif self.user_choise in ["выход", "exit", "wyjście"]:
                self.terminal_running = False
                output(self.translations["core_stoping"])
                time.sleep(1)
                output(self.translations["exiting"])

            elif self.user_choise == "any":
                output("ㄟ(≧◇≦)ㄏ")

        elif self.system == "Minecraft":

            if self.user_choise in ["помощь", "help", "pomoc"]:
                helping = self.current_module.help(self.language)
                output("")
                for i in helping:
                    output(f"{i} : {helping[i]}")
                
            elif self.user_choise in ["моды", "mods"]:
                webbrowser.open("https://docs.google.com/spreadsheets/d/1f-hTM34sLfALxQuS4YoAA-Rx9XL9Adfl")

            elif self.user_choise in ["текстур паки", "texture packs", "pakiety tekstur"]:
                result = self.current_module.texture_packs()
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i)                

            # схематики

            elif self.user_choise in ["схематики", "scematics", "schematy"]:
                output("")
                output(self.translations["minecraft_module"]["choose_the_shematic"])

                if self.sub_fill_status == 0:
                    if self.language == "ru":
                        self.list_of_options = ["домик", "конюшня", "лодка", "дирижабль", "назад"] #Склад
                    elif self.language == "en":
                        self.list_of_options = ["house", "stable", "boat", "airship", "back"]
                    elif self.language == "pl":
                        self.list_of_options = ["dom", "stajnia", "łódź", "sterowiec", "powrot"]
                    self.input_state = "sub choise"
                    self.sub_fill_status = 1
                    return
                
                if self.sub_fill_status == 1:
                    # Выбор схематики
                    self.temp[0] = self.user_sub_choise
                    self.temp[2] = "0"

                    if self.temp[0] in ["домик", "house", "dom"]:
                        self.sub_fill_status = 2
                        self.temp[0] = "house-schematic"
                        self.temp[2] = "6"

                    elif self.temp[0] in ["конюшня","stable","stajnia"]:
                        self.sub_fill_status = 2
                        self.temp[0] = "stable-shematic"
                        self.temp[2] = "4"

                    elif self.temp[0] in ["лодка","boat","łódź"]:
                        self.sub_fill_status = 2
                        self.temp[0] = "boat-shematic"
                        self.temp[2] = "3"

                    elif self.temp[0] in ["дирижабль","airship","sterowiec"]:
                        self.sub_fill_status = 2
                        self.temp[0] = "airship-shematic"
                        self.temp[2] = "7"

                    elif self.temp[0] in ["назад", "back", "powrot"]:
                        self.back()

                if self.sub_fill_status == 2:
                    # Создаём список возможностей
                    if self.language == "ru":
                        self.list_of_options = ["ресурсы", "компоненты", "спереди", "сбоку", "назад"]
                    elif self.language == "en":
                        self.list_of_options = ["resourses", "components", "front", "side", "back"]
                    elif self.language == "pl":
                        self.list_of_options = ["zasoby", "komponenty", "przód", "bok", "powrot"]

                    for i in range(int(self.temp[2])):
                        self.list_of_options.append(str(i+1))

                    output("")
                    output(self.translations["minecraft_module"]["what_do_you_want_to_do"])

                    self.sub_fill_status = 3
                    return

                if self.sub_fill_status == 3:
                    # Выбор действия
                    with open("modules/Minecraft_module/memory_minecraft.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    self.temp[1] = self.user_sub_choise

                    if self.temp[1] in ["ресурсы", "resourses", "zasoby"]:
                        result = data[self.temp[0]]["resourses"]
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in result:
                                output(translator.translate(str(i)))
                        else:
                            for i in result:
                                output(i)                         
                        self.sub_fill_status = 3
                    elif self.temp[1] in ["компоненты", "components", "komponenty"]:
                        result = data[self.temp[0]]["components"]
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in result:
                                output(translator.translate(str(i)))
                        else:
                            for i in result:
                                output(i)  
                        self.sub_fill_status = 3
                    elif self.temp[1] in ["спереди", "front", "przód"]:
                        self.temp[1] = "front"
                        self.sub_fill_status = 4
                    elif self.temp[1] in ["сбоку", "side", "bok"]:
                        self.temp[1] = "side"
                        self.sub_fill_status = 4
                    elif self.temp[1].isdigit():
                        self.temp[1] = "layer" + self.temp[1]
                        self.sub_fill_status = 4
                    elif self.temp[1] in ["назад", "back", "powrot"]:
                        self.back()
                    
                if self.sub_fill_status == 4:
                    image = self.current_module.show_shematic(self.temp[0], self.temp[1])
                    time.sleep(1)
                    if image != False:
                        image.show() 
                    else:
                        output(self.translations["minecraft_module"]["image_generation_error"])
                    
                    self.sub_fill_status = 3

            elif self.user_choise in ["сундуки", "chests", "skrzynie"]:
                output("")
                result = self.current_module.show_list(True, "chests")
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i) 

            elif self.user_choise in ["незер", "nether"]:
                output("")
                result = self.current_module.show_list(True, "nether")
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i) 

            elif self.user_choise in ["прочее", "other", "inne"]:
                output("")
                result = self.current_module.show_list(False, "other")
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i) 

            elif self.user_choise == "any":
                output("♪(^∇^*)")

            elif self.user_choise in ["выход", "exit", "wyjscie"]:
                output(self.translations["moduleloading"]["exiting_from_module"])
                self.system = "main"
                self.list_of_options = list(self.helping.keys())
                time.sleep(0.2)

        elif self.system == "School":

            if self.user_choise in ["помощь","help","pomoc"]:
                helping = self.current_module.help(self.language)
                output("")
                for i in helping:
                    output(f"{i} : {helping[i]}")

            elif self.user_choise in ["оценки","grades","wyniki"]:
                result = self.current_module.grades()
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i) 

            elif self.user_choise in ["средний бал","average grade","średni wynik"]:
                result = self.current_module.all_avg()
                if self.autotranslation:
                    translator = GoogleTranslator(source='ru', target=self.language)
                    for i in result:
                        output(translator.translate(str(i)))
                else:
                    for i in result:
                        output(i) 

            elif self.user_choise == "any":
                output("~(￣▽￣)~*")

            elif self.user_choise in ["выход", "exit", "wyjscie"]:
                output(self.translations["moduleloading"]["exiting_from_module"])
                self.system = "main"
                self.list_of_options = list(self.helping.keys())
                time.sleep(0.2)

        elif self.system == "Archive":
            # self.list_of_options = ("помощь", "просмотренно", "просмотренно майнкрафт", "просмотренно бесконечные", "время просмотра", "дневник", "выход")

            if self.user_choise in ["помощь","help","pomoc"]:
                helping = self.current_module.help(self.language)
                output("")
                for i in helping:
                    output(i, ":", helping[i])
            
        elif self.user_choise in ["просмотренно", "watched", "ogladane"]:
            if self.sub_fill_status == 0:
                if self.language == "ru":
                    self.list_of_options = ["все", "майнкрафт", "бесконечные", "время просмотра", "заброшеные", "своё условие", "назад"]
                elif self.language == "en":
                    self.list_of_options = ["all", "minecraft", "infinite", "watch time", "abandoned", "your condition", "back"]
                elif self.language == "pl":
                    self.list_of_options = ["wszystko", "minecraft", "nieskończone", "czas oglądania", "porzucone", "swoja umowa", "powrót"]
                self.input_state = "sub choise"
                self.sub_fill_status = 1
                return

            if self.sub_fill_status == 1:
                # Выбор действия юзера
                self.temp[0] = self.user_sub_choise
 
                if self.temp[0] in ["все", "all", "wszystko"]:
                    result = self.current_module.show_watched(["Просмотренно до переезда в польшу", "Архивация 1"], None)
                    if self.autotranslation:
                        translator = GoogleTranslator(source='ru', target=self.language)
                        for i in result:
                            output(translator.translate(str(i)))
                    else:
                        for i in result:
                            output(i) 

                elif self.temp[0] in ["майнкрафт", "minecraft", "minecraft"]:
                    result = self.current_module.show_watched(["Просмотренно майнкрафт"], None)
                    if self.autotranslation:
                        translator = GoogleTranslator(source='ru', target=self.language)
                        for i in result:
                            output(translator.translate(str(i)))
                    else:
                        for i in result:
                            output(i) 

                elif self.temp[0] in ["бесконечные", "infinite", "nieskończone"]:
                    result = self.current_module.show_watched(["Бесконечные"], None)
                    if self.autotranslation:
                        translator = GoogleTranslator(source='ru', target=self.language)
                        for i in result:
                            output(translator.translate(str(i)))
                    else:
                        for i in result:
                            output(i) 

                elif self.temp[0] in ["время просмотра", "watch time", "czas oglądania"]:
                    output(self.current_module.show_watched_time(["Бесконечные", "Просмотренно до переезда в польшу", "Архивация 1", "Просмотренно майнкрафт"]))

                    output("время занижено т. к. многое ты в архив не вписал")


                elif self.temp[0] in ["заброшеные", "abandoned", "porzucone"]:
                    result = self.current_module.show_watched(["Бесконечные", "Просмотренно до переезда в польшу", "Архивация 1", "Просмотренно майнкрафт"], "`Статус` = 'забросил'")
                    if self.autotranslation:
                        translator = GoogleTranslator(source='ru', target=self.language)
                        for i in result:
                            output(translator.translate(str(i)))
                    else:
                        for i in result:
                            output(i) 

                elif self.temp[0] in ["своё условие", "your condition", "porzucone"]:
                    if self.temp[1] == "1":
                        output("это експирементальная функция, будте акуратны")
                        self.input_state = "any input"
                        output("Введите условие типа a = 'b'")
                        return
                    else:
                        result = self.current_module.show_wathed(["Бесконечные", "Просмотренно до переезда в польшу", "Архивация 1", "Просмотренно майнкрафт"], self.user_input)
                        if self.autotranslation:
                            translator = GoogleTranslator(source='ru', target=self.language)
                            for i in result:
                                output(translator.translate(str(i)))
                        else:
                            for i in result:
                                output(i) 

                elif self.temp[0] == "назад":
                    self.back()

        elif self.user_choise in ["сериалы", "series", "serialy"]:
            result = self.current_module.serial_progress()
            if self.autotranslation:
                translator = GoogleTranslator(source='ru', target=self.language)
                for i in result:
                    output(translator.translate(str(i)))
            else:
                for i in result:
                    output(i) 

        elif self.user_choise in ["пароли", "passwords", "hasla"]:
            self.input_state = "any input"
            self.show_tultip = False
            output("Введи пароль от хранилища: (qwerty123)")

            if self.user_input == "назад":
                self.input_state = "choise" 
                self.show_tultip = True                 
            else:
                a = 1
                result = self.current_module.codes(self.user_input)

                if type(result) == list:
                    for i in result:
                        if i in ["ylanck", "зlanck"]:
                            output(" ")
                        else:
                            output(i)
                    output("")
                    self.input_state = "choise" 
                    self.show_tultip = True
                else:
                    if a == 1:
                        a = 0
                    else:
                        output(result)
                
        elif self.user_choise in ["цели", "goals", "cele"]:
            result = self.current_module.tags()
            if self.autotranslation:
                translator = GoogleTranslator(source='ru', target=self.language)
                for i in result:
                    output(translator.translate(str(i)))
            else:
                for i in result:
                    output(i) 

            # self.input_state = "password"
            # self.show_tultip = False
            # output("Введи пароль от хранилища:")

        elif self.user_choise == "any":
            output("ヽ(≧∇≦)ﾉ")

        elif self.user_choise in ["выход", "exit", "wyjscie"]:
            output(self.translations["moduleloading"]["exiting_from_module"])
            self.system = "main"
            self.list_of_options = list(self.helping.keys())
            time.sleep(0.2)

        if self.cleaning:
            if self.input_state == "choise":
                self.user_sub_choise = ""
                self.user_input = ""
            elif self.input_state == "sub choise":
                self.user_choise = ""
                self.user_input = ""
            elif self.input_state == "any input":
                self.user_choise = ""
                self.user_sub_choise = ""
            
            self.temp = ["0","1","2","3"]
            self.cleaning = False