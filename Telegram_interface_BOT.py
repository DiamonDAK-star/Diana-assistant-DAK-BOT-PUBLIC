# from telegram import Update
from deep_translator import GoogleTranslator
from telegram.ext import Application, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
import json

from Diana_core_V1 import Core

core = Core()
check = True

with open("modules/Archive_module/archive.json", "r", encoding='utf-8') as f:
    data = json.load(f)
TOKEN = data["T"]

if TOKEN == "Put_your_token_here":
    check = False

if check:
    def make_keyboard(options, row_size=4):
        keyboard = []

        for i in range(0, len(options), row_size):
            keyboard.append(options[i:i + row_size])

        return keyboard


    async def handle_message(update, context):

        user = update.message.text
        messages = []

        def output(*args):
            for i in args:
                i = GoogleTranslator(source='ru', target=core.language).translate(i)
            messages.append(" ".join(map(str, args)))

        user = GoogleTranslator(source=core.language, target='ru').translate(user)
        core.process(user, output)

        await update.message.reply_text("\n".join(messages))

        if core.input_state in ["choise", "sub choise"] and core.show_tultip:

            keyboard = make_keyboard(core.main_list_of_options)


            markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

            await update.message.reply_text(f"Диана: {core.system}, жду команды :> ", reply_markup=markup)
        else:
            await update.message.reply_text(f"Диана: {core.system}, жду команды :> ")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Бот запущен")

    app.run_polling()
else:
    print("Ошибка нахождения ключа, для публичной версии надо добавить свой ключ!")