from machine import Pin, ADC
from utelegram import Bot, Conversation

TOKEN = ''

sensor = ADC(Pin(32))

bot = Bot(TOKEN)
c = Conversation(['UPPER', 'LOWER'])
user = None
sent = False #per non notificare più volte lo stesso evento

min_temp = -10000 #default molto alti per evitare le notifiche
max_temp = 10000

@c.add_command_handler('ENTRY', 'start')
def start(update):
    update.reply('Inserisci la soglia superiore in gradi celsius')
    return 'UPPER'

@c.add_message_handler('UPPER', '^[0-9]*$')
def upper(update):
    global max_temp
    max_temp = int(update.message['text']) 
    update.reply('soglia superiore impostata a *{}* celsius\.\nInserisci la soglia inferiore'.format(max_temp))
    return 'LOWER'

@c.add_message_handler('LOWER', '^[0-9]*$')
def lower(update):
    global user
    global min_temp
    min_temp = int(update.message['text']) 
    user = update.message['chat']['id']
    update.reply('soglia inferiore impostata a *{}* celsius\.'.format(min_temp))
    return c.END

bot.add_conversation_handler(c)

while True:
    bot.read()
    temp = ((1/4095)*sensor.read())*100 #maximum value 100 celsius with 1 volt
    print(temp)
    if temp > max_temp:
    	print('superato')
    	if not sent:
    	    sent = True
    	    bot.send_message(user, 'Soglia superiore superata')
    elif temp < min_temp:
    	if not sent:
    	    sent = True
    	    bot.send_message(user, 'Soglia inferiore superata')
    else:
    	sent = False
