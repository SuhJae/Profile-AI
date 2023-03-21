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

@app.route('/', methods=['GET', 'POST'])
def index():
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
    app.run(host='0.0.0.0', debug=True)
