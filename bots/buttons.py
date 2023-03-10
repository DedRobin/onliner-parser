from telegram import ReplyKeyboardMarkup

markup_start = ReplyKeyboardMarkup(
    [
        ["Добавить товар для отслеживания"],
    ]
    , resize_keyboard=True)

markup_back = ReplyKeyboardMarkup(
    [
        ["Назад"],
    ],
    resize_keyboard=True
)
