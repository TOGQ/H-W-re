from email.base64mime import body_decode
import requests,json

try:
    BARK_KEY = os.environ['BARK_KEY']
except:
    # 本地调试用
    BARK_KEY = ''


    # 本地调试用， please type here the website address without any 'https://' or '/'
URL_BASE = "hax"    

try:
    TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
except:
    # 本地调试用
    TG_BOT_TOKEN = ''

try:
    TG_USER_ID = os.environ['TG_USER_ID']
except:
    # 本地调试用
    TG_USER_ID = ''

try:
    FEISHU_TOKEN = os.environ['FEISHU_TOKEN']
except:
    # 本地调试用
    FEISHU_TOKEN = '3b3ae76f-9ae2-4b35-98cc-9c5afd485d3d'    


try:
    URL_BASE = os.environ['URL_BASE']
except:
    # 本地调试用， please type here the website address without any 'https://' or '/'
    URL_BASE = ''

body = "🎉 Your VPS has been renewed until November 2, 2022 "
def push(body):
    print('- body: %s \n- waiting for push result' % body)
    # bark push
    if BARK_KEY == '':
        print('*** No BARK_KEY ***')
    else:
        barkurl = 'https://api.day.app/' + BARK_KEY
        title = URL_BASE
        rq_bark = requests.get(url=f'{barkurl}/{title}/{body}?isArchive=1')
        if rq_bark.status_code == 200:
            print('- bark push Done!')
        else:
            print('*** bark push fail! ***', rq_bark.content.decode('utf-8'))
    # tg push
    if TG_BOT_TOKEN == '' or TG_USER_ID == '':
        print('*** No TG_BOT_TOKEN or TG_USER_ID ***')
    else:
        body = URL_BASE + '\n\n' + body
        server = 'https://api.telegram.org'
        tgurl = server + '/bot' + TG_BOT_TOKEN + '/sendMessage'
        rq_tg = requests.post(tgurl, data={'chat_id': TG_USER_ID, 'text': body}, headers={
            'Content-Type': 'application/x-www-form-urlencoded'})
        if rq_tg.status_code == 200:
            print('- tg push Done!')
        else:
            print('*** tg push fail! ***', rq_tg.content.decode('utf-8'))
    if FEISHU_TOKEN == '' :
        print('*** No FEISHU_TOKEN ***')
    else: 
        body = str(URL_BASE) + '\n\n' + body
        print (body)
        server = 'https://open.feishu.cn'
        fsurl = server + '/open-apis/bot/v2/hook/' + FEISHU_TOKEN
        rq_fs = requests.post(fsurl, data=json.dumps({"msg_type":"text","content":{"text": body}}), headers={
            "Content-Type": "application/json"})
        if rq_fs.status_code == 200:
            print('- fs push Done!')
        else:
            print('*** fs push fail! ***', rq_fs.content.decode('utf-8'))



    print('- finish!')
    # kill_browser()
push(body)