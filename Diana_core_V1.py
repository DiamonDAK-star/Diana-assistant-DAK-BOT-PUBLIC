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


memory_file = "memory_main.json"
with open(memory_file, "r", encoding='utf-8') as f:
    data = json.load(f)

class Core:
    def __init__(self):
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
        self.helping = {
            "помощь" : "для высвечивания этого текста", 
            "майн" : "запускает модуль майнкрафта", 
            "майнкрафт": "запускает модуль майнкрафта", 
            "школа": "запускает модуль техникума", 
            "техникум": "запускает модуль техникума", 
            "архив": "запускает модуль архивов", 
            "заметки": "показывает заметки",
            # "даты":"показывает важные даты",
            # "выбери игру": "для выбора игры из списка: ['Minecraft', 'Barotrauma', 'Flotsam', 'Terra tech', 'Timber born', 'Risen kingdom', 'Tails of iron', 'Доп. игра'] \n Где дополнительный список игр это: ['Castle story', 'Cult of the lamb', 'Dorf romantic', 'Kendle knight', 'Terra nill', 'Tin boy', 'Word of goo']",
            "монетка": "подбрасывает монетку и говорит Орёл или решка", 
            "анекдот": "расказывает анекдот", 
            "курсор": "для изменения курсора", 
            "выход": "закрывает програму"
            # "дела" : "для показа списка дел"
        }
        self.list_of_options = tuple(self.helping.keys())
        self.temp = ["0","1","2","3"]
        self.sub_fill_status = 0

        # Нужен для очистки всех переменных
        # Если поставить в True то все переменные очистятся и оно снова станет False
        
        
    def back(self):
        cleaning = True
        self.sub_fill_status = 0
        self.input_state = "choise"
        self.temp = ["0","1","2","3"]
        self.list_of_options = tuple(self.current_module.help().keys())
        
    def load_module(self, module, log, output):
        if log:
            output("Загрузка модуля")
        try:
            module = importlib.import_module(f"modules.{module}")
            if log:
                output(f"Модуль {module} загружен")
            return module
        except ModuleNotFoundError:
            # if log:
            output(f"Ошибка загрузки модуля {module}")
            return False

    # def current_date_check(self, output):
        today = datetime.today()
        dates = data["dates"]
        check = True
        for i in dates:
            if (today.day == i[0]) and (today.month == i[1]):
                output(f"Сегодня {i}")
                check = False

        if check:
            output("Сегодня обычный день, надеюсь он проходит хорошо")

    def process(self, user, output):

        if self.input_state in ["choise", "sub choise"]:

            if user.lower() in self.list_of_options or len(user) == 0:

                if len(user) == 0:
                    user = "any"
                else:
                    user = user.lower()

                if self.input_state == "choise":
                    self.user_choise = user
                else:
                    self.user_sub_choise = user
                
            else:
                output("Такой опции нет")
                return

        elif self.input_state == "any input":
            self.user_input = user

        else:
            output("Ошибка состояния ввода")
            self.input_state = "choise"
            return

        cleaning = False
        if self.system == "main":

            # Входы в модули
            if self.user_choise in ("майн","майнкрафт"):
                module = self.load_module("module_minectaft", True, output)

                if module != False:
                    self.system = "Minecraft"
                    self.current_module = module
                    self.list_of_options = tuple(self.current_module.help().keys())
                else:
                    output("Ошибка загрузки модуля")  

            elif self.user_choise in ("школа", "техникум"):
                module = self.load_module("module_school", True, output)

                if module != False:
                    self.system = "School"
                    self.current_module = module
                    self.list_of_options = tuple(self.current_module.help().keys())  
                else:
                    output("Ошибка загрузки модуля")
            
            elif self.user_choise == "архив":
                module = self.load_module("module_archive", True, output)

                if module != False:
                    self.system = "Archive"
                    self.current_module = module     
                    self.list_of_options = tuple(self.current_module.help().keys())           
                else:
                    output("Ошибка загрузки модуля")

            # обычные команды
            elif self.user_choise == "помощь":
                output()
                for i in self.helping:
                    output(i, ":", self.helping[i])

            elif self.user_choise == "заметки":
                with open("memory_main.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    
                notes = data["notes"]

                output("Какую заметку ты хочешь увидеть?")
                if self.input_state == "choise":
                    self.list_of_options = ["заметка 1","заметка 2","заметка 3",]
                    self.input_state = "sub choise"
                    return
                else:
                    output()
                    if self.user_sub_choise == "заметка 1":
                        for i in notes["note1"]:
                            output(i)
                    elif self.user_sub_choise == "заметка 2":
                        for i in notes["note2"]:
                            output(i)
                    elif self.user_sub_choise == "заметка 3":
                        for i in notes["note3"]:
                            output(i)
                    elif self.user_sub_choise == "назад":
                        self.back()

            # elif self.user_choise == "даты":
                with open("memory_main.json", "r", encoding="utf-8") as f:
                    data = json.load(f)

                dates = data["dates"]
                for i in dates:
                    output(f"{i}: {dates[i][0]:0>2}.{dates[i][1]:0>2}")

            # elif self.user_choise =="выбери игру":
                # search_filling = True
                # light = False
                # while search_filling:
                #     self.user_input = input("У андрея есть свет? (да/нет) :> ")
                #     if self.user_input == "да":
                #         light = True
                #         search_filling = False
                #     elif self.user_input == "нет":
                #         light = False
                #         search_filling = False
                #     else:
                #         output("напиши да или нет")

                # if light:
                #     game = choice(remote_games)
                # else:
                    # game = choice(['Minecraft', 'Barotrauma', 'Flotsam', 'Terra tech', 'Timber born', 'Risen kingdom', 'Tails of iron', 'Доп. игра'])
                    # if game == "Доп. игра":
                    #     game = choice(['Castle story', 'Cult of the lamb', 'Dorf romantic', 'Kendle knight', 'Terra nill', 'Tin boy', 'Word of goo'])

                    # output()
                    # output(game)

            # elif self.user_input =="список дел":
            #     # with open("memory_main.json", "r", encoding="utf-8") as f:
            #     #     data = json.load(f)

            #     # a = data[""]
            #     # b = data["tasks_for_later"]
            #     list_of_tasks =  data["tasks_for_later"]
            #     for i in list_of_tasks:
            #         output(list_of_tasks[i])

            elif self.user_choise == "монетка":
                output()
                if random.randint(1, 2) == 1:
                    output("Орёл")
                else:
                    output("Решка")

            elif self.user_choise == "анекдот":
                module = self.load_module("module_archive", True, output)

                if module != False:
                    self.system = "Archive"
                    self.current_module = module  
                    
                    with open("memory_main.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    joke = random.choice(data["jokes"])
                    output()
                    output(self.current_module.reveal(joke))

                    self.system = "main"

                else:
                    output("Ошибка декода")

            elif self.user_choise == "курсор":
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

                output("Изменено!")
                output()

            elif self.user_choise == "выход":
                self.terminal_running = False
                output("Остановка ядра...")
                time.sleep(1)
                output("Выход...")

            elif self.user_choise == "any":
                output("ㄟ(≧◇≦)ㄏ")

            else:
                output("Не поняла команду")

        elif self.system == "Minecraft":

            if self.user_choise == "помощь":
                helping = self.current_module.help()
                output()
                for i in helping:
                    output(i, ":", helping[i])
                

            elif self.user_choise == "моды":
                webbrowser.open("https://docs.google.com/spreadsheets/d/1f-hTM34sLfALxQuS4YoAA-Rx9XL9Adfl")

            elif self.user_choise == "текстур паки":
                result = self.current_module.texture_packs()
                for i in result:
                    output(i)                

            # схематики

            elif self.user_choise == "схематики":
                output()
                output("Выбери схематику")

                if self.sub_fill_status == 0:
                    self.list_of_options = ["домик", "конюшня", "лодка", "дирижабль", "назад"] #Склад
                    self.input_state = "sub choise"
                    self.sub_fill_status = 1
                    return
                
                if self.sub_fill_status == 1:
                    # Выбор схематики
                    self.temp[0] = self.user_sub_choise
                    self.temp[2] = "0"

                    if self.temp[0] == "домик":
                        self.sub_fill_status = 2
                        self.temp[0] = "house-schematic"
                        self.temp[2] = "6"

                    elif self.temp[0] == "конюшня":
                        self.sub_fill_status = 2
                        self.temp[0] = "stable-shematic"
                        self.temp[2] = "4"

                    elif self.temp[0] == "лодка":
                        self.sub_fill_status = 2
                        self.temp[0] = "boat-shematic"
                        self.temp[2] = "3"

                    elif self.temp[0] == "дирижабль":
                        self.sub_fill_status = 2
                        self.temp[0] = "airship-shematic"
                        self.temp[2] = "7"

                    elif self.temp[0] == "назад":
                        self.back()

                if self.sub_fill_status == 2:
                    # Создаём список возможностей
                    self.list_of_options = ["ресурсы", "компоненты", "спереди", "сбоку"]
                    for i in range(int(self.temp[2])):
                        self.list_of_options.append(str(i+1))
                    self.list_of_options.append("назад")

                    output()
                    output("Выбери что ты хочешь сделать")

                    self.sub_fill_status = 3
                    return

                
                if self.sub_fill_status == 3:
                    # Выбор действия
                    with open("modules/Minecraft_module/memory_minecraft.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    self.temp[1] = self.user_sub_choise

                    if self.temp[1] == "ресурсы":
                        output(data[self.temp[0]]["resourses"])
                        self.sub_fill_status = 3
                    elif self.temp[1] == "компоненты":
                        output(data[self.temp[0]]["components"])
                        self.sub_fill_status = 3
                    elif self.temp[1] == "спереди":
                        self.temp[1] = "front"
                        self.sub_fill_status = 4
                    elif self.temp[1] == "сбоку":
                        self.temp[1] = "side"
                        self.sub_fill_status = 4
                    elif self.temp[1].isdigit():
                        self.temp[1] = "layer" + self.temp[1]
                        self.sub_fill_status = 4
                    elif self.temp[1] == "назад":
                        self.back()
                    
                if self.sub_fill_status == 4:
                    image = self.current_module.show_shematic(self.temp[0], self.temp[1])
                    time.sleep(1)
                    if image != False:
                        image.show() 
                    else:
                        output("Ошибка генерации изображения")
                    
                    self.sub_fill_status = 3

            elif self.user_choise == "сундуки":
                output()
                result = self.current_module.show_list(True, "chests")
                for i in result:
                    output(i)

            elif self.user_choise == "незер":
                output()
                result = self.current_module.show_list(True, "nether")
                for i in result:
                    output(i)

            elif self.user_choise == "прочее":
                output()
                result = self.current_module.show_list(False, "other")
                for i in result:
                    output(i)

            elif self.user_choise == "any":
                output("♪(^∇^*)")

            elif self.user_choise == "выход":
                output("Выход из модуля")
                self.system = "main"
                self.list_of_options = tuple(self.helping.keys())
                time.sleep(0.2)

            else:
                output("Команда не распознана") 

        elif self.system == "School":

            if self.user_choise == "помощь":
                helping = self.current_module.help()
                output()
                for i in helping:
                    output(i, ":", helping[i])

            elif self.user_choise == "оценки":
                result = self.current_module.grades()
                for i in result:
                    output(i)

            elif self.user_choise == "средний бал":
                result = self.current_module.all_avg()
                for i in result:
                    output(i)

            elif self.user_choise == "any":
                output("~(￣▽￣)~*")

            elif self.user_choise == "выход":
                output("Выход из модуля")
                self.system = "main"
                self.list_of_options = tuple(self.helping.keys())
                time.sleep(0.2)

            else:
                output("Команда не распознона!")

        elif self.system == "Archive":

            # self.list_of_options = ("помощь", "просмотренно", "просмотренно майнкрафт", "просмотренно бесконечные", "время просмотра", "дневник", "выход")

            if self.user_choise == "помощь":
                helping = self.current_module.help()
                output()
                for i in helping:
                    output(i, ":", helping[i])
            
            elif self.user_choise == "просмотренно":
                result = self.current_module.show_watched(["Просмотренно до переезда в польшу", "Архивация 1"])
                for i in result:
                    output(i)

            elif self.user_choise == "просмотренно майнкрафт":
                result = self.current_module.show_watched(["Просмотренно майнкрафт"])
                for i in result:
                    output(i)

            elif self.user_choise == "просмотренно бесконечные":
                result = self.current_module.show_watched(["Бесконечные"])
                for i in result:
                    output(i)

            elif self.user_choise == "время просмотра":
                output(self.current_module.show_watched_time(["Бесконечные", "Просмотренно до переезда в польшу", "Архивация 1", "Просмотренно майнкрафт"]))

                output("Но данные могут быть неточными")


            elif self.user_choise == "сериалы":
                result = self.current_module.serial_progress()
                for i in result:
                    output(i)

            elif self.user_choise == "пароли":
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
                        output()
                        self.input_state = "choise" 
                        self.show_tultip = True
                    else:
                        if a == 1:
                            a = 0
                        else:
                            output(result)
                    
            elif self.user_choise == "цели":
                result = self.current_module.tags()
                for i in result:
                    output(i)

                # self.input_state = "password"
                # self.show_tultip = False
                # output("Введи пароль от хранилища:")

            elif self.user_choise == "any":
                output("ヽ(≧∇≦)ﾉ")

            elif self.user_choise == "выход":
                output("Выход из модуля")
                self.system = "main"
                self.list_of_options = tuple(self.helping.keys())
                time.sleep(0.2)

            else:
                output("Команда не распознона!")

            if cleaning:
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
                cleaning = False