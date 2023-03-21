from flask import Flask, render_template, request
import redis
import configparser

# Load config file
config = configparser.ConfigParser()
config.read('config.ini')

# Connect to Redis
r = redis.Redis(
    host=config['REDIS']['host'],
    port=config['REDIS']['port'],
    db=config['REDIS']['db']
)

app = Flask(__name__)

class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

@app.route('/', methods=['GET', 'POST'])
def index():
    print(f'[{BC.OKCYAN}Event{BC.RESET}] {BC.BOLD}{BC.OKCYAN}GET{BC.RESET} request from {BC.BOLD}{BC.OKCYAN}{request.remote_addr}{BC.RESET}')
    if request.method == 'POST':
        user = request.form['twitter_handle']
        message = r.get(user)
        if message is None:
            message = "{}에 대한 답변을 찾을 수 없습니다. (대소문자 구분 있음)".format(user)
        else:
            message = message.decode('utf-8')
        return render_template('index.html', message=message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
