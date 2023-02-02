from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from model import dataList, MultDel, plusMinus,countParentheses

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Здравствуй, дорогой друг! Если тебе нужна помощь в счете, ты обратился по адресу.')
    context.bot.send_message(update.effective_chat.id,'Если ты хочешь прочитать инструкцию к калькулятору, нажми: 1, а если хочешь посчитать, нажми:2. Если хочешь выйти, нажми:3')
    return A

def menu(update, context):
    choise = update.message.text
    if choise=='1':
        context.bot.send_message(update.effective_chat.id, 'В этом калькуляторе можно сложить,вычесть,умножить, разделить используя для ввода знаки:+,-,*,/.')
        context.bot.send_message(update.effective_chat.id, 'Можно использовать скобки и вещественные числа.Просто введите полностью выражение,которое выхотите вычислить.')
        context.bot.send_message(update.effective_chat.id, 'Сделай выбор еще раз.')
        return A
    elif choise=='2':
        context.bot.send_message(update.effective_chat.id, 'Введите выражение,которое вы хотите посчитать.')
        return B
    elif choise=='3':
        context.bot.send_message(update.effective_chat.id, 'До свидания! Приходи еще!')
        return ConversationHandler.END  

    else:
        context.bot.send_message(update.effective_chat.id, 'Неправильно ввели номер. Повторите ввод, пожалуйста')
        return A

def calcul(update, context):
      
    x=update.message.text
    xWithoutParentheses=countParentheses(x)
    data=dataList(xWithoutParentheses)
    newdata=MultDel(data)
    result=plusMinus(newdata)
    with open('db.csv','a') as data:
        data.write(f'{update.effective_user.id},{update.message.text},{result}\n')
    context.bot.send_message(update.effective_chat.id, f'Ваш результат: {result}') 
    context.bot.send_message(update.effective_chat.id, 'Хотите еще раз ознакомиться с инструкцией? нажмите 1. Если хотите еще раз посчитать, нажмите 2. Выход-3') 
    return A

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До свидания! С удовольствием сыграю с тобой еще раз!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
menu_handler = MessageHandler(Filters.text, menu)
calcul_handler = MessageHandler(Filters.text, calcul)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A:[menu_handler],
                                    B:[calcul_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()