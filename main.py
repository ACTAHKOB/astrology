import telebot
import telethon.sync
import telethon.errors
import telethon.sessions

# Импортируйте необходимые модули:
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
#from telethon.tl.functions import ChannelParticipantsSearch
# Получите ключи API и секретный ключ для работы с API Telegram. 
# Для этого нужно зарегистрировать свое приложение на сайте https://my.telegram.org/auth.
api_id = 22874196
api_hash = 'bc8fb121b166e7e7731b9188895d2542'



#Создать сессию Telethon:
session = telethon.sessions.StringSession()

#Авторизоваться в Telegram API:
client = telethon.sync.TelegramClient(session, api_id, api_hash)
client.start()

#Получить информацию о группе:
group_entity = client.get_entity('horoscope_astrolog')

#Получить список участников группы:
participants = client.get_participants(group_entity)
usernames = list()
#Пройти по списку участников и проверить наличие у них username:
for participant in participants:
    if participant.username:
        usernames.append(participant.username)





bot = telebot.TeleBot('6075105291:AAG3_jsefRmepKAEMrAqPkmYH4NmMu3SjpY')


channel_id = '-1001328883095' #группа @horoscope_astrolog
previous_message = ''

@bot.message_handler(commands=['help', 'start'])
def startMessage(message):
    bot.send_message(message.chat.id, 'Добрый день. Этот бот позволяет получить информацию о членстве определенного человека/людей в канале \n Напишите юзернеймы пользователей которые хотите проверить, (НО БЕЗ "@")')

@bot.message_handler(content_types=['text'])
def GetList(message):
    UserList = message.text.split()
    
    list_in = []
    list_not_in = []
    global usernames


    
    for i in UserList:
        if i in usernames:
            list_in.append(i)
        else:
            list_not_in.append(i)
    str_in = ''
    str_not_in = ''
    for i in list_in:
        str_in += i
        str_in += ' '

    for i in list_not_in:
        str_not_in += i
        str_not_in += ' '
    bot.send_message(message.chat.id, f'пользователи которые состоят в группе: {str_in}')
    bot.send_message(message.chat.id, f'пользователи которые HE состоят в группе: {str_not_in}')

bot.polling(non_stop=True)

    


