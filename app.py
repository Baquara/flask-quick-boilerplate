from flask import Flask, render_template, request, jsonify
import re
import json
import requests
import json
from sqlalchemy import *


engine = create_engine('sqlite:///./banco.db?check_same_thread=False')
engine.echo = False
metadata = MetaData(engine)

app = Flask(__name__)


def dbresults(com):
    data = engine.execute(com)
    if data is not None:
        return [{key: value for key, value in row.items()} for row in data if row is not None]
    else:
        return [{}]

@app.route("/")
def home():
    data = dbresults('SELECT * FROM departamentos')
    print(data)
    return render_template("index.html")

@app.route("/retorno", methods=['POST'])
def returnebd():
    textarea = request.json.get("textarea", None)
    return textarea

if __name__ == "__main__":
    app.run()
 
