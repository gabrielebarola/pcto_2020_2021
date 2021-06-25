from utelegram import Bot, Conversation, ReplyKeyboardMarkup, KeyboardButton
from servo import Servo

TOKEN = '1706490752:AAH-v4l4r-NmN2sfXOsO0bz_zOwWn1P7IQc'

Base = Servo(12)
Servo1 = Servo(14)
Servo2 = Servo(33)
Servo3 = Servo(25)
Servo4 = Servo(26)
Pinza = Servo(27)

servos = [Base, Servo1, Servo2, Servo3, Servo4, Pinza]

selected_servo = None

b = Bot(TOKEN)

main_keyboard = ReplyKeyboardMarkup([
	[KeyboardButton('Controllo Manuale')],
	[KeyboardButton('Operazioni registrate')]
	
])

keyboard_manuale = ReplyKeyboardMarkup([
	[KeyboardButton('S0: -10'), KeyboardButton('Servo 0'), KeyboardButton('S0: +10')],
	[KeyboardButton('S1: -10'), KeyboardButton('Servo 1'), KeyboardButton('S1: +10')],
	[KeyboardButton('S2: -10'), KeyboardButton('Servo 2'), KeyboardButton('S2: +10')],
	[KeyboardButton('S3: -10'), KeyboardButton('Servo 3'), KeyboardButton('S3: +10')],
	[KeyboardButton('S4: -10'), KeyboardButton('Servo 4'), KeyboardButton('S4: +10')],
	[KeyboardButton('S5: -10'), KeyboardButton('Servo 5'), KeyboardButton('S5: +10')],
	[KeyboardButton('Back')]
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
	global selected_servo
	num = update.message['text'][-1]
	selected_servo = servos[int(num)]
	update.reply('Inserisci l\'angolo a cui posizionare il *servo {}* oppure premi back per tornare al menù precedente'.format(num), reply_markup=back_keyboard)
	return 'MANUALE'
	
@controllo_manuale.add_message_handler('MENU', '^S[0-9]: -10$')
def decr(update):
	servo = servos[int(update.message['text'][1])]
	servo.move(servo.angle-10)
	update.reply('ok')
	return 'MENU'
	
@controllo_manuale.add_message_handler('MENU', '^S[0-9]: \+10$')
def incr(update):
	servo = servos[int(update.message['text'][1])]
	servo.move(servo.angle+10)
	update.reply('ok')
	return 'MENU'

@controllo_manuale.add_message_handler('MANUALE', '^[0-9]*$')
def move_to(update):
	global selected_servo
	angle = int(update.message['text'])
	
	if angle > 180:
		angle = 180
		update.reply('Valore troppo elevato, posizionamento a 180', reply_markup=keyboard_manuale)
	elif angle < 0:
		angle = 0 
		update.reply('Valore troppo basso, posizionamento a 0', reply_markup=keyboard_manuale)
	else:
		update.reply('Posizionamento a {}'.format(str(angle)), reply_markup=keyboard_manuale)
		
	selected_servo.move(angle)
	return 'MENU'

@controllo_manuale.add_message_handler('MANUALE', '^Back$')
def back_to_menu_manuale(update):
	update.reply('Utilizza la tastiera per comandare i servomotori', reply_markup=keyboard_manuale)
	return 'MENU'
	
@controllo_manuale.add_message_handler('MENU', '^Back$')
def back_to_main(update):
	update.reply('Benvenuto\!', reply_markup=main_keyboard)
	return controllo_manuale.END
	
@b.add_command_handler('start')
def start(update):
	update.reply('Benvenuto\!', reply_markup=main_keyboard)
	controllo_manuale.end() #chiudi conversazioni in caso di reset
	

b.add_conversation_handler(controllo_manuale)

b.start_loop()
