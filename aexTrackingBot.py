import logging
# Importar libreria de precios de la yerba
from aexRequests import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import config['TOKEN']

# Iniciar Loggin
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# funcion para enviar el primer mensaje luego del /start


def start(update, context):
    update.message.reply_text(
        'Envíe el codigo para mostrar el seguimiento')
    chat_id = update.message.chat_id


# funcion para explicar los comandos
# def help_command(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text(
#         '- Envíe el codigo para buscar el pedido')


def echo(update, context):
    try:
        trackingCode = update.message.text
        send = responseFilter(trackingCode)
        update.message.reply_text(f'N° de paquete: {trackingCode}')
        update.message.reply_text(send)
    except:
        update.message.reply_text('Codigo invalido! vuelva a intentarlo')


def main():
    """Inicia el bot con un TOKEN"""
    updater = Updater(
        config['TOKEN'], use_context=True)

    dp = updater.dispatcher

    # los diferentes comandos para bot
    dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("ayuda", help_command))
    #dp.add_handler(CommandHandler("buscar", menuPrecio))

    # updater.dispatcher.add_handler(CallbackQueryHandler(buttonPrecio))
    # updater.dispatcher.add_handler(CallbackQueryHandler(buttonLink))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    # is the original dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
