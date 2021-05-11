from flask import Flask,request, jsonify
from API import light
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/post', methods=['GET','POST'])
def post():
    data = request.get_json()    
    data = str(data['title'])
    print(data)

    light.a(data, 8, 1)

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
