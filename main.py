import time

from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from webhook_flask import \
    app, \
    WEBHOOK_URL_BASE, \
    WEBHOOK_URL_PATH, \
    WEBHOOK_SSL_CERT, \
    WEBHOOK_LISTEN, \
    WEBHOOK_PORT, \
WEBHOOK_SSL_PRIV


if __name__ == "__main__":
    set_default_commands(bot)
    # bot.infinity_polling()
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    time.sleep(1)
    # Set webhook
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))
    # Start flask server
    app.run(host=WEBHOOK_LISTEN,
            port=WEBHOOK_PORT,
            ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
            debug=True)
