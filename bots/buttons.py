from telegram import ReplyKeyboardMarkup

markup_start = ReplyKeyboardMarkup(
    [
        ["Добавить товар для отслеживания",
         "Показать отслеживаемые товары"],
    ]
    , resize_keyboard=True
)
