from app import app, cache, request, jsonify, render_template
import requests, sys, json, re
from config import token_bot, path_bot

def write_json(data, filename=f'{path_bot}/data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(filename=f'{path_bot}/data.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
    return {}

def sendMessage(chat_id, text='bla', parse_mode='html', reply_markup={}, token=token_bot):
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}

    if len(reply_markup) > 0:
        data['reply_markup'] = json.dumps(reply_markup)

    r = requests.post(
        url = f'https://api.telegram.org/bot{token_bot}/sendMessage',
        data = data,
        ).json()
    return r

@app.route(f'/{token_bot}', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        r = request.get_json()    
        # write_json(r)
        # write_json(request.method, filename = f'{path_bot}method.json')    
        chat_id = r['message']['chat']['id']
        first_name = r['message']['from']['first_name']
        message  = r['message']['text'].strip()
        # the message for echo bot
        m = [f'Hi {first_name}', message]
        sendMessage(chat_id, "\n".join(m), token = token_bot)
    return jsonify({'token':'ok'})

@app.route("/")
def index():
    return render_template("index.html", title = 'Meow!, meow', footer = 'Meow!, meow')

@app.errorhandler(404)
def page_not_found(e):    
    return render_template("404.html", title = '404', footer = 'Meows!, meows'), 404
