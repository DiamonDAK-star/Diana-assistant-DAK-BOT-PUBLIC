import json
from PIL import Image


def texture_packs():
    with open("modules/Minecraft_module/memory_minecraft.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    texture_packs = data["texture_packs"]

    result = []

    result.append(("╔"+"═"*25+"╦"+"═"*35+"╦"+"═"*89+"╗"))
    for texture in texture_packs:
        a = texture["name"]
        b = texture["function"]
        c = texture["link"] 
        result.append((f"║ {a:<23} " + f"║ {b:<33} " + f"║ {c:<87} ║"))
    result.append(("╚"+"═"*25+"╩"+"═"*35+"╩"+"═"*89+"╝"))

    return result


def list_of_shematics():
    list = {"домик":5, "конюшня":4, "лодка":3, "дирижабль":7}
    # "Склад" 
    # "Поле":5, 
    return list

def show_shematic (target, sub_target):
    with open("modules/Minecraft_module/memory_minecraft.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Оглошение словаря текстур
    # Принцип названий файлов:
    # cobblestone-stairs-front-right": Image.open("modules/Minecraft_module/cobblestone-stairs-front-right.png")
    # ГДЕ:
    # modules/Minecraft_module/ = папка
    # cobblestone-stairs = название
    # front = преспектива (front/side/top), где side это показывается левая сторона
    # right = направление ступеньки
    textures = {
        "air": Image.open("modules/Minecraft_module/air.png"),
        "ballon": Image.open("modules/Minecraft_module/ballon.png"),
        "cobblestone": Image.open("modules/Minecraft_module/cobblestone.png"),
        "cobblestone-stairs-front-left": Image.open("modules/Minecraft_module/cobblestone-stairs-front-left.png"),
        "cobblestone-stairs-front-right": Image.open("modules/Minecraft_module/cobblestone-stairs-front-right.png"),
        "cobblestone-stairs-top-left": Image.open("modules/Minecraft_module/cobblestone-stairs-top-left.png"),
        "cobblestone-stairs-top-right": Image.open("modules/Minecraft_module/cobblestone-stairs-top-right.png"),
        "cobblestone-stairs-side-left": Image.open("modules/Minecraft_module/cobblestone-stairs-side-left.png"),
        "chest-front": Image.open("modules/Minecraft_module/chest-front.png"),
        "chest-top": Image.open("modules/Minecraft_module/chest-top.png"),
        "dirt": Image.open("modules/Minecraft_module/dirt.png"),
        "door-front-bottom": Image.open("modules/Minecraft_module/door-front-bottom.png"),
        "door-front-top": Image.open("modules/Minecraft_module/door-front-top.png"),
        "engine": Image.open("modules/Minecraft_module/engine.png"),
        "fence-side-A": Image.open("modules/Minecraft_module/fence-side-A.png"),
        "fence-side-B": Image.open("modules/Minecraft_module/fence-side-B.png"),
        "fence-side-C": Image.open("modules/Minecraft_module/fence-side-C.png"),
        "fence-top-center": Image.open("modules/Minecraft_module/fence-top-center.png"),
        "fence-top-A": Image.open("modules/Minecraft_module/fence-top-A.png"),
        "fence-top-B": Image.open("modules/Minecraft_module/fence-top-B.png"),
        "fence-top-C": Image.open("modules/Minecraft_module/fence-top-C.png"),
        "fence-top-D": Image.open("modules/Minecraft_module/fence-top-D.png"),
        "flower": Image.open("modules/Minecraft_module/flower.png"),
        "floater": Image.open("modules/Minecraft_module/floater.png"),
        "gate-top": Image.open("modules/Minecraft_module/gate-top.png"),
        "gate-front": Image.open("modules/Minecraft_module/gate-front.png"),
        "planks": Image.open("modules/Minecraft_module/planks.png"),
        "planks-slab-A": Image.open("modules/Minecraft_module/planks-slab-A.png"),
        "planks-slab-B": Image.open("modules/Minecraft_module/planks-slab-B.png"),
        "seat": Image.open("modules/Minecraft_module/seat.png"),
        "stairs-top-left": Image.open("modules/Minecraft_module/stairs-top-left.png"),
        "stairs-top-right": Image.open("modules/Minecraft_module/stairs-top-right.png"),
        "stairs-side-front-left": Image.open("modules/Minecraft_module/stairs-side-front-left.png"),
        "stairs-side-left": Image.open("modules/Minecraft_module/stairs-side-left.png"),
        "stairs-side-right": Image.open("modules/Minecraft_module/stairs-side-right.png"),
        # "stairs-front-left": Image.open("modules/Minecraft_module/stairs-front-left.png"),
        # "stairs-front-right": Image.open("modules/Minecraft_module/stairs-front-right.png"),
        "stairs-side-front-upsidedown-left": Image.open("modules/Minecraft_module/stairs-side-front-upsidedown-left.png"),
        "stairs-side-upsidedown-left": Image.open("modules/Minecraft_module/stairs-side-upsidedown-left.png"),
        "stairs-side-upsidedown-right": Image.open("modules/Minecraft_module/stairs-side-upsidedown-right.png"),
        "staring-weel": Image.open("modules/Minecraft_module/staring-weel.png"),
        "trap-door-front": Image.open("modules/Minecraft_module/trap-door-front.png"),
        "trap-door-side-left": Image.open("modules/Minecraft_module/trap-door-side-left.png"),
        "trap-door-side-right": Image.open("modules/Minecraft_module/trap-door-side-right.png"),
        "trap-door-top-left": Image.open("modules/Minecraft_module/trap-door-top-left.png"),
        "trap-door-top-right": Image.open("modules/Minecraft_module/trap-door-top-right.png"),
        "wood-side": Image.open("modules/Minecraft_module/wood-side.png"),
        "wood-top": Image.open("modules/Minecraft_module/wood-top.png")
    }

    map_data = data[target][sub_target]
    block_size = 16
    rows = 8
    cols = 8

    final_img = Image.new("RGB", (cols * block_size, rows * block_size))

    for y in range(rows):
        for x in range(cols):
            block_type = map_data[y][x]
            texture = textures[block_type]
            final_img.paste(texture, (x * block_size, y * block_size))

    return final_img

def show_list(show_keys, target):
    with open("modules/Minecraft_module/memory_minecraft.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    a = data[target]
    list_of_things = a[0]
    result = []

    for i in list_of_things:
        if show_keys:
            result.append(i+": " + list_of_things[i])
        else:
            result.append(list_of_things[i])
    
    return result
    

def help(language):
    helping = {}
    if language == "ru":
        helping = {
            "помощь" : "для высвечивания этого текста", 
            "моды" : "показывает таблицу с модами",
            "текстур паки" : "показывает текстур паки",
            "схематики": "показывает схематики",
            "сундуки" : "показывает названия сундуков для склада",
            "незер" : "показывает список для подготовки к походу в незер",
            "прочее" : "показываает прочие заметки",
            "выход" : "выходит из модуля"
        }
    elif language == "en":
        helping = {
            "help" : "shows this text", 
            "mods" : "opens mods table",
            "texture packs" : "opens texture pack table",
            "scematics": "shows blueprints",
            "chests" : "shows hint for chest organazing",
            "nether" : "shows hint for nether",
            "other" : "shows other notes",
            "exit" : "exits the module"
        }
    elif language == "pl":
        helping = {
            "pomoc" : "wyświetla ten tekst", 
            "mods" : "otwiera tabelę modyfikacji",
            "pakiety tekstur" : "otwiera tabelę pakietów tekstur",
            "schematy" : "wyświetla plany",
            "skrzynie" : "wyświetla wskazówkę dotyczącą organizacji skrzyń",
            "nether" : "wyświetla wskazówkę dotyczącą przygotowań do Netheru",
            "inne" : "wyświetla inne notatki",
            "wyjscie" : "wychodzi z modula"
        }
    return helping