import requests
import telebot
from telebot import types
from time import sleep
Done = 0
Error = 0
token = input('[~] Enter Token :')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        sent = bot.send_message(message.chat.id, text='Hi bro📮\n\n ارسل حسابك بهذا النمط :\nيوزر الوهمي : باسورد الوهمي : يوزر حسابك')
        bot.register_next_step_handler(sent, login)
def login(message):
        global Done,Error
        username = message.text.split(':')[0]
        password = message.text.split(':')[1]
        usernamee = message.text.split(':')[2]
        url_log = 'https://bayitakipci.com/memberlogin?'
        headers_log = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '101',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'afc294f33a01e23b1ff9bdb5d8a57c57=cd15ea0423f399cfeee06acb9e8085bf; _ga=GA1.2.1863789683.1621358532; _gid=GA1.2.791918419.1621358532',
                'origin': 'https://bayitakipci.com',
                'referer': 'https://bayitakipci.com/memberlogin',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

        data_log = {
                'username': username,
                'password': password,
                'userid': '',
                }

        reqqq = requests.post(url_log, headers=headers_log, data=data_log)
        if '"status":"success","returnUrl":"\/tools"' in reqqq.text:
            r = reqqq.cookies['afc294f33a01e23b1ff9bdb5d8a57c57']
            bot.send_message(message.chat.id, text='*تم تسجيل دخول ✅!*', parse_mode='markdown')
            url = f'https://www.instagram.com/{usernamee}/?__a=1'
            headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': 'csrftoken=MmU9R8bA9VJYzannZljTyjjlNWOO4hsC; mid=YKQDCwALAAGNJ4hMdeFUCVoxA_bO; ig_did=E14AB5AD-1BFF-4229-A9D9-D5FE3988725E; ig_nrcb=1',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            }
            req12 = requests.get(url,headers=headers).json()
            if 'graphql' in req12:
                iduser = str(req12['graphql']['user'].get('id'))
                url_follow = f'https://bayitakipci.com/tools/send-follower/{iduser}?formType=send'
                headers_follow = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '41',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'cookie': f'_ga=GA1.2.515201356.1621362121; _gid=GA1.2.832356304.1621362121; afc294f33a01e23b1ff9bdb5d8a57c57={r}',
                    'origin': 'https://bayitakipci.com',
                    'referer': f'https://bayitakipci.com/tools/send-follower/{iduser}',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }
                data = {
                    'adet': '50',
                    'userID': iduser,
                    'userName': usernamee,
                }
                req_follow = requests.post(url_follow, headers=headers_follow, data=data).text
                print(req_follow)
                bot.send_message(message.chat.id, text='Started (:')
                if '"status":"success"' in req_follow:
                    bot.send_message(message.chat.id, text="تم ارسل 50 متابع !", parse_mode='markdown')
                else:
                    pass
