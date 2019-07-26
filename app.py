from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.environ.get('FLASK_NAME')
    return f'Hello, {name if name is not None else "Damon"}!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
