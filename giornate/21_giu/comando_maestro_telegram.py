from utelegram import Bot, Conversation, ReplyKeyboardMarkup, KeyboardButton

TOKEN = '1706490752:AAH-v4l4r-NmN2sfXOsO0bz_zOwWn1P7IQc'

b = Bot(TOKEN)

main_keyboard = ReplyKeyboardMarkup([
	[KeyboardButton('Controllo Manuale')],
	[KeyboardButton('Operazioni registrate')]
	
])

keyboard_manuale = ReplyKeyboardMarkup([
	[KeyboardButton('-5'), KeyboardButton('Servo 0'), KeyboardButton('+5')],
	[KeyboardButton('-5'), KeyboardButton('Servo 1'), KeyboardButton('+5')],
	[KeyboardButton('-5'), KeyboardButton('Servo 2'), KeyboardButton('+5')],
	[KeyboardButton('-5'), KeyboardButton('Servo 3'), KeyboardButton('+5')],
	[KeyboardButton('-5'), KeyboardButton('Servo 4'), KeyboardButton('+5')],
	[KeyboardButton('-5'), KeyboardButton('Servo 5'), KeyboardButton('+5')]
])

back_keyboard = ReplyKeyboardMarkup([
	[KeyboardButton('Back')]
])

controllo_manuale = Conversation(['MENU', 'MANUALE'])

@controllo_manuale.add_message_handler('ENTRY', '^Controllo Manuale$')
def menu_manuale(update):
	update.reply('Utilizza la tastiera per comandare i servomotori', reply_markup=keyboard_manuale)
	return 'MENU'
	
@controllo_manuale.add_message_handler('MENU', '^Servo [0-9]$')
def chiedi_angolo(update):
	num = update.message['text'][-1]
	update.reply('Inserisci l\'angolo a cui posizionare il *servo {}* oppure premi back per tornare al menù precedente'.format(num), reply_markup=back_keyboard)
	return 'MANUALE'

@controllo_manuale.add_message_handler('MANUALE', '^Back$')
def back_to_menu_manuale(update):
	update.reply('Utilizza la tastiera per comandare i servomotori', reply_markup=keyboard_manuale)
	return 'MENU'

@b.add_command_handler('start')
def start(update):
	update.reply('Benvenuto\!', reply_markup=main_keyboard)
	controllo_manuale.end() #chiudi conversazioni in caso di reset
	

b.add_conversation_handler(controllo_manuale)

b.start_loop()
