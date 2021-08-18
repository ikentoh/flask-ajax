import os

from flask import Flask
from flask_cors import CORS


#
# flask app本体定義
#


# flask app生成
app = Flask(__name__)
CORS(app)

# secret key生成
secret_key = os.urandom(16)
print('current secret_key: ', secret_key)
app.secret_key = secret_key


@app.route(r'/', methods=['GET'])
def index():
    return 'hello, world!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050, threaded=True)
