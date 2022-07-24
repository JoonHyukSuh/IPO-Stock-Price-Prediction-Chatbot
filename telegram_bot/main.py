
import telegram
from telegram.ext import Updater,MessageHandler,Filters
import emoji
import os


api_key = '5546249421:AAFeBf4yuVufMMs-IZYDm83cqyYAaE9MjtY'
chat_id = 5575834060
bot = telegram.Bot(token = api_key)
BASE_PATH  = os.getcwd()



info_message = '''다음의 명령어를 입력해주세요.

- 안부 물어보기 : 뭐해
- 주식 가격 물어보기 : "기업명" + 주식
- 차트 보기 : "기업명" + 차트
- 사진 보기 : 사진
'''

bot.sendMessage(chat_id = chat_id,text='안녕하세요 IPO 공모가 예측 봇 Stock-Manager 입니다.') # 채팅방에 입장했을 때, 인사말 
bot.sendMessage(chat_id = chat_id,text=info_message)

# updater
updater = Updater(token=api_key, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling() # 주기적으로 텔레그램 서버에 접속해서 chatbot으로부터 새로운 메세지가 존재하면 받아오는 명령어.

def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.

    if '뭐해' in user_text: 
        bot.send_message(chat_id=chat_id, text="챗봇에 대해 공부하는 중이에요.") # 답장 보내기
    elif '주식'in user_text: 
        cor_name = user_text.split()[0]
        bot.send_message(chat_id=chat_id, text=f"{cor_name} 주식의 현재 가격은 0000원 입니다.") # 답장 보내기
    elif '차트' in user_text:
        cor_name = user_text.split()[0]
        bot.send_message(chat_id=chat_id, text=f"{cor_name}주식의 차트를 불러오는 중입니다!")
        bot.send_message(chat_id =chat_id,text=emoji.emojize(':chart_with_upwards_trend:',language='alias'))

    elif '사진' in user_text:
        bot.send_photo(chat_id = chat_id, photo=open(BASE_PATH+'/telegram_bot/test_chart.jpeg','rb')) #

echo_handler = MessageHandler(Filters.text,handler) # chatbot에게 메세지를 전송하면,updater를 통해 필터링된 text가 handler로 전달이 된다. -> 가장 중요하고, 계속해서 수정할 부분

dispatcher.add_handler(echo_handler)



