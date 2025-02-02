import telebot
import postgresql as psql
from Connection import *


# Conexão local Postgresql
con = Connection('pq://ocatolicobot:ocatolicobotpasswd@localhost/ocatolicobot')
# Conexão Externa
#con = Connection('pq://ocatolicobot:ocatolicobotpasswd@179.83.81.217/ocatolicobot')

token = '776808432:AAFusuIi1GyNlWb1nFdkWFl54s8LL89nQkw'
bot = telebot.TeleBot(token)

# Comandos de Boas Vindas.
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Olá, seja bem vindo ao O Católico Bot!')
    bot.send_message(message.chat.id, 'Estamos em processo de criação!')
    bot.send_message(message.chat.id, 'Logo logo estarei pronto para lhe ajudar a encontrar a missa/adoração/evento/confissão que estiverem disponíveis para você')
    bot.send_message(message.chat.id, 'Para mais informações ou sugestões entre em contato com: headsappsconsultoria@gmail.com')

    # Salvando dados do sobre o primeiro contato com o usuário.
    # Afim de gerar uma base de dados de todos os usuários.
    chat_id = '{' + str(message.chat.id) + '}'
    user_name = '{' + str(message.chat.username) + '}'

    sqlSaveUser = "insert into chat_users values (default, '{0}', '{1}')".format(chat_id, user_name)
    if con.manipulate(sqlSaveUser):
        print('Chat_User inserido com Sucesso')
    else:
        print('Erro ao inserir Chat_User')

# Comandos personalizados.
@bot.message_handler(func = lambda m: True)
def echo_all(message):
    send_welcome(message)


# Executa o Bot.
bot.polling()
