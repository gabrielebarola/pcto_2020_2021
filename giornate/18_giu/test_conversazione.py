#REMEMBER TO RENAME FILE TO main.py BEFORE UPLOAING TO THE BOARD

#THIS SIMPLE EXAMPLE IS USED TO TURN AN LED CONNECTED TO PIN 2 ON AND OFF USING A CUSTOM KEYBOARDAD,
#IT IS ALSO POSSIBLE TO KNOW THE CURRENT STATE OF THE PIN
from utelegram import Bot, Conversation, ReplyKeyboardMarkup, KeyboardButton
from machine import Pin

TOKEN = 'token'

bot = Bot(TOKEN)
led = Pin(2, Pin.OUT)
c = Conversation(['NAME', 'AGE'])

@c.add_command_handler('ENTRY', 'start')
def start(update):
	update.reply('Come ti chiami?')
	return 'NAME'
	
@c.add_message_handler('NAME', '(.*?)') #every message
def nome(update):
	update.reply('Ciao {}, quanti anni hai?'.format(update.message['text']))
	return 'AGE'
	
@c.add_command_handler('AGE', 'value')
def fake_value(update):
	update.reply('fallo dopo')
	return 'AGE'
	
@c.add_message_handler('AGE', '^[0-9]*$') #only numbers
def eta(update):
	if int(update.message['text']) > 17:
		update.reply('accesso consentito')
		led.on()
		return c.END
	else: 
		update.reply('accesso non consentito, riprova')
		led.off()
		return 'AGE'

@bot.add_command_handler('value')
def value(update):
    if led.value():
        update.reply('LED is on')
    else:
        update.reply('LED is off')
        
bot.add_conversation_handler(c)
bot.start_loop()

